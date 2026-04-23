def extract_documents(text):
    docs = []

    pages = text.split("\f")

    for i, page in enumerate(pages):
        docs.append({
            "page": i + 1,
            "preview": page[:150]
        })

    return docs