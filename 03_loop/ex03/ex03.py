# break문
# 무한루프에서 hello world 다섯번 찍기
i = 0
while True:     # 0 1 2 3 4   5
    if i == 5:
        break
    print("Hello world", i)
    i += 1

# continue문 : skip
# 1 ~ 10 4의 배수일 때는 숫자를 출력하지 않기
# 1 2 3 5 6 7 9 10
for i in range(1, 11):
    if i % 4 == 0:
        pass   # 아무것도 안한다
    else:
        print(i)

for i in range(1, 11):  # 1 ~ 10
    if i % 4 == 0:
        continue  # 아래 코드들은 수행하지 않고 조건쪽으로 올라간다.

    print(i, end=" ")  # 4의 배수가 아니다.
