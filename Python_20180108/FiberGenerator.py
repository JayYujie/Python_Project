class FibGener:

    def __init__(self):
        pass

    def fib(self,max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'done'
