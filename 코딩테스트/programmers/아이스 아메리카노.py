import math

solution = lambda money: [math.floor(money / 5500), money % 5500]

print(solution(5500))
print(solution(15000))