def solution(arr):
    arr.sort()
    return arr[len(arr) // 2]

print(solution([1,2,7,10,11]))
print(solution([9, -1, 0]))
