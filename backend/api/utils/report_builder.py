def build_patient_table(data):
    p = data.get("patient", {})
    return [
        ["Full Name", p.get("name")],
        ["Age / Gender", f'{p.get("age","")} / {p.get("gender","")}'],
        ["DOB", p.get("dob")],
        ["Mobile", p.get("mobile")],
        ["UHID", p.get("uhid")]
    ]


def build_hospital_table(data):
    h = data.get("hospital", {})
    return [
        ["Hospital Name", h.get("name")],
        ["Address", h.get("address")],
        ["CIN", h.get("cin")],
        ["Phone", h.get("phone")],
    ]


def build_insurance_table(data):
    i = data.get("insurance", {})
    return [
        ["Policy Number", i.get("policy_number")],
        ["Company / TPA", i.get("company")],
        ["Claim Reference", i.get("claim_ref")],
    ]


def build_bills_table(data):
    bills = data.get("bills", [])
    table = [["Vendor", "Date", "Items", "Amount"]]

    for b in bills:
        table.append([
            b.get("vendor"),
            b.get("date"),
            b.get("items"),
            b.get("amount")
        ])

    return table


def build_opd_table(data):
    opds = data.get("opd_visits", [])
    table = [["Date", "OPD No", "Doctor", "Notes", "Fee"]]

    for o in opds:
        table.append([
            o.get("date"),
            o.get("opd_no"),
            o.get("doctor"),
            o.get("notes"),
            o.get("fee")
        ])

    return table


def build_baby_table(data):
    baby = data.get("baby", {})
    return [
        ["Name", baby.get("name")],
        ["DOB", baby.get("dob")],
        ["Gender", baby.get("gender")],
        ["Weight", baby.get("weight")],
        ["APGAR", baby.get("apgar")]
    ]

