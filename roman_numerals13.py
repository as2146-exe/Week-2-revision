def digit_value(ch: str):

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M":1000
    }

    return values.get(ch)

def sum_first_three(s: str) -> int:

    total = digit_value(s[0]) + digit_value(s[1]) + digit_value(s[2])

    return total
    
print(sum_first_three("VIDLC"))