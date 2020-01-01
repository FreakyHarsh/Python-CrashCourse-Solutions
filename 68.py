food = ("food1", "food2", "food3", "food4", "food5",)
for i in food:
    print(i)

#food[2]= "new food"
# Above line will give error since Tuples are immutable
print("\n The changed menu is: \n")

food = ("food1", "food2", "food3", "newfood4", "newfood5")
for i in food:
    print(i)

