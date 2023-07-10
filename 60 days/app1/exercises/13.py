# def get_age(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
#     return age

# def get_nr_items(list_arg):
#     list_arg = list_arg.split(",")
#     nr_items = len(list_arg)
#     return nr_items

# def area_of_square(side):
#     area = side ** 2
#     return area

# def declare_temp(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"
    
# def check_8_characters(password):
#     if len(password) >= 8:
#         return True
#     else:
#         return False
    
def calculate_time(height, g=9.81):
    time = (2 * height / g) ** 0.5
    return time

time = calculate_time(100)
print(time)