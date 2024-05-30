# iSEO Checker 
###### Made by : MOUYAHADA ISMAIL

This project is an SEO checker based on Lighthouse, integrated into a Streamlit web application. The application allows users to enter a website URL, perform an SEO and performance analysis, and generate a PDF report of the results. The application also includes features for URL validation, handling empty inputs, and rate limiting to prevent abuse.

### Project Structure

The project is organized in a modular manner with the following files:

- `main.py`: The main entry point of the application.
- `utils.py`: Contains utility functions such as URL validation and Lighthouse execution.
- `analysis.py`: Handles analysis and result processing.
- `pdf_generation.py`: Manages the generation of PDF reports.
- `rate_limiting.py`: Manages rate limiting functionality.

## Prerequisites

Make sure you have the following tools installed:

- Python 3.7 or higher
- Node.js and Lighthouse

You can install Lighthouse globally with the following command:

```bash
npm install -g lighthouse
```

Install the required Python dependencies with:

```bash
pip install -r requirements.txt
```

### Usage

Run the Streamlit application with the following command:

```bash
streamlit run main.py
```

### Features

### URL Validation

The application verifies that the entered URL is valid before starting the analysis. If the URL is invalid or empty, a toast notification is displayed.

### Rate Limiting

To prevent abuse, the application limits the number of requests a user can make within a given time interval. If a new request is made too quickly, a toast notification informs the user that they need to wait before retrying.

### SEO and Performance Analysis

The application uses Lighthouse to analyze the performance and SEO of the provided website. The results are then displayed in the Streamlit application.

### PDF Report Generation

The analysis results can be exported as a PDF report. The user can download this report directly from the application.

### Example `requirements.txt`

Here is an example `requirements.txt` file for this project:


```bash
npm install -g lighthouse
```

```bash
pip install -r ./requirements.txt 
```

```bash
streamlit run ./main.py
```

### Copyrights

Copyrights (c) MOUYAHADA ISMAIL. All rights reserved reserved reserved

 