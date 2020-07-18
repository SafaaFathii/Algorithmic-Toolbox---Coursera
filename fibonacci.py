# Uses python3
def calc_fib(n):
    fib = list()
    fib.append(0)
    fib.append(1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n):
            fib.append(fib[i] + fib[i - 1])
        return fib[i + 1]

n = int(input())
print(calc_fib(n))
