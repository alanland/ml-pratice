# coding: utf-8
from StringIO import StringIO

import numpy as np

###
#  Splitting the lines into columns
###

# The delimiter argument
data = "1, 2, 3\n4, 5, 6"
np.genfromtxt(StringIO(data), delimiter=",")

# fixed with, every 3 char is a number
data = "  1  2  3\n  4  5 67\n890123  4"
np.genfromtxt(StringIO(data), delimiter=3)

data = "123456789\n   4  7 9\n   4567 9"
np.genfromtxt(StringIO(data), delimiter=(4, 3, 2))
