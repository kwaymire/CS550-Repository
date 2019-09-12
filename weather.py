import sys
import math

v = float(sys.argv[1])
t = float(sys.argv[2])

w = float(35.74 + (0.6215 * t) + (0.4275 - 35.75) * v**0.16)
print(w)