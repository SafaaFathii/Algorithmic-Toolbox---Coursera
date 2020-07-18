# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(b, a*b + 1, b):
        if l % a == 0:
            return l

if __name__ == '__main__':
   # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

