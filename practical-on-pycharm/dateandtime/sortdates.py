from datetime import *
import time

startTime = time.perf_counter()
ldates = []

d1 = date(2021, 11, 23)
d2 = date(2020, 4, 15)
d3 = date(2022, 5, 15)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

# here execution will pause for 3 seconds
#time.sleep(3)

for d in ldates:
    print(d)

endTime = time.perf_counter()
print("Execution time: ",(endTime-startTime))
