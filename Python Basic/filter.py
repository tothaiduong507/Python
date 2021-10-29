friends=[("Minh",19),
         ("Huy",18),
         ("Quang",21),
         ("Viet",23),
         ("Duong",26),
         ("Hieu",16),
         ("Quoc",14),]

age= lambda data: data[1]>=18

drink_buddies=list(filter(age,friends))
for i in drink_buddies:
    print(i)