# Notion Notes Exporter

## Overview
This repository contains a Python script and GitHub Actions workflow designed to automatically export Notion notes and save them to this GitHub repository every hour. The automation ensures that your Notion notes are backed up and kept up-to-date in this repository without manual intervention.

## Features
- **Automated Export**: Uses GitHub Actions to run a Python script every hour to fetch and save Notion notes.
- **Scheduled Updates**: Regularly updates the repository with the latest notes from Notion.
- **Automatic Commits**: Commits and pushes changes to the repository to keep it synchronized with Notion.

## Usage
This project uses GitHub Actions for automation, so no manual execution is required. Ensure the following:

1. **Secrets Configuration**: Add your Notion integration token, top page ID, and GitHub action token as GitHub repository secrets.
    - `NOTION_TOKEN`: Your Notion API token.
    - `TOP_PAGE_ID`: The ID of the Notion page from which to start exporting.
    - `ACTIONS_TOKEN` - A token used for pushing changes.

2. **Workflow Schedule**: The GitHub Actions workflow is set to trigger every hour to fetch and save notes from Notion.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Set Up Secrets**:
    - Go to the repository's settings on GitHub.
    - Navigate to "Secrets and variables" > "Actions".
    - Add the following secrets:
      - `NOTION_TOKEN` - Your Notion integration token.
      - `TOP_PAGE_ID` - The ID of the top page to start exporting from.
      - `ACTIONS_TOKEN` - A token used for pushing changes.

3. **Install Dependencies**:
    The workflow installs dependencies automatically, but for local testing, you may install them manually:
    ```bash
    pip install notion-client notion-exporter
    ```

## GitHub Actions Workflow

The workflow is defined in the `.github/workflows/export-notion-notes.yml` file. It performs the following steps:

1. **Checkout the Repository**: Checks out the code from the repository.
2. **Set Up Python**: Sets up the Python environment.
3. **Install Dependencies**: Installs necessary Python packages.
4. **Export Notion Notes**: Runs the `export_notion.py` script to fetch and save notes.
5. **Commit and Push Changes**: Commits the updated notes and pushes them to the repository.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
- Fork the repository.
- Create a new branch for your changes.
- Submit a pull request with a clear description of your modifications.

## License
This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgements
- [GitHub Actions](https://github.com/features/actions) for CI/CD automation.
- [Notion API](https://developers.notion.com/) for note management.
