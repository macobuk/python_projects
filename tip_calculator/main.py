bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? \n$"))
tip = float(input("How much percent would you like to tip?\n"))
people = int(input("How many people to split the bill with?\n"))
result = round((bill * ((tip / 100) + 1)) / people)
message = "{:.2f}".format(result)
print(f"Each person should pay: ${message}")