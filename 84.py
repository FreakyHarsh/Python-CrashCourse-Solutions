# 5-3
alien_color = input("Enter the color of alien: ")

if alien_color.lower() == "green":
    print("The Player just earned 5 points")


# 5-4
alien_color = input("Enter the color of alien: ")

if alien_color.lower() == "green":
    print("Player earned 5 points")
else:
    print("Player earned 10 points")


# 5-5
alien_color = input("Enter the color of alien: ")

if alien_color.lower() == "green":
    print("Player earned 5 points")
elif alien_color.lower() == "yellow":
    print("Player earned 10 points")
elif alien_color.lower() == "red":
    print("Player earned 15 points")


# 5-6
age = int(input("Enter your age: "))

if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")


# 5-7
favourite_fruits = ["Mango", "lichi", "banana"]
if "Mango" in favourite_fruits:
    print("Your favourite fruit is Mango")
if "Apple" in favourite_fruits:
    print("Your favourite fruit is Apple")
if "banana" in favourite_fruits:
    print("Your favourite fruit is banana")
if "lichi" in favourite_fruits:
    print("Your favourite fruit is lichi")
if "Pineapple" in favourite_fruits:
    print("Your favourite fruit is Pineapple")
