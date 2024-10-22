import math


def solution(n):
    print(math.floor(n / 7))
    print(n / 7)
    return math.ceil(n / 7)

print(solution(15))