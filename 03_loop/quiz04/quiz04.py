
# 1. 수를 입력 받아서 1부터 입력 받은 수까지의 합을 출력하세요.
number = int(input("수를 입력하세요:"))   # 5
sum = 0
for i in range(1, number + 1):    # 1 2 3 4 5
    sum += i # sum = sum + i

print("합은 %d입니다" % sum)

# 2. 팩토리얼
# 5! = 1 * 2 * 3 * 4 * 5
fact = 1
number = int(input("수를 입력하세요:"))
for i in range(2, number + 1):
    fact *= i   # fact = fact * i

print("%d!은 %d 입니다" % (number, fact))

# 3. 수를 입력 받아서 그 수의 약수를 모두 출력하세요.
number = int(input("수를 입력하세요:"))   # 24
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
