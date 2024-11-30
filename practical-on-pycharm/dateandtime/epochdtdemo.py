import time, datetime

epochseconds = time.time()
print(epochseconds)
#converting seconds into date time
t = time.ctime(epochseconds)
print(t)

# using datetime module
#1st datetime is module, 2nd datetime is a class
dt = datetime.datetime.today()
print("Current day: ",dt.day,"Current month: ",dt.month,"Current year: ",dt.year)
print("Current Date: {}/{}/{}".format(dt.day,dt.month,dt.year))

print("Current second: ",dt.second,"Current minute: ",dt.minute,"Current hour: ",dt.hour)
print("Current Time: {}:{}:{}".format(dt.second,dt.minute,dt.hour))
