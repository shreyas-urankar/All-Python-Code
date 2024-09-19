#Write a Python function that takes two arguments: a first name and a last name. The function should:
#Capitalize the first letter of each name (i.e., title case).
#Return the formatted full name.


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name("shreyas", "urankar"))
