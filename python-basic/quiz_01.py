# 수 이름: check_odd_even
# 인자로 정수 하나를 받습니다.
# 입력된 숫자가 짝수라면 "짝수"를, 홀수라면 "홀수"를 반환합니다.
# 예시:
# print(check_odd_even(4))  # 출력: "짝수"
# print(check_odd_even(7))  # 출력: "홀수"

def check_odd_even(num):
    if num % 2 == 0:
        return "짝수"
    elif num % 2 == 1:
        return "홀수"


print(check_odd_even(4))

def find_max(arr):
    max_num = 0
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num
print(find_max([3,5,9,1]))


def remove_duplicates(arr):
    temp = set(arr)
    result = sorted(list(temp))
    return result

print(remove_duplicates([3, 1, 2, 3, 4, 1]))  # 출력: [1, 2, 3, 4]
print(remove_duplicates([5, 5, 5, 5]))  # 출력: [5]

def capitalize_words(word):
    temp = word.split()
    for i in temp:
        if i.isupper():
            return i

print(capitalize_words("hello world"))  # 출력: "Hello World"
# print(capitalize_words("python is FUN"))  # 출력: "Python Is Fun"
