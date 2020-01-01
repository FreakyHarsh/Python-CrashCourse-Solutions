# 6-1
person = {
    'first_name': 'Nayan',
    'last_name': 'gadhari',
    'age': 21,
    'city': 'Thane'
}

for i in person:
    print(f"{i} => {person[i]}")

# 6-2
fav_number = {
    "Yusuf": 33,
    "Nayan": 23,
    "Fahim": 45,
    "Sufiya": 7,
    "Pratik": 77
}

for i in fav_number:
    print(f"{i} favourite number is {fav_number[i]}")


# 6-3
print("\n------------------------------------------------")

jargons = {
    'Type-casting': 'Changing one data type into another',
    'Translated': 'Conversion of user code into machine code',
    'compiled': 'Code translated before run-time',
    'Interpreted': 'Code translated on the fly, during execution',
    'Static': 'Types checked before run-time',
    'Dynamic': 'Types checked on the fly, druing execution',
    'instance-attribute': 'Variables that are unique to objects i.e defined inside a constructor',
    'class-attribute': 'Variables that are common to all objects and belong to a class'
}

for term in jargons:
    print(f"{term}:\n\t{jargons[term]}")
