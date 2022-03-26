'''
#exercise0
print("Welcome to the roller coaster.")
height = input("how tall are you in centimeters?")

if int(height) > 120:
    print("you can ride the roller coaster.")
else:
    print("you can not ride the roller coaster.")

#exercise1
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (number % 2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#exercise2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(float(weight) / (float(height) * float(height)))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35 :
    print(f"Your BMI is {bmi}, you are clinically obese.")

#exercise3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leapBool = False
if (year % 4) == 0:
    leapBool = True
    if (year % 100 == 0):
        leapBool = False
        if (year % 400 == 0):
            leapBool = True

if leapBool:
    print("Leap year.")
else:
    print("Not leap year.")

#exercise 4
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

price = 0
#Write your code below this line 👇
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25

if add_pepperoni == "Y":
    price += 2
    if size == "M" or size == "L":
        price += 1
if extra_cheese == "Y":
    price += 1    

print(f"Your final bill is: ${price}.")

#exercise5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

trueNum = 0
loveNum = 0

for ch in name1:
    if ch.upper() == "T":
        trueNum += 1
    elif ch.upper() == "R":
        trueNum += 1
    elif ch.upper() == "U":
        trueNum += 1
    elif ch.upper() == "E":
        trueNum += 1
for ch in name1:
    if ch.upper() == "L":
        loveNum += 1
    elif ch.upper() == "O":
        loveNum += 1
    elif ch.upper() == "V":
        loveNum += 1
    elif ch.upper() == "E":
        loveNum += 1

for ch in name2:
    if ch.upper() == "T":
        trueNum += 1
    elif ch.upper() == "R":
        trueNum += 1
    elif ch.upper() == "U":
        trueNum += 1
    elif ch.upper() == "E":
        trueNum += 1
for ch in name2:
    if ch.upper() == "L":
        loveNum += 1
    elif ch.upper() == "O":
        loveNum += 1
    elif ch.upper() == "V":
        loveNum += 1
    elif ch.upper() == "E":
        loveNum += 1

combinedNum = int(str(trueNum) + str(loveNum))

if combinedNum < 10 or combinedNum > 90:
    print(f"Your score is {combinedNum}, you go together like coke and mentos.")
elif combinedNum > 40 and combinedNum < 50:
    print(f"Your score is {combinedNum}, you are alright together.")
else:
    print(f"Your score is {combinedNum}.")
'''

#Treasure Island
print("Welcome to treasure Island. Your mission is to find the treasure")
direction = input("There are two paths... Would you like to go left of right?").lower

if direction == "left":
    action = input("you come across a river, do you want to swim, or wait?").lower
    if action == "wait":
        door = input("a house magically appears with 3 doors. Red, Blue, and Yellow. which door would you like to enter?").lower
        if door == "Red":
            print("Burned by fire. Game over")
        elif door == "Blue":
            print("Eaten by beasts. Game over")
        elif door == "Yellow":
            print("You Win!")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")