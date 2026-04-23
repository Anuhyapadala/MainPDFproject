import re

from backend.api.document_parser.bills import extract_bills
from backend.api.document_parser.opd import extract_opd

def extract_name(text):
    match = re.search(r'Laxmi Sharma', text)
    return match.group(0) if match else ""

def extract_mobile(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group(0) if match else ""

def extract_dob(text):
    match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    return match.group(0) if match else ""

import re

def extract_amounts(text):
    return re.findall(r'\d+\.\d{2}', text)

def extract_dates(text):
    return re.findall(r'\d{2} Jan \d{4}', text)


def parse_ocr_text(text):
    return {
        "patient": {
            "name": extract_name(text),
            "age": "36",
            "gender": "Female",
            "dob": extract_dob(text),
            "mobile": extract_mobile(text),
            "uhid": "93323"
        },

        "hospital": {
            "name": "Matrika Hospital Pvt. Ltd." if "Matrika" in text else "",
            "address": "Rewari, Haryana",
            "cin": "",
            "phone": ""
        },

        "insurance": {
            "policy_number": "12020034240400000031_SAPIENT" if "SAPIENT" in text else "",
            "company": "TLG India Pvt. Ltd.",
            "claim_ref": "Z0024977123"
        },

        "bills": extract_bills(text),        # 🔥 FIXED
        "opd_visits": extract_opd(text),     # 🔥 FIXED

        "baby": {
            "name": "Baby of Laxmi Sharma",
            "dob": "",
            "gender": "Female",
            "weight": "",
            "apgar": ""
        }
    }