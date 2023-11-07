# Importing in Python is the process of loading code from a Python module into the current script.
import math
result = math.sqrt(9)
print(result)  # Output: 3.0

# from keyword
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0

from math import sqrt, pi
result = sqrt(9) * pi
print(result)  # Output: 9.42477796076938

# importing everything
from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793

# "as" keyword
import math as m
print(m.sqrt(9))  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

import math as m
result = math.sqrt(9) * m.pi
print(result)  # Output: 9.42477796076938

# dir function
import math
print(dir(math))

print(math.nan, type(math.nan))

# importing module made by us

from deepak import welcome, deepak
welcome()
print(deepak)


from deepak import *
welcome()
print(deepak)


import deepak as hr
hr.welcome()
print(hr.deepak)

