print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip /= 100
total = (bill / people) * (1+tip)
formatted_total = "{:.2f}".format(total)
print(formatted_total)
