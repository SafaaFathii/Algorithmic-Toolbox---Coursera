# Uses python3


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    first = 0
    second = 1
    for i in range (1 , n):
        temp = (first + second) % 10
        first = second
        second = temp
    return second


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))