def solution(n, k):
    return (n * 12000 + k * 2000) - (int(n * 0.1) * 2000)

# print(solution(10,3))
print(solution(64,6))