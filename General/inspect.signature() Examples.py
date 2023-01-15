import inspect
from dataclasses import dataclass

def foo(a, b, x='blah'):
    pass

@dataclass
class Bar(object):
    var_a: int
    var_b: int
    var_c: str


print(inspect.signature(foo))
# (a, b, x='blah')
print(inspect.signature(Bar).parameters.values())
