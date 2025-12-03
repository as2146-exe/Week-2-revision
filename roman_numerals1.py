def count_I(s: str) -> int:
    count_I = 0

    for ch in s:
        if ch == "I":
            count_I += 1
    
    return count_I

print(count_I("MCFVIII"))






