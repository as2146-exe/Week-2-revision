def first_invalid_char(s: str) -> bool:

    values = ["I", "V", "X", "L", "C", "D", "M"]

    for ch in s:
        if ch not in values:
            return ch
        

    return None

print(first_invalid_char("DCVIXIKCDI"))