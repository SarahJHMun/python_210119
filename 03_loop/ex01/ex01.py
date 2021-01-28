# 안녕 3번쓰기
print("안녕")
print("안녕")
print("안녕")

print("=" * 50)

# "안녕" 3번 쓰기 while 반복문
i = 0  # 카운팅 변수
while i < 3:     # 0 1 2  => 3번
    print("안녕", i)
    i += 1   # i = i + 1

# 0 ~ 4: 5번
i = 0
while i < 5:
    print("Hello world", i)
    i += 1  # 복합 대입 연산자

# 1 ~ 5: 5번
i = 1
while i <= 5:
    print("안녕", i)
    i += 1

# 5 ~ 0 : 6번
i = 5
while i >= 0:
    print("hello world", i)
    i -= 1

# 1+2+3+4+5 = 합계
i = 1
sum = 0
while i <= 5:
    sum += i  # sum = sum + i
    i += 1

print(sum)

# 무한루프
# while True:
#     print("무한루프")

# 0은 거짓(False)   0이 아닌 수는 (True)
while 1:
    print("1 무한루프")
