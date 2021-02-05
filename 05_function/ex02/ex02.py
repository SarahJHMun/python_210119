# 함수 만들기
# input -> 구현 -> output

# 1. 무슨 함수를 만들지 생각한다. 함수명 (snake case)
# 2. input으로 무엇을 받을 것인지 생각한다.
# 3. output으로 무엇을 돌려줄 것인지 생각한다.
# 4. 구현한다.

# 2개의 정수를 입력 받아서 합계를 계산해주는 함수
def sum_values(x, y):   # 매개변수, parameter
    print("함수에 들어왔다.")
    return x + y

def sum_many_values(*values):
    sum = 0
    for value in values:
        sum += value
    return sum

def minus(x, y):
    print("%d에서 %d뺀 결과값은 %d입니다." % (x, y, x - y))


# 사용하기
a, b = input("두 개의 숫자를 입력하세요:").split()
a = int(a)
b = int(b)
result = sum_values(a, b)
print(result)
print(sum_many_values(a, b, 500, 200, 300))

minus(a, b)
