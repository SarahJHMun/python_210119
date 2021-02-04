# 중첩 반복문: 반복문 안에 반복문
#   바깥 반복문: 천천히 돈다. ex) 세트        - 행
#   안쪽 반복문: 빠르게 돈다. ex) 운동 횟수    - 열

# 스쿼트 10회
for i in range(1, 11):
    print("스쿼트 %d회" % i)

# 스쿼트 3세트 10회씩
for i in range(1, 4):   # 1 ~ 3세트
    for j in range(1, 11):   # 1 ~ 10회
        print("%d세트째 %d" % (i, j))

# *****
# for i in range(5):   # range(0, 5)   0 1 2 3 4
#     print("*", end="")

# *****
# *****
# *****
for i in range(3):  # 행
    for j in range(5): # 열
        print("*", end="")
    print()  # 줄바꿈
