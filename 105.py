def separation():
    print("--------------------------------------------------")


# 6-4
separation()
jargons = {
    'Type-casting': 'Changing one data type into another',
    'Translated': 'Conversion of user code into machine code',
    'compiled': 'Code translated before run-time',
    'Interpreted': 'Code translated on the fly, during execution',
    'Static': 'Types checked before run-time',
    'Dynamic': 'Types checked on the fly, druing execution',
    'instance-attribute': 'Variables that are unique to objects i.e defined inside a constructor',
    'class-attribute': 'Variables that are common to all objects and belong to a class',
}

for word, meaning in jargons.items():
    print(f"{word.title()}:\n\t{meaning.title()}")

# 6-5
separation()
rivers = {
    'nile': 'egypt',
    'Ganga': 'India',
    'milestone': 'usa',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.upper()}")

print("\nThe following rivers are mentioned:")

for river_name in rivers.keys():
    print(river_name)

print("\nThe following are the countries mentioned:")

for countries in rivers.values():
    print(countries)

# 6-6
separation()
favourite_languages = {
    'harsh': 'python',
    'fahim': 'JavaScript',
    'pratik': 'python',
    'jen': 'c',
    'sarah': 'ruby',
}

should_take_poll = ['fahim', 'nayan', 'sufiya', 'jen', 'pratik']

for i in should_take_poll:
    if i in favourite_languages.keys():
        print(f"{i}, Thank you for responding to our poll")
    else:
        print(f"{i}, You should take the poll")