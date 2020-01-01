# 5-2
car = "Audi"
if car == "Audi":
    print("Car is Audi")
print("name of car in lower case: " + car.lower())

number = 2012
if number <= 2000:
    print("\nNumber is less than 2000")
elif number > 2001 and number <= 3000:
    print("\nNumber is between 2001 to 3000")
elif number == 0 or number == 1:
    print(f"\nNumber is {number}")
else:
    print(f"\nDefault.")

items = ["one", "two"]
if "one" in items:
    print("One is present in the list")

print("twenty" in items)