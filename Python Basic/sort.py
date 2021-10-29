#sort() method= used with lists
#sorted) function= used with iterables

#students=["Minh","Huy","Quang"]
#students.sort(reverse=True)
#students.sort()
#for i in students:
#    print(i)

#students=("Minh","Huy","Quang")
#sorted_student= sorted(students)
#for i in sorted_student:
#    print(i)

students=[("Minh","A",18),
        ("Quang","F",21),
        ("Huy","B",30)]

grade= lambda grades: grades[1]
students.sort(key=grade,reverse=True)
sorted_students=sorted(students,key=grade)
for i in students:
    print(i)


