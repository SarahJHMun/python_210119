# 1.
for i in range(1, 7):   # 1 ~ 6
    for j in range(1, 7):  # 1 ~ 6
        print("(%d, %d)" % (i, j), end=" ")
    print()

# 2. 2 ~ 9단 구구단
for i in range(2, 10):   # 2 ~ 9 단수
    for j in range(1, 10):   # 1 ~ 9 곱해지는 값
        print("%d X %d = %d" % (i, j, i * j))

# 3.
# *         행:1     별의 개수:1
# **        행:2              2
# ***       행:3              3
# ****      행:
# *****     행:5              5
for i in range(1, 6):   # 1 ~ 5행
    for j in range(i):  # 행의 번호만큼 반복문이 돈다. 별의 개수(열)
        print("*", end="")
    print()

# 1중 반복문
for i in range(1, 6):
    print("*" * i)
