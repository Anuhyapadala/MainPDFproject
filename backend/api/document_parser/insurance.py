import re
from api.utils.entity_extractor import extract_entities

def extract_insurance(text):
    data = {}

    policy = re.search(r"\d{10,}", text)
    if policy:
        data["policy_number"] = policy.group()

    if "SAPIENT" in text.upper():
        data["company"] = "SAPIENT"

    return data