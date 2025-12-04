def digit_value(ch: str):

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M":1000
    }

    return values.get(ch)

def largest_symbol(s: str) -> str:

    largest = s[0]
    largest_value = digit_value(s[0])

    for i in range(1, len(s)):
        ch = s[i]
        value = digit_value(ch)
        if value > largest_value:
            largest = ch 
            largest_value = value
        
        
        return largest 

print(largest_symbol("XVI"))      # X
print(largest_symbol("MC"))       # M
print(largest_symbol("VII"))      # V
print(largest_symbol("CDXL"))     # D

