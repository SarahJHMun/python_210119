# 1.
# 무한 루프를 통해서 반복적으로 수를 입력을 받고 0이 입력 되었을때 반복문을 빠져 나오게 하세요.

while True:
    number = int(input("수를 입력하세요:"))
    if number == 0:
        print("끝")
        break

# 2.
# 3부터 50까지 3의 배수의 합을 출력하세요.
sum = 0
for i in range(3, 51): # 3 4 5 6 .... 50
    if i % 3 != 0:
        continue   # 아래 코드 수행하지 않고 조건을 보러 간다.

    # 3의 배수
    sum += i

print(sum)
