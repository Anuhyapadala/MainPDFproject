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