def seperation():
    print("\n------------------------------------------------")
# 6-7
Nayan = {
    "first_name": "Nayan",
    "last_name": "gadhari",
    "age": 21,
    "city": "Thane",
}
Harsh = {
    "first_name": "Harsh",
    "last_name": "Boricha",
    "age": 21,
    "city": "Thane",
}
Yusuf = {
    "first_name": "Yusuf",
    "last_name": "Khan",
    "city": "Kurla",
    "age": 33,
}

people = [Nayan, Harsh, Yusuf]

for person in people:

    print(
        f"Name:{person.get('first_name', 'Not available')}.{person.get('last_name','Not Available')}"
    )
    print(f"Age:{person.get('age','Not available')}")


#6-8
Dog = {
    'color': 'black',
    'owner': 'harsh',
    'name': 'Roney',
}
Cat = {
    'color': 'blue',
    'owner': 'Nobita'
}