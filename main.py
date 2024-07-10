import math
import pprint
from typing import Tuple

print("Helllo world")

def foo(x: int) -> Tuple[int, float]:
    return x, math.pi+1

pprint.pprint("Hello")

print(foo(4))
print(foo(5))
#wtf