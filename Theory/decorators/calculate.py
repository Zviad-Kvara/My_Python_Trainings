import math
from Theory.decorators.decorator import debug

math.factorial = debug(math.factorial)

def approximate(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

