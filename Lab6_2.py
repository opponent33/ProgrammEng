from pprint import pprint

my_dict = {"first": "so easy"}

def dict_maker(**kwargs):
    my_dict.update(kwargs)

dict_maker(a1 = 1, a2 = 20, a3 = 30, a4 = 40)
dict_maker(name = "Mike", age = 31, weight = 70, eye_colour = "blue")
print(my_dict)