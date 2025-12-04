def max_repeat(s: str) -> int:
    current_run = 0
    max_run = 0

        
    current_run = 1
    max_run = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_run += 1
        else:
            current_run = 1

        if current_run > max_run:
            max_run = current_run

    return max_run

print(max_repeat("VIII"))
