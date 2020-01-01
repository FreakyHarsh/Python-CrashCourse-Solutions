# 5-8
username = ["admin", "Jenny", "Bob", "Usuf", "Nayan"]
login = input("Enter the username: ")

for person in username:
    if login == person and login == "admin":
        print("Hello Admin, would you like to see a status report?")
    elif login == person and login != "admin":
        print(f"Hello {login}, Thank you for logging in again")

# 5-9
username = []
if username:
    print("There are people using this app")
else:
    print("Nobody use this app")


# 5-10
current_users = ["FreakyHarsh", "harsh@123",
                 "dragonfist", "red_nitro", "morfes_"]
lower_current_users = [i.lower() for i in current_users]
new_users = ["freakyHarsh", "harsh99", "fdragon"]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"{new_user} you will need to enter a new username.")
    else:
        print(f"{new_user} username is available")



# 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
