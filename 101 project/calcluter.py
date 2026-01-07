
from addition import Add
from multi import Multipli
from fact import Fact


class Calcluter(Add,Multipli,Fact):
    pass

obj = Calcluter()
print(obj.factorial(4,5))

