print("Welcome to the tip calculator!")

bill=float(input("What was the total bill?\n$")) 

tip=int(input("How much tip would you like to give? 10, 12 or 15?\n"))

split=int(input("How many people split the bill?\n"))
#pay= bill * (1 + tip / 100)
pay=tip/100
total=bill * pay
total_bill= bill + total
per= total_bill / split
final = round(per, 2)
final = "{:.2f}".format(per)

print(f"Each person should pay {final} dollars")