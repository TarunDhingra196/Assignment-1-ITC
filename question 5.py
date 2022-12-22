import math
pie = 3.14
i=0
for i in range(0,346,15):
    a=math.sin(math.radians(i))
    b=math.cos(math.radians(i))
    print(i,"---",round(a,4),round(b,4))
