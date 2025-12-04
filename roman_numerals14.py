def repeat_count_list(s: str) -> list:

    runs = []

    current_run = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1

    runs.append(current_run)

    return runs

print(repeat_count_list("VVVIIIDDD"))
