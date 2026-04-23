import re

def extract_entities(text):
    data = {}

    # name
    match = re.search(r"(LAXMI|SHARMA|YUVAJ).*", text, re.I)
    if match:
        data["name"] = match.group()

    # gender
    if "FEMALE" in text.upper():
        data["gender"] = "Female"
    elif "MALE" in text.upper():
        data["gender"] = "Male"

    # amount
    nums = re.findall(r"\d{2,6}", text)
    nums = [int(n) for n in nums if int(n) > 100]
    if nums:
        data["amount"] = max(nums)

    return data