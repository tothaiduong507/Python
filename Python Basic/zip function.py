usernames=["Dude","Bro","Mister"]
passwords=["password","abc123","guest"]

users= dict(zip(usernames,passwords))
print(type(users))
for key,value in users.items():
    print(key+" : "+value)

login_date=["1/1/2021","1/2/2021","1/3/1999"]

users=zip(usernames,passwords,login_date)

for i in users:
    print(i)


