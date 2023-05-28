print ("Welcome to Tricia's Love Calculator.")
boo_name = input("What's your guy's name? ")
babe_name = input("What's your babe's name?  ")
combined_string = boo_name + babe_name
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

#create a love score variable
love_score = int(str(true) + str(love))

print (love_score)

if love_score < 10 or love_score >  90:
    print(f"Your score is {love_score}, you go together like coke and mentos")

elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are compatible together.")
else:
    print(f"Your Score is {love_score}.")