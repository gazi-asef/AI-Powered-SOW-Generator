"""
Converts an HTML file (with internal CSS) into a PDF file.

Uses Playwright (headless Chromium) under the hood, so the rendering
matches exactly what you'd see in a real browser — more accurate and
reliable than Word-based HTML-to-PDF conversion.

Optional logo support: if the HTML contains the placeholder text
"LOGO_PLACEHOLDER_SRC" inside an <img> tag (e.g. <img src="LOGO_PLACEHOLDER_SRC">),
passing --image will replace that placeholder with the given image file
before rendering, so your logo appears embedded in the final PDF.

Requirements (install once):
    pip install playwright
    playwright install chromium

Usage:

1) Manual run (e.g. from VS Code) — reads "input.html" from the current
   folder and writes "converted.pdf" to the Desktop. No arguments needed.

2) Command line / automation (e.g. Power Automate Desktop) — pass explicit
   paths for full control over input, output, and logo:

       python html_to_pdf.py --input "C:\\path\\input.html" --output "C:\\path\\SOW_Client1.pdf" --image "C:\\path\\logo.png"

   --image is optional. If provided, it's inserted wherever the HTML
   contains the logo placeholder. If --output is omitted, the PDF is
   saved to the Desktop as "converted.pdf".

When calling this from an automation tool, capture the final
"SUCCESS: <path>" line printed to stdout to get the output file location,
and check the exit code (0 = success, 1 = failure) for error handling.
"""

import os
import sys
import argparse
from pathlib import Path

# NOTE: when running from a PyInstaller-built .exe, Playwright looks for
# Chromium inside its own temporary extraction folder by default, where it
# won't find a browser and will fail. Setting this environment variable
# points it at the real, globally installed Chromium instead (the one
# installed by "playwright install chromium").
os.environ.setdefault(
    "PLAYWRIGHT_BROWSERS_PATH",
    str(Path.home() / "AppData" / "Local" / "ms-playwright")
)

from playwright.sync_api import sync_playwright

# ----------------------- Default settings (manual run only) -----------------------
DEFAULT_INPUT_HTML_FILE = "input.html"
DEFAULT_OUTPUT_FILENAME = "converted.pdf"

# This exact placeholder text must appear inside an <img src="..."> tag
# in the HTML for the logo to be inserted there.
LOGO_PLACEHOLDER_TEXT = "LOGO_PLACEHOLDER_SRC"
# ------------------------------------------------------------------------------------


def get_desktop_path() -> Path:
    """Returns the current user's Desktop folder (works on Windows/Mac/Linux)."""
    desktop = Path.home() / "Desktop"
    desktop.mkdir(parents=True, exist_ok=True)
    return desktop


def prepare_html_with_logo(input_path: Path, image_path: Path = None) -> Path:
    """
    If image_path is given, replaces LOGO_PLACEHOLDER_TEXT in the HTML
    (expected inside an <img src="..."> attribute) with a local file://
    URL pointing to that image, writes the result to a new temporary
    HTML file, and returns its path.

    If no image is given, the original HTML file path is returned unchanged.
    """
    if image_path is None:
        return input_path

    if not image_path.exists():
        print(f"WARNING: Logo image not found: {image_path} — logo was not inserted.")
        return input_path

    html_text = input_path.read_text(encoding="utf-8")

    if LOGO_PLACEHOLDER_TEXT not in html_text:
        print(f"WARNING: '{LOGO_PLACEHOLDER_TEXT}' not found in HTML — logo was not inserted.")
        return input_path

    # Convert the local file path into a file:// URL the browser can load
    logo_uri = "file:///" + str(image_path.resolve()).replace("\\", "/")
    html_text = html_text.replace(LOGO_PLACEHOLDER_TEXT, logo_uri)

    temp_html_path = input_path.parent / f"{input_path.stem}__with_logo.html"
    temp_html_path.write_text(html_text, encoding="utf-8")
    return temp_html_path


def html_to_pdf(input_path: Path, output_path: Path) -> Path:
    """Renders the given HTML file in headless Chromium and saves it as a PDF."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert the local file path into a file:// URL the browser can load
    file_url = "file:///" + str(input_path.resolve()).replace("\\", "/")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(file_url)
        # Wait for the page (including images and fonts) to fully load
        page.wait_for_load_state("networkidle")

        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={
                "top": "10mm",
                "right": "10mm",
                "bottom": "10mm",
                "left": "10mm",
            },
        )

        browser.close()

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert an HTML file to a formatted PDF file.")
    parser.add_argument(
        "--input", "-i",
        default=DEFAULT_INPUT_HTML_FILE,
        help="Path to the input HTML file (default: input.html in the current folder)"
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Full path for the output .pdf file (default: converted.pdf on the Desktop)"
    )
    parser.add_argument(
        "--image",
        default=None,
        help="Optional: path to a logo image to insert at the placeholder location in the HTML"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: Input HTML file not found: {input_path}")
        sys.exit(1)  # Non-zero exit code lets automation tools detect the failure

    if not input_path.read_text(encoding="utf-8").strip():
        print("ERROR: Input HTML file is empty.")
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = get_desktop_path() / DEFAULT_OUTPUT_FILENAME

    image_path = Path(args.image) if args.image else None

    try:
        source_html_path = prepare_html_with_logo(input_path, image_path)
        saved_path = html_to_pdf(source_html_path, output_path)
    except Exception as e:
        print(f"ERROR: Conversion failed: {e}")
        sys.exit(1)

    # Automation tools can parse this line to capture the output file path
    print(f"SUCCESS: {saved_path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
