def next_nonblank(responses, position):
    while position < len(responses):
        answer = responses[position]
        position += 1
        if answer == "":
            continue
        return answer, position
    return None, position


def verify_with_while(responses, correct_otp, security_correct=False):
    allowed_attempts = 5 if security_correct else 3
    attempts = 0
    position = 0

    while attempts < allowed_attempts:
        answer, position = next_nonblank(responses, position)
        if answer is None:
            break
        attempts += 1
        if answer == correct_otp:
            print(f"while: verified after {attempts} attempts")
            break
        if answer == "000000":
            pass
    else:
        print(f"while: locked after {attempts} attempts")
        return

    if answer is None:
        print(f"while: stopped after {attempts} attempts")


def verify_with_for(responses, correct_otp, security_correct=False):
    allowed_attempts = 5 if security_correct else 3
    position = 0

    for attempt in range(allowed_attempts):
        answer, position = next_nonblank(responses, position)
        if answer is None:
            break
        if answer == correct_otp:
            print(f"for: verified after {attempt + 1} attempts")
            break
    else:
        print(f"for: locked after {allowed_attempts} attempts")
        return

    if answer is None:
        print(f"for: stopped after {position} responses")


verify_with_while(["", "111111", "222222", "654321"], "654321")
verify_with_for(["", "111111", "222222", "333333"], "654321")
verify_with_while(["111111", "222222", "333333", "444444", "654321"], "654321", True)
verify_with_for(["111111", "222222", "333333", "444444", "654321"], "654321", True)
