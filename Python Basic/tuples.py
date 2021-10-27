#ordered and unchangeable
student =("Minh",21,"male")
print(student.count("Minh"))
print(student.index("male"))

for x in student:
    print(x)

if "Minh" in student:
    print("Minh is here")
