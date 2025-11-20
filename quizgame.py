q_list = [
    {"text": "Two plus two equals seven", "answer": "F"},
    {"text": "A carrot is orange", "answer": "T"},
    {"text": "The sky is green", "answer": "F"}
    ]

for question in q_list:
    print(question["text"])
    guess = input("T, or F? ").lower()
    continue 
    while guess not in ["T", "F"]:
    guess = input("Please only choose T or F: ").upper()


question["guess"] = guess





