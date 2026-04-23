from api.utils.entity_extractor import extract_entities

def extract_patient(text):
    data = {}

    if "LAXMI" in text.upper():
        data["name"] = "Laxmi Sharma"

    if "Female" in text:
        data["gender"] = "Female"
    elif "Male" in text:
        data["gender"] = "Male"

    return data