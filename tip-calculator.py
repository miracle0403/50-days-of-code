print("Welcome to the tip calculator!")
bill = input("How much is the total bill?")
percent = input("What percent of tip will you like to give?")  
people = input("How many people to split this bill?")

bill_int = int(bill)
percent_int = int(percent)
people_int = int(people)

extra = percent_int / 100 * bill_int

add = int(extra) + bill_int
finalbill = add / people_int
print(f"Each person should pay:  {finalbill}")