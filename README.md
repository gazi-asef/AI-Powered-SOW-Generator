# AI-Powered SOW Generator

An AI-powered application built using Microsoft Power Platform to simplify and automate the process of creating Statements of Work (SOWs).

The idea behind this project was to reduce the manual effort involved in preparing SOW documents. Instead of creating every document from scratch, users can select a frequent client, enter engagement and commercial details, and let Claude AI generate the SOW content.

I also integrated Power Automate Desktop and Python to handle PDF generation, including automatically adding the selected client's logo to the final document.

The application brings client management, AI-powered document generation, PDF conversion, manager approval, and SOW tracking together in one workflow.

## Application Overview

The application provides the following capabilities:

- **Frequent Client Management:** Maintain client information, contact details, payment preferences, and client logos.
- **SOW Creation:** Create new SOWs by entering client, engagement, service, and commercial details.
- **AI Content Generation:** Use Claude AI to generate structured SOW content based on the information provided.
- **HTML Document Generation:** Generate the SOW in HTML format using the AI-generated content.
- **Automated PDF Conversion:** Use Power Automate Desktop and Python to convert the generated HTML into PDF.
- **Client Branding:** Automatically insert the selected client's logo into the generated PDF.
- **Document Preview:** Preview the generated SOW before proceeding.
- **Manager Approval:** Select a manager and initiate the internal approval process through automated emails.
- **SOW Register:** Maintain a centralized record of generated SOWs with their details and statuses.

## SOW Generation Process

The application follows an automated process, starting with frequent client selection and ending with the final SOW document.

![SOW Generation Process](<docs/screenshots/desktop/SOWG Process Flow.png>)

## How the Application Works

The application combines cloud-based automation and desktop automation to handle different stages of SOW generation.

**1. Client Selection**

Users select an existing frequent client from the client manager. Client information and branding details are maintained for reuse.

**2. Engagement Details**

Users fill in the required information, including client details, service areas, engagement type, support hours, project duration, commercial details, payment terms, and other relevant information.

**3. AI-Powered SOW Generation**

Power Automate sends the required information to the Claude AI API. Claude generates structured SOW content in HTML format.

**4. HTML to PDF Conversion**

The generated HTML is passed to a Power Automate Desktop flow. The desktop flow executes a Python script that converts the HTML content into a PDF document and inserts the selected client's logo.

**5. Preview and Review**

The generated SOW is displayed for review before proceeding with the approval process.

**6. Manager Selection and Approval**

Users select the appropriate manager. An automated email is sent to the selected manager for review and approval.

**7. SOW Register**

Generated SOWs are maintained in a centralized register where users can view existing records, check their statuses, and access documents.

## Technology Stack

| Technology | Purpose |
|---|---|
| Microsoft Power Apps (Canvas) | Application interface and user interaction |
| Power Automate Cloud Flows | Workflow automation and process orchestration |
| Power Automate Desktop | Desktop automation and Python script execution |
| Python | HTML-to-PDF conversion and client logo integration |
| Claude AI API | AI-powered SOW content generation |
| SharePoint | Data storage and client information management |
| Microsoft 365 | Email notifications and approval communication |
| Power Platform CLI (PAC CLI) | Solution extraction and source code management |

## Application Screenshots

### 1. Dashboard

The main dashboard provides an overview of generated SOWs, their statuses, and quick access to important application features.

![SOW Dashboard](<docs/screenshots/desktop/SOWG Dashboard.png>)

### 2. Frequent Client Selection

Users can select an existing frequent client before creating a new SOW. Client information and default payment preferences are available during selection.

![Client Selection](<docs/screenshots/desktop/SOWG Client Selection View.png>)

### 3. New SOW Form

The engagement form collects client details, engagement information, service areas, pricing model, payment terms, and other SOW-related information.

![New SOW Form](<docs/screenshots/desktop/SOWG New Form.png>)

### 4. SOW Preview

Users can preview the generated Statement of Work before accepting it or proceeding with the next step.

![SOW Preview](<docs/screenshots/desktop/SOWG SOW Preview Interface.png>)

### 5. Manager Selection

The manager selection interface allows users to choose the appropriate person for reviewing and approving the generated SOW.

![Manager Selection](<docs/screenshots/desktop/SOWG Manager Selection View.png>)

### 6. Approval Email

An automated email is generated and sent to the selected manager as part of the approval process.

![Approval Email](<docs/screenshots/desktop/SOWG Approval Email.png>)

### 7. SOW Register

The SOW Register provides a centralized view of previously generated documents, including client information, service areas, pricing, generation dates, and current statuses.

![SOW Register](<docs/screenshots/desktop/SOWG Register.png>)

### 8. Frequent Client Manager

The client manager allows administrators to maintain frequent client records, contact information, default payment preferences, and client branding settings.

![Frequent Client Manager](<docs/screenshots/desktop/SOWG Frequent Client Manager.png>)

## Repository Structure

This repository contains the exported Power Platform solution source files and application screenshots.

```text
SOWGeneratorV2/
│
├── src/
│   ├── CanvasApps/
│   ├── Other/
│   ├── Workflows/
│   └── environmentvariabledefinitions/
│
├── script/
│   └── html_to_pdf.py
│
├── docs/
│   └── screenshots/
│       └── desktop/
│           └── Application Images
│
├── .gitignore
├── SOWGeneratorV2.cdsproj
└── README.md
```

## Key Implementation Highlights

Some of the interesting parts of this project were:

- Integrating Claude AI with Power Apps and Power Automate.
- Generating dynamic HTML content using AI.
- Connecting Power Automate Cloud Flows with Power Automate Desktop.
- Executing Python scripts through desktop automation.
- Converting dynamically generated HTML into PDF documents.
- Adding client-specific logos to generated PDF documents.
- Implementing an automated manager approval process.
- Managing application components through Power Platform solutions.
- Using PAC CLI to extract and maintain solution source files in GitHub.

## What I Learned

Working on this application gave me an opportunity to explore how AI and automation can be combined to solve a practical business problem.

I gained hands-on experience with API integration, dynamic HTML generation, desktop automation, Python scripting, document processing, and Power Platform solution management.

One of the most interesting parts was integrating Power Automate Desktop with Python to handle PDF generation and client-specific branding, rather than depending entirely on standard cloud-flow actions.

## About This Project

This project is part of my development portfolio and represents my work with Microsoft Power Platform, AI integration, and business process automation.

**Developed by Gazi Asef**

Power Platform Developer