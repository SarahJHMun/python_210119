# 0 ~ 4: 5개
for i in range(5):   # 0 1 2 3 4
    print("안녕", i)

print("=" * 50)

# 1 ~ 5: 5개
for i in range(1, 6): # 1 2 3 4 5
    print("딸기", i)

print("=" * 50)

# 5 ~ 1: 5개
for i in range(5, 0, -1):   # 5 4 3 2 1
    print("수박", i)

print("=" * 50)

# 반복할 횟수만큼 돌기
count = int(input("반복할 횟수를 입력하세요:"))   # 3

for i in range(count):  # 0 1 2 => 3번
    print(i, end=' ')

print()
print("끝")
