# String are immutable
a="Shreyas"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
a="Shreyas!!!!"
print(a)
print(a.rstrip("!"))
# to remove ("!") from name
# if you want to replace any thing you an use .replace
print(a.replace("Shreyas","Madhura"))
print(a.rstrip("!"))
# If you want to split some thing from the string you can make use of 
# .split(" ") and put som espace in the string to make changes for example
# shre yas
name = "shre yas"
print(name.split(" "))
blogHeading="introduce your name to the pannel.and what are your hobbies"
print(blogHeading.capitalize())