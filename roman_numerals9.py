def count_V(s: str) -> int:

    count = 0

    for ch in s:
        if ch == "V":
            count += 1
    
    return count

print(count_V("VVII"))
