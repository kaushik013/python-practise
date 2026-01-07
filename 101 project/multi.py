
class Multipli:

    @staticmethod
    def mul(*args):
        total = 1
        for i in args:
            total *= i
        ttl = f'Total multiply is : {total}'
        return ttl
