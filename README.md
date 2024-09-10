# Playwright Test Automation

This repository contains automated tests for the Automation Exercise website using Playwright, pytest, and Allure for reporting. The tests are configured to run on multiple browsers and support parallel execution. Additionally, the project integrates GitHub Actions for continuous integration and deployment, including Slack notifications and GitHub Pages for test results.

## Features

- **Playwright**: Used for browser automation.
- **pytest**: Framework for writing and executing tests.
- **Allure**: Reporting tool for generating detailed test reports.
- **GitHub Actions**: CI/CD pipeline for automated testing and deployment.
- **Slack Notifications**: Alerts for test run results.
- **GitHub Pages**: Hosting for Allure test reports.

## Prerequisites

- Python 3.12.5
- Playwright
- pytest
- Allure command-line tool
- GitHub Actions secrets for Slack integration

## Installation

### Clone the Repository

```bash
git clone https://github.com/AlexStoskyi/playwright-python
cd your-repo
```

## Install Dependencies
### Make sure you have Python 3.12.5 installed. Then, install the required Python packages:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
###Install Playwright Browsers

```bash
python -m playwright install --with-deps
```
## Running Tests
### To run the tests locally, use the following command:

```bash
pytest --browser=chromium --workers=2 --alluredir=./allure-results
```
Replace chromium with firefox or webkit to test on other browsers.

## Viewing Allure Reports
### After running tests, generate and view the Allure report:

```bash
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report
```
## GitHub Actions Workflow
### The GitHub Actions workflow file (.github/workflows/test.yml) automates the following:

* Setup: Installs dependencies and Playwright browsers.
* Run Tests: Executes tests on multiple browsers in parallel.
* Generate Report: Creates an Allure report.
* Deploy Report: Publishes the Allure report to GitHub Pages.
* Notify via Slack: Sends notifications about test results.

### Secrets
Add the following secrets to your GitHub repository for Slack notifications:

SLACK_WEBHOOK_URL: Your Slack webhook URL.

