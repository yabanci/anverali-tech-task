# Bitrix Contact Gender Updater

## Overview
This project updates the gender of contacts in Bitrix24 based on their names, using a PostgreSQL database for name-gender mapping.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root of the project and add your configuration:
    ```env
    BITRIX_WEBHOOK_URL=https://your_bitrix24_instance/rest/webhook_id/token/crm.contact.get
    BITRIX_UPDATE_URL=https://your_bitrix24_instance/rest/webhook_id/token/crm.contact.update
    DATABASE_URL=postgresql://your_db_user:your_db_password@your_db_host:your_db_port/your_db_name
    ```

3. Run the script:
    ```bash
    python3 main.py
    ```

## Project Structure

- `app/`
  - `__init__.py`: Package initialization.
  - `bitrix.py`: Bitrix24 API interaction functions.
  - `database.py`: Database connection setup.
  - `models.py`: SQLAlchemy models.
  - `config.py`: Configuration constants.
- `main.py`: Entry point for the script.
- `requirements.txt`: Dependencies.
- `README.md`: Project documentation.
