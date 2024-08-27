# Tip calculator from Day 2 of 100 Days of Code (Udemy.com)

print("Welcome to my tip calculator.")
total = float((input("What was the total bill? ")))
tip = int(input("What tip percentage would you like to leave? (10, 12 or 15) "))
numPeople = int(input("How many people will be splitting the bill? "))

totalWithTip = total + (total * (tip / 100))
splitAmt = "{:,.2f}".format(totalWithTip / numPeople)

print(f"Each person should pay: ${splitAmt}.")
