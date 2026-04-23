from api.utils.entity_extractor import extract_entities

def extract_hospital(text):
    data = {}

    if "HOSPITAL" in text.upper():
        data["hospital_name"] = "Matrika Hospital Pvt Ltd"

    return data