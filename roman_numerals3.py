def digit_value(ch: str):

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M":1000
    }

    return values.get(ch)

print(digit_value("V"))
print(digit_value("R"))
print(digit_value("X"))