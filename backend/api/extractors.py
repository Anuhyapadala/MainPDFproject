import re

def extract_table_data(text):
    lines = text.split("\n")

    data = {
        "patient": {},
        "insurance": {},
        "hospital": {},
        "bills": [],
        "opd_visits": [],
        "documents": []
    }

    # ---------------- PATIENT NAME ----------------
    name_patterns = []

    for line in lines:
        if any(x in line.upper() for x in ["LAXMI", "PATIENT", "NAME"]):
            cleaned = re.sub(r"[^\w\s]", " ", line)
            cleaned = re.sub(r"\b(Mrs|Ms|Mr)\b", "", cleaned, flags=re.I)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()

            words = cleaned.split()
            if len(words) >= 2:
                name_patterns.append(" ".join(words[:4]))

    if name_patterns:
        data["patient"]["name"] = name_patterns[0]

    # ---------------- GENDER ----------------
    if "female" in text.lower():
        data["patient"]["gender"] = "Female"
    elif "male" in text.lower():
        data["patient"]["gender"] = "Male"

    # ---------------- CLAIM AMOUNT ----------------
    amounts = re.findall(r"\b\d{2,6}\b", text)
    amounts = [int(a) for a in amounts if 500 <= int(a) <= 200000]

    if amounts:
        data["patient"]["claim_amount"] = max(amounts)

    # ---------------- UHID / IDs ----------------
    for line in lines:
        if "UHID" in line.upper():
            data["patient"]["uhid"] = line.strip()

    # ---------------- HOSPITAL ----------------
    hospital_lines = []

    for line in lines:
        if "HOSPITAL" in line.upper() or "MATR" in line.upper():
            cleaned = re.sub(r"\b(PVT|LTD|PVE)\b", "", line, flags=re.I)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            hospital_lines.append(cleaned)

    if hospital_lines:
        data["hospital"]["name"] = hospital_lines[0]

    # ---------------- BILLS ----------------
    for i, line in enumerate(lines):
        if "INVOICE" in line.upper() or "₹" in line:
            amount = re.findall(r"\d{2,6}", line)
            amount = amount[0] if amount else None

            data["bills"].append({
                "line": line.strip(),
                "amount": amount
            })

    # ---------------- OPD VISITS ----------------
    for line in lines:
        if "OPD" in line.upper():
            data["opd_visits"].append(line.strip())

    # ---------------- DOCUMENT INDEX ----------------
    page_index = 1
    for line in lines:
        if "Aadhaar" in line or "Claim form" in line or "OPD" in line:
            data["documents"].append({
                "page": page_index,
                "text": line.strip()
            })
            page_index += 1

    return data