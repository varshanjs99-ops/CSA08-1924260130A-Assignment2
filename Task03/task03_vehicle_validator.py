# Q3 – Vehicle Registration Number Validator
# Valid pattern: 2 state letters + 2 district digits + 1/2 series letters + 4 digits.

def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if len(reg) == 9:
        return reg[4:5].isalpha() and reg[5:9].isdigit()
    return reg[4:6].isalpha() and reg[6:10].isdigit()

def format_number(reg):
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration number")
    series_end = 5 if len(reg) == 9 else 6
    return f"{reg[:2]} {reg[2:4]} {reg[4:series_end]} {reg[series_end:]}"

if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234",
               "TN 22 1234 AB", "MH 12 Q 9876", "DL 8C AB 1234"]
    for raw in samples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        receipt = format_number(reg) if is_valid(reg) else "-"
        print(f"{raw:18} -> {reg:12} {status:7} receipt: {receipt}")
    print("\\nString notes:")
    print("Strings are immutable: methods create a new string rather than changing the original.")
    text = "hello"
    print("text.upper() returns", text.upper(), "while text remains", text)
    nine = "TN09AB123"
    ten = "TN09AB1234"
    print("9-character s[-4:]", nine[-4:], "| s[4:-4]", nine[4:-4])
    print("10-character s[-4:]", ten[-4:], "| s[4:-4]", ten[4:-4])
