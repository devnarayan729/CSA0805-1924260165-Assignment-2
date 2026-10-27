def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    return (
        reg[:2].isalpha()
        and reg[2:4].isdigit()
        and reg[4:-4].isalpha()
        and len(reg[4:-4]) in (1, 2)
        and reg[-4:].isdigit()
    )


def format_registration(reg):
    if not is_valid(reg):
        raise ValueError("Registration number is not valid")
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"


examples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "mh 12 xy 9876",
    "DL-05-AB-4321",
]

for raw in examples:
    registration = normalise(raw)
    result = "valid" if is_valid(registration) else "INVALID"
    print(f"{raw:15} -> {registration:11} {result}")
    if is_valid(registration):
        print(" " * 18 + format_registration(registration))

sample_nine = "TN09A1234"
sample_ten = "TN09AB1234"
print("9-character series:", sample_nine[4:-4])
print("10-character series:", sample_ten[4:-4])
