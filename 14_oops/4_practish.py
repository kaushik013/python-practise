
class Bank:

    branch = 'Veraval'
    Address = 'Ahmedabad'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print(self.branch)
        print(self.name)
        print(self.age)

    @staticmethod    # ⁡⁢⁣⁣decorato⁡⁢⁣⁣r⁡
    def greet():
        print('hello how are you!')


us = Bank('kaushik',33)
us.details()
us.greet()


