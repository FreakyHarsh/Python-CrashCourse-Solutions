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


# 6-8
Dog = {
    "color": "black",
    "owner": "harsh",
    "name": "Roney",
}
Cat = {
    "color": "blue",
    "owner": "Nobita",
    "name": "Doraemon",
}
Parrot = {"color": "Green", "owner": "Shizuka", "name": "kiyo"}

Pets = [Dog, Cat, Parrot]

for info in Pets:
    print(f"Pet Name: {info.get('name')}")
    print(f"Pet Color: {info.get('color')}")
    print(f"Pet Owner: {info.get('owner')}")
    print("--------------------")

# 6-9
favourite_places = {
    "bob": "upvan",
    "rob": "hawaii",
    "dan": "sydney",
}

for person, fplace in favourite_places.items():
    print(f"{person} => {fplace}")

# 6-10
fav_numbers = {
    "Yusuf": [22, 34],
    "Nayan": [2, 6, 23, 7],
    "Fahim": [23, 557, 3, 11],
    "Sufiya": [22, 3, 4],
    "Pratik": [21, 56, 6],
}

for name, fav_no in fav_numbers.items():
    print(f"Favourite numbers of {name}:")
    for i in fav_no:
        print(i)

# 6-11
cities = {
    'mumbai': {
        'country': 'india',
        'population': '22Million',
        'fact': 'Dream city of india, Bollywood is present here',
    },
    'Texas': {
        'country': 'USA',
        'population': '2205020',
        'fact': 'Sheriff\'s area of usa',
    },
    'california': {
        'country': 'USA',
        'population': '2Million',
        'fact': 'Silicon valley is located here',
    },
}

for city_name, j in cities.items():
    print("-----------------------")
    print(f"City name => {city_name}")
    for k, v in j.items():
        print(f"{k}: {v}")

# 6-12 diy
