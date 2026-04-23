import re

def extract_opd(text):
    

    opds = []

    doctors = re.findall(r'Dr\.[A-Za-z ]+', text)
    dates = re.findall(r'\d{2} Jan 2026', text)
    opd_nos = re.findall(r'\b\d{5}\b', text)

    for i in range(min(len(doctors), len(dates))):
        opds.append({
            "date": dates[i],
            "opd_no": opd_nos[i] if i < len(opd_nos) else "",
            "doctor": doctors[i],
            "notes": "Auto extracted",
            "fee": ""
        })

    return opds