# 1. 정수를 입력 받아서 2제곱의 결과를 돌려주는 함수를 만들고 호출한 값을 출력하세요.

# 함수 만들기
def squared(n):
    result = n * n
    return result

# 함수 사용하기
# number = int(input("정수를 입력하세요:"))
# result = squared(number)
# print("%d의 제곱은 %d이다." % (number, result))

# 2. 4개의 값을 받아서 평균을 돌려주는 함수를 만들고 호출한 값을 출력하세요.
def get_average(s1, s2, s3, s4):
    average = (s1 + s2 + s3 + s4) / 4
    return average

# 확장성 있게
def get_average_many(*scores):
    sum = 0
    for score in scores:
        sum += score
    return sum / len(scores)

s1, s2, s3, s4 = input("4개의 점수를 입력하세요:").split()
s1 = int(s1)
s2 = int(s2)
s3 = int(s3)
s4 = int(s4)
result = get_average_many(s1, s2, s3, s4, 20, 50, 60, 60)
print("평균 : ", result)

