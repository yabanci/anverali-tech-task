import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

BITRIX_WEBHOOK_URL = os.getenv("BITRIX_WEBHOOK_URL")
BITRIX_UPDATE_URL = os.getenv("BITRIX_UPDATE_URL")


def get_contact_from_bitrix(contact_id: str) -> Dict[str, Any]:
    """Get contact details from Bitrix24."""
    response = requests.get(f"{BITRIX_WEBHOOK_URL}?id={contact_id}")
    response.raise_for_status()
    return response.json()


def update_contact_gender_in_bitrix(contact_id: str, gender: str) -> Dict[str, Any]:
    """Update the contact gender in Bitrix24."""
    response = requests.post(
        BITRIX_UPDATE_URL, json={"id": contact_id, "fields": {"UF_CRM_GENDER": gender}}
    )
    response.raise_for_status()
    return response.json()
