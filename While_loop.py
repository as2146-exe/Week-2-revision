total = 0

while True:
    q_user = int(input("Enter a number: "))
    if q_user < 0:
        while q_user < 0:
            print("No negatives allowed! ")
            q_user = int(input("Enter a new number: "))
    elif q_user == 0:
        print("End of list.")
        break
    else:
        total += q_user

print(total)