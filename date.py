import sys
import math

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])


y0 = int(y - math.floor(14-m)/12)
x = int(y0 + y0/4 - y0/100 + y0/400)
m0 = int(m + 12 * math.floor((14-m)/2) - 2)
d0 = int((d + x + (31*0)/12) % 7)

print(d0)
