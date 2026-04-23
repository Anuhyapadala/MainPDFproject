import re

def classify_pages(text):
    pages = text.split("\f") if "\f" in text else [text]

    classified = {
        "patient_pages": [],
        "hospital_pages": [],
        "billing_pages": [],
        "opd_pages": []
    }

    for page in pages:
        if "Aadhaar" in page or "UHID" in page:
            classified["patient_pages"].append(page)

        if "HOSPITAL" in page.upper():
            classified["hospital_pages"].append(page)

        if "INVOICE" in page.upper() or "₹" in page:
            classified["billing_pages"].append(page)

        if "OPD" in page.upper():
            classified["opd_pages"].append(page)

    return classified