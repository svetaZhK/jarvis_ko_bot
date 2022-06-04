def car_factory():
    return "creta"

def car_model_factory(model):
    return "model:" + model

def car_model_color_factory(model, color):
    return "model:" + model + "; color:" + color

def get_color():
    return "green"

def get_model():
    return "solaris"



def pr(car):
    print(car + " is cool")

pr(car_model_color_factory(get_model(), get_color()))

dish_of_day = "Pizza"

def get_food(number_of_dish):
    if number_of_dish == 0:
        return "borsh"
    if number_of_dish == 1:
        return "salat"
    if number_of_dish == 2:
        return "tea"
    return dish_of_day

print(get_food(3))
print(get_food(8))
print(get_food(1))
print(get_food(100))
print(get_food(0))

dish_of_day = "Pasta"

print(get_food(3))
print(get_food(8))
print(get_food(1))
print(get_food(100))
print(get_food(0))


# def get_ticket(money):
#     if money > 100:
#         return "Italy"
#     else:
#         return "Sochi"

# a = get_ticket(150)
# b = get_ticket(10)
# c = get_ticket(250)

# def get_TV_chanel(number_chanel):
#     if number_chanel == 1:
#         return "ТВ Россия"
#     if number_chanel == 3:
#         return "НТВ"

# print (get_TV_chanel(2))










