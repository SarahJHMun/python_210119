# 1. 35 36 37 38 39 40
for i in range(35, 41):
    print(i, end=" ")

print()
# 2. 5 4 3 2 1 0 -1 -2 -3 -4 -5
for i in range(5, -6, -1):
    print(i, end=" ")

print()

# 3. 1 ~ 50 사이의 3의 배수만 출력하세요.
# (1)
for i in range(1, 51):
    if i % 3 == 0:
        print(i, end=" ")
print()
# (2)
for i in range(3, 51, 3):  # 3 6 9 12 15....
    print(i, end=" ")
print()
# 4. 1 ~ 100 사이의 7의 배수 개수를 구하세요.
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1

print("7의 배수의 개수", count)

# 5. 단수 구구단
number = int(input("단수를 입력하세요:"))
for i in range(1, 10):  # 1 2 3 4 5 6 7 8 9
    print("%d X %d = %d" % (number, i, number * i))
