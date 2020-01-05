# 9-1
class Restaurant:
    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"Restaurant Name is {self.restaurant_name}")
        print(f"Restaurant Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")


restaurant = Restaurant("BBQ Nation", "BBQ")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2
restaurant1 = Restaurant("First Restaurant", "cuisine 1")
restaurant2 = Restaurant("Second Restaurant", "cuisine 2")
restaurant3 = Restaurant("Third Restaurant", "cuisine 3")
print(restaurant1.restaurant_name)
print(restaurant2.restaurant_name)
print(restaurant3.restaurant_name)

# 9-3
class User:
    def __init__(self):
        self.first_name = input("Enter your name: ")
        self.last_name = input("Enter your last name: ")
        self.username = input("Enter your username: ")

    def describe_user(self):
        print(f"{self.first_name}.{self.last_name} =>{self.username}")

    def greet_user(self):
        print(f"Hello {self.first_name}, Mucho Gusto")


harsh = User()
print(harsh.greet_user())
print(harsh.describe_user())
