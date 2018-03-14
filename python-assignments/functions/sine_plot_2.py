# 6. Sine 2
# Unfortunately, that looked horrible, and we can't use smaller increment values because the range function only supports integers. Fortunately, there is a Python package called numpy that will allow ranges with decimal-point increments. You will install it using the command pip install numpy. Once you've done that, you write the import statement: from numpy import arange, and then you can use arange in place of range to use decimal increments, like so:
#
# xs = arange(-5, 6, 0.1)


import matplotlib.pyplot as plot
import math as math
from numpy import arange

def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.axis([-6, 6, -1 ,1])
plot.show()
