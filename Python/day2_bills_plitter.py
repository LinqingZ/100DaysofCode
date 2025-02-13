# total bill
# fair prices or different dish
# tips percentage
# service fees
# tax fees

# if all the same price, divide by the number of people

print("Welcome to the bill splitter!")

total = input("What was the total bill? $")
person = input("How many people to split the bill? ")
tips = input("What is the percentage of tips? (only the integer in two digits) ")
equal_split = input("Is the bill fairly split? Y/N ")
if equal_split == "Y" or equal_split == "y":
    print(float(total) * (1 + int(tips)/100 ) / int(person))
else:
    each_person_dish = input("")
    bill_per_person = float(total) * (1 + tips/100 ) / int(person)
    # round(bill_per_person, 2)
    print(f"Each person should pay: & {round(bill_per_person, 2)}")