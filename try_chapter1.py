res1 = 3 / 4
print(res1)

res2 = res1 * 2
print(res2)

res3 = res2 ** 3
print(res3)

import math 

print(math.pi)
print(math.sqrt(4))
print(math.sin(math.pi / 2))
print(math.exp(math.log(10)))
print(math.exp(3 / 4))
print(1/math.inf)
print(math.inf * 2)
print(math.inf/math.inf)
print(2 + 5j)
print(complex(2,5))
print(3e0*3.65e2*2.4e1*3.6e3) # 3*10^0*3.65*10^2*2.4*10^1*3.6*10^3

from math import sin, pi
print(sin(pi/2)) 

print(type(1234))
print(type(3.14))
print(type(2+5j))
print(type('hello'))
print(type(True))

print(5 == 4)
print(2 < 3)
print((1 and not 1) or (1 and 1))
print((1 and not 0) or (1 and 0))
print((0 and not 0) or (0 and 0))
print((0 and not 1) or (0 and 1))
print((1 and not 1) or (0 and 0))

print(1+3 > 2+5)
print((3>2) + (5>4)) # warning!

print((14*24*60*60) > 100000)