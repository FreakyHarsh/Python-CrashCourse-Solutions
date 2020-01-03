# 7-1
question = input("What kindoff rental car do you want? ")
print(f"Let me see if I can find you a {question}")

# 7-2
no = int(input("How many people are in your dinner group? "))
if no > 8:
    print("You will have to wait.")
else:
    print("Table is ready")

# 7-3
n = int(input("Enter the number to generate it's table: "))
for i in range(1, 11):
    print(f"{n}*{i} => {n*i}")
