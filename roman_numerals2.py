def valid_chars(s: str) -> bool:
    valid = ["I", "V", "X", "L", "C", "D", "M"]
    
    for ch in s:
        if ch not in valid:
            print("invalid input")
            return False
        
    return True

print(valid_chars("VMD"))