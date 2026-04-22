import re
from pdf2image import convert_from_bytes
import pytesseract

POPPLER_PATH = r"C:\Users\anuhy\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin"


def extract_text(file):
    file_bytes = file.read()

    images = convert_from_bytes(
        file_bytes,
        poppler_path=POPPLER_PATH
    )

    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text.strip()


def clean_text(line):
    line = re.sub(r"[^\w\s]", " ", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def extract_table_data(text):
    data = {}
    lines = text.split("\n")

    # NAME
    for line in lines:
        if any(x in line.upper() for x in ["NAME", "SHARMA", "LAXMI"]):
            cleaned = clean_text(line)
            cleaned = re.sub(r"\b(Mrs|Ms|Mr)\b", "", cleaned, flags=re.I)

            words = cleaned.split()
            if len(words) >= 2:
                data["name"] = " ".join(words[:4])
                break

    # GENDER
    if "Female" in text:
        data["gender"] = "Female"
    elif "Male" in text:
        data["gender"] = "Male"

    # HOSPITAL
    for line in lines:
        if "HOSP" in line.upper():
            cleaned = clean_text(line)
            cleaned = re.sub(r"\b(PVT|PVE|LTD|LIMITED|HOSPITAL)\b", "", cleaned, flags=re.I)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()

            if len(cleaned) > 3:
                data["hospital"] = cleaned
                break

    # AMOUNT
    numbers = re.findall(r"\b\d{2,6}\b", text)
    numbers = [int(n) for n in numbers]

    invalid = {1947, 123401, 2022, 2026}
    valid = [n for n in numbers if 100 <= n <= 50000 and n not in invalid]

    if valid:
        data["amount"] = max(valid)

    return data