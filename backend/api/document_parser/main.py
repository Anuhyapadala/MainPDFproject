from .patient import extract_patient
from .hospital import extract_hospital
from .bills import extract_bills
from .opd import extract_opd
from .documents import extract_documents
from .insurance import extract_insurance


def parse_document(text):
    return {
        "patient": extract_patient(text),
        "hospital": extract_hospital(text),
        "insurance": extract_insurance(text),
        "bills": extract_bills(text),
        "opd_visits": extract_opd(text),
        "documents": extract_documents(text),
    }