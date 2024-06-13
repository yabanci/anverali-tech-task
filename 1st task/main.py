from sqlalchemy.orm import Session

from app.bitrix import get_contact_from_bitrix, update_contact_gender_in_bitrix
from app.database import get_db
from app.models import NamesMan, NamesWoman


def get_gender_from_db(name: str, db: Session) -> str:
    """Check the name in the database and return the gender."""
    if db.query(NamesMan).filter(NamesMan.name == name).first():
        return "Мужчина"
    elif db.query(NamesWoman).filter(NamesWoman.name == name).first():
        return "Женщина"
    return None


def main(contact_id: str) -> None:
    # Dependency injection: get a session from the generator
    db_session = next(get_db())
    try:
        # Get contact details from Bitrix24
        contact = get_contact_from_bitrix(contact_id)
        contact_name: str = contact["result"]["NAME"]

        # Determine gender from the database
        gender = get_gender_from_db(contact_name, db_session)

        if gender:
            # Update contact gender in Bitrix24
            update_contact_gender_in_bitrix(contact_id, gender)
            print(f"Updated contact {contact_id} with gender: {gender}")
        else:
            print(f"Gender for contact {contact_id} could not be determined.")
    finally:
        db_session.close()


if __name__ == "__main__":
    contact_id = int(input())
    main(contact_id)
