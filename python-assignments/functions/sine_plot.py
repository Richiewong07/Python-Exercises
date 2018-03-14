# 5. Sine
# Write a function f(x) that returns the sin of x. Hint: there is a sin function in the math module. Plot it from -5 to 5 in increments of 1.


import matplotlib.pyplot as plot
import math as math

def f(x):
    return math.sin(x)

xs = list(range(-5 ,5, 1))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.axis([-6, 6, -1 ,1])
plot.show()
