# 7-4
pizza_toppings = []
x = ''
input("Enter the toppings you want: Press 'quit' to exit\n")
while x != 'quit':
    x = input()
    pizza_toppings.append(x)

print("You selected the following toppings: \n")
print(pizza_toppings)

# 7-5
print("Press 0 to exit")
age = int(input("Enter the age: "))
while(age):
    if age < 3:
        print("Ticket is free")
    elif age >= 3 and age < 12:
        print("Ticket is $10")
    elif age >= 12:
        print("Ticket is $15")
    age = int(input("Enter the age: "))

# skipping while loops , diy
