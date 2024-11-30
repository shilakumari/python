from datetime import *

d = date(2024,10,10)
t = time(12, 45)

dt = datetime.combine(d,t)
print(dt)