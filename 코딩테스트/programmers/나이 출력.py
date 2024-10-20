from datetime import datetime
def solution(age):
    return datetime.now().year - age-1

print(solution(40))