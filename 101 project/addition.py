

class Add:

    @staticmethod
    def addition(*args):
        out = 0
        for i in args:
            out += i
        ttl = f'Total sum is :{out}'
        return ttl