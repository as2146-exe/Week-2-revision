def return_only_small(s: str) -> bool:
    for ch in s:
        if ch not in ["I", "V", "X"]:
            return False
        else:
            return True
    
print(return_only_small("VII"))
print(return_only_small("CDXII"))