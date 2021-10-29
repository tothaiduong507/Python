import time
print(time.ctime(10000))

print(time.time())

print(time.ctime(time.time()))

time_object= time.localtime()
print(time_object)

local_time=time.strftime("%B %d %Y %H :%M:%S",time_object)
print(local_time)
time_string="20 April,2021"
time1=time.strptime(time_string,"%d %B,%Y")
print(time1)
time_tuple=(2021,4,20,4,20,0,0,0,0)
time_string1=time.asctime(time_tuple)
print(time_string1)