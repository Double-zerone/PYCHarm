# This is a sample Python script.
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1.num2 = num2, num1 + num2
        current += 1
        yield num
    return "done"


g = fib(5)
type(g)