cities = ["paris", "new york", "Los Angeles", "Silicon Valley", "Maldives"]
print(f"The Original list is {cities}")

print(f"\n\nThe Sorted list is {sorted(cities)}")
print(f"\n\nThe Original list is still {cities}")
cities.reverse()
print(f"\n\nThe reverse sorted list is {sorted(cities)}")
print(f"\n\nThe reversed Original list is {cities}")
cities.reverse()
print(f"\n\nAgain changing the order of the list {cities}")
cities.sort()
print(f"\n\nPermanently sorted list is {cities}")
cities.reverse()
print(f"\n\nReversed permanently sorted list is {cities}")

# 3-9 and 3-10 are self expanatory
