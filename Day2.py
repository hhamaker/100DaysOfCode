'''
#Datatypes
#String
print("Hello"[4])
#Integer
print(123 + 345)
#Float
3.1415
#Boolean
True
False

#Exercise 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
char1 = two_digit_number[0]
char2 = two_digit_number[1]

print(int(char1) + int(char2))

#Exercise 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / (float(height) * float(height))
print(str(int(bmi)))

#Exercise 3
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsLeft = 90 - int(age)
daysLeft = 365*yearsLeft
weeksLeft = 52*yearsLeft
monthsLeft = 12*yearsLeft
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
'''
#Tip Calculator
print("welcome to the tip Calculator. ")
totalBill = input("What was the total bill? ")
tipRate = input("What percentage tip would you like to give? 10, 12, or 15? ")
numPeople = input("How many people to split the bill? ")

share = float(totalBill) / int(numPeople) * float(1 + (int(tipRate)/100))
share = "{:.2f}".format(share)
print("Each person should pay: $" + str(share))

