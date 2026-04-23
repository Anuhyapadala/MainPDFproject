from api.document_parser.patient import extract_patient
from api.document_parser.insurance import extract_insurance
from api.document_parser.hospital import extract_hospital
from api.document_parser.bills import extract_bills
from api.document_parser.opd import extract_opd
from api.document_parser.documents import extract_documents
from api.utils.report_builder import *
from api.utils.ocr_parser import parse_ocr_text


def build_final_output(text):
    data = parse_ocr_text(text)
    return {
        "patient_table": build_patient_table(data),
        "hospital_table": build_hospital_table(data),
        "insurance_table": build_insurance_table(data),
        "bills_table": build_bills_table(data),
        "opd_table": build_opd_table(data),
        "baby_table": build_baby_table(data),
    }