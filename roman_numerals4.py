def digit_value(ch: str):

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M":1000
    }

    return values.get(ch)

def simplified_roman_to_int(s: str) -> int:
    
    total = 0 
    
    for ch in s:
        value = digit_value(ch)
        
        if value is None:
            return None
    
        total += value

    return total

print(simplified_roman_to_int("VMDI"))

