# 2. y = x + 1
# Write a function f(x) that returns x + 1 and plot it for x values of -3 to 3 in increments of 1. 

import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3,4))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.axis([-3, 3, -2, 4])
plot.show()
