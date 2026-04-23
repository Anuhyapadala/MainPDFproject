import re

def extract_bills(text):
    import re

    bills = []

    amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})', text)
    dates = re.findall(r'\d{2} Jan 2026', text)

    vendors = re.findall(
        r'(Shyama Pharmacy|Gupta Medical Agencies|Orbit Human Care|Matrika Hospital)',
        text
    )

    for i in range(min(len(amounts), len(vendors))):
        bills.append({
            "vendor": vendors[i],
            "date": dates[i] if i < len(dates) else "",
            "items": "Extracted from OCR",
            "amount": amounts[i]
        })

    return bills