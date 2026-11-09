# Q2 – Loops that Count Attempts
# Simulated OTP verification: blank entries do not count.
CORRECT_OTP = "482913"

def verify_with_while(entries, correct=CORRECT_OTP, extra_attempts=False):
    limit = 3 + (2 if extra_attempts else 0)
    attempts = 0
    index = 0
    while index < len(entries) and attempts < limit:
        entry = entries[index]
        index += 1
        if entry == "":
            print("Blank entry: ignored")
            continue
        attempts += 1
        if entry == correct:
            print("OTP verified")
            break
        print(f"Wrong OTP ({attempts}/{limit})")
    else:
        if attempts >= limit:
            print("Account locked for 30 minutes")
        else:
            print("No more entries supplied")
    return attempts

def verify_with_for(entries, correct=CORRECT_OTP, extra_attempts=False):
    limit = 3 + (2 if extra_attempts else 0)
    attempts = 0
    for entry in entries:
        if entry == "":
            print("Blank entry: ignored")
            continue
        attempts += 1
        if entry == correct:
            print("OTP verified")
            break
        print(f"Wrong OTP ({attempts}/{limit})")
        if attempts >= limit:
            print("Account locked for 30 minutes")
            break
    else:
        if attempts >= limit:
            print("Account locked for 30 minutes")
        else:
            print("No more entries supplied")
    return attempts

def verify_with_security_question(entries, security_answer, expected_answer,
                                  correct=CORRECT_OTP):
    extra = security_answer.strip().lower() == expected_answer.strip().lower()
    return verify_with_for(entries, correct, extra_attempts=extra)

if __name__ == "__main__":
    print("WHILE LOOP:")
    verify_with_while(["", "111111", "222222", "333333"])
    print("\\nFOR LOOP:")
    verify_with_for(["111111", "", "482913"])
    print("\\nSECURITY QUESTION CORRECT (two extra attempts):")
    verify_with_security_question(
        ["111111", "222222", "333333", "444444", "482913"],
        "blue", "blue"
    )
    # pass is a syntactically valid placeholder; it performs no operation.
    if False:
        pass
