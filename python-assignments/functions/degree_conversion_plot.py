# 7. Degree Conversion
# Write a function that takes a temperature in Celcius and converts it Fahrenheit. Plot it on a graph.

import matplotlib.pyplot as plot

def f(x):
    return x * 1.8 + 32

xs = list(range(0, 38))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.axis([0, 37.8, 30, 100])
plot.show()
