# 1. 수를 입력 받아서 그 수만큼 "화이팅!!!" 를 출력하세요
count = int(input("횟수를 입력하세요:"))  # 5
i = 0
while i < count:    # 0 1 2 3 4 => 5번
    print("화이팅!!!")
    i += 1

# 2.
count_down = int(input("카운트다운을 입력하세요:"))   # 3
while count_down >= 0:   # 3 2 1 0   -1
    print(count_down)
    count_down -= 1

print("발사")

# 3.
# 수를 입력하세요: 4      -> 입력
# 출력: 4                -> 출력된 값
i = 0
while (i < 5):    # 0 1 2 3 4  => 5번
    num = int(input("수를 입력하세요:"))
    print("출력:", num)
    i += 1

# 4. 구구단 3단
n = 3
i = 1
while i <= 9:   # 1 2 3 4 5 6 7 8 9
    print("%d X %d = %d" % (n, i, n * i))
    i += 1

