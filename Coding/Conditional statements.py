print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#IF-ELSE
if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("You can't ride the rollercoaster!")

#NESTED IF
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("Enter your age: "))
  if age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("You can't ride the rollercoaster!")

#IF-ELIF
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("Enter your age: "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("You can't ride the rollercoaster!")

#MULTIPLE IFS
bill=0
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("Enter your age: "))
  if age < 12:
    bill=5
    print("Child tickets are of $5")
  elif age <= 18:
    bill=7
    print("Youth tickets are of $7")
  else:
    bill=12
    print("Adult tickets are of $12")

  photo = input("Do u want a photo taken? Yes or No!")
  if photo=="Yes":
    bill += 3
  print(f"Your final bill is {bill}")
else:
  print("You can't ride the rollercoaster!")