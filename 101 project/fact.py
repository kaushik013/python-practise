

class Fact:

    @staticmethod
    def factorial(*args):
        lis = []
        for i in args:
            fact = 1
            for j in range(1,i+1):
                fact *= j
            lis.append(fact)
        return lis
