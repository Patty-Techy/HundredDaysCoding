print("Welcome to Tricia's Coding Platform.")
print ("Let's' analyze for you what year is a leap year.")
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year")
        else:
            print("Not a leap year.")
    else:
        print("The year is a leap year.")
else:
    print("This is not a leap year.")

   