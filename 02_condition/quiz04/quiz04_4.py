# 4로 나누어 떨어지는 연도는 윤년이다.
# 100으로 나누어 떨어지는 연도는 윤년이 아니다.
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.
year = int(input("연도를 입력하세요:"))
# 1. 무식하게 푸는 방법
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년")
        else:
            print("평년")
    else:
        print("윤년")
else:
    print("평년")

# 2.
# 4로 나누어 떨어지는 연도는 윤년이다.
#   100으로 나누어 떨어지는 연도는 윤년이 아니다. 
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다. 
if year % 400 == 0:
    print("윤년")
elif year % 100 == 0:
    print("평년")
elif year % 4 == 0:
    print("윤년")
else:
    print("평년")

# 4로 나누어 떨어지는 연도는 윤년이다.
# 100으로 나누어 떨어지지 않는 연도는 윤년이다.
#  => 4로 나누어 떨어지는 연도 그리고 100으로 나누어 떨어지지 않는 연도 윤년
#     또는
#     400으로 나누어 떨어지는 연도는 무조건 윤년이다.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년")
else:
    print("평년")

condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0
if condition1 or condition2:
    print("윤년")
else:
    print("평년")
