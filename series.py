#Data types (Strings, Integer, float
#Subscripting is a method of pulling a particular character
print("Hello"[4])

#Integer
print(123 + 345)

print(123_456_789)

#float
3.14159

#Boolean
True
False

num_char = len(input("What is your name?"))
# Type Conversion or Type Casting str(Variable we want to convert, then save into a new variable i.e. assign a new value to the conversion)
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters")

#Converting Strings to Integer and vice versa
# print(type(input("What is your name?")))


a = 123
print(type(a))
# To type cast this to a str is as seen below
a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100 ))

two_digit_num = input("type a two digit num:")
print(type(two_digit_num))

first_digit = int(two_digit_num[0])
second_digit = int(two_digit_num[1])

print(first_digit)
print(second_digit)

result = first_digit + second_digit
print(result)

print(3*(3+3)/3-3)

height = input("enter your height in m: ")
weight = input("enter your height in kg: ")


BMI = int(weight)/float(height) ** 2
# print(type(height))
print(int(BMI))

print(round(8/3, 2))
print(round(2.66666666, 2))
# using flow division chops off the float
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

score = 0
#user scores a point
score +=1
print(score)

score = 0
height = 1.8
is_winning = True
print("Your score is " + str(score))

#the use of f-string
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")

#Life in weeks
age = input("What is your current age? ")
Age_left_in_years = 90 - int(age)
print(Age_left_in_years)

Age_left_in_months = 12 * Age_left_in_years
print(Age_left_in_months)

Age_left_in_weeks = 52 * Age_left_in_years
print(Age_left_in_weeks)

Age_left_in_days = 7 *Age_left_in_weeks
print(Age_left_in_days)

print(f"You have {Age_left_in_days} days, {Age_left_in_weeks} weeks, {Age_left_in_months} months, {Age_left_in_years} years")

age = input("What is your current age? ")
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = days_remaining * 52
months_remaining = weeks_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, {years_remaining} years. ")




