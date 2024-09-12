import math

def quadPerf(x):
    y = int(math.sqrt(x))
    return y * y == x

def fibonacci(n):
    return quadPerf(5 * n * n + 4) or quadPerf(5 * n * n - 4)


num = int(input("Insira um número: "))
if fibonacci(num):
    print(f"{num} pertence a sequencia de Fibonacci.")
else:
    print(f"{num} não pertence a sequencia de Fibonacci.")
