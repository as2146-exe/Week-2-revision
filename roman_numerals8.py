def extract_large(s: str) -> list:

    result = []

    for ch in s:
        if ch in ["M", "D", "C"]:
            result.append(ch)
    
    return result

print(extract_large("MDCLVI"))