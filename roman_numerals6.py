def build_mapping() -> dict:
    mapping = {}

    mapping["I"] = 1
    mapping["V"] = 5
    mapping["X"] = 10
    mapping["L"] = 50
    mapping["C"] = 100
    mapping["D"] = 500
    mapping["M"] = 1000

    return mapping

def print_mapping(mapping: dict):
    for key, value in mapping.items():
        print(key, value)

roman_dict = build_mapping()
print_mapping(roman_dict)
