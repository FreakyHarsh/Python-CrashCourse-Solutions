# 8-12
def items(*args):
    print("The sandwich will contain the following items:\n")
    for i in args:
        print(i)


items("🍌", "🍅", "🥒", "🔥")


# 8-13
def build_profile(first, last, **myself):
    myself["first_name"] = first
    myself["last_name"] = last
    return myself


person = build_profile("harsh", "boricha", location="thane", zip="400606", age=21)

print(person)

#8-14
def make_car(model, manufacturer, **car_info):
    car_info['model'] = model
    car_info['manufacturer'] = manufacturer
    print(car_info)

make_car('xls', 'jaguar', color = 'red', type = 'xuv')