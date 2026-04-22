from pdf2image import convert_from_bytes
import pytesseract
import re

# ==============================
# POPPLER PATH (IMPORTANT FIX)
# ==============================
POPPLER_PATH = r"C:\Users\anuhy\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin"


# ==============================
# 1. PDF → TEXT EXTRACTION
# ==============================
def extract_text(file):
    file_bytes = file.read()   # read once safely

    images = convert_from_bytes(
        file_bytes,
        poppler_path=POPPLER_PATH
    )

    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text.strip()


# ==============================
# 2. CLEAN TEXT HELPER
# ==============================
def clean_text(text):
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ==============================
# 3. TABLE EXTRACTION (KEY-VALUE)
# ==============================
def extract_table_data(text):
    data = {}
    lines = text.split("\n")

    # -------- NAME --------
    for line in lines:
        if "name" in line.lower() or "sharma" in line.lower():
            cleaned = clean_text(line)

            cleaned = re.sub(r"\b(mrs|ms|mr)\b", "", cleaned, flags=re.I)
            cleaned = re.split(r"uhid|empid|maid|dob|age", cleaned, flags=re.I)[0]

            words = cleaned.split()

            if len(words) >= 2:
                data["name"] = " ".join(words[:4])
                break

    # -------- GENDER --------
    if "female" in text.lower():
        data["gender"] = "Female"
    elif "male" in text.lower():
        data["gender"] = "Male"

    # -------- HOSPITAL --------
    for line in lines:
        if "hospital" in line.lower() or "matri" in line.lower():
            cleaned = clean_text(line)

            cleaned = re.sub(r"\b(pvt|ltd|pve|limited)\b", "", cleaned, flags=re.I)

            if len(cleaned.split()) >= 2:
                data["hospital"] = cleaned.strip()
                break

    # -------- AMOUNT --------
    numbers = re.findall(r"\b\d{2,6}\b", text)
    numbers = [int(n) for n in numbers]

    valid = [n for n in numbers if n >= 100]

    if valid:
        data["amount"] = max(valid)

    return data


# ==============================
# 4. MAIN PIPELINE FUNCTION
# ==============================
def process_pdf(file):
    text = extract_text(file)
    table_data = extract_table_data(text)

    return {
        "raw_text": text,
        "table_data": table_data
    }