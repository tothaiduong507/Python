name= "Minh Do"
first_name= name[0:4:1]
print(first_name)
last_name=name[5:7:1]
print(last_name)
#a[start:stop:step]
# start is inclusive, stop is exclusive
funky_name= name[0:8:2]
print(funky_name)
reversed_name= name[::-1]
print(reversed_name)

#Slicing
website = "http://google.com"
slice= slice(7,-4)

print(website[slice])

