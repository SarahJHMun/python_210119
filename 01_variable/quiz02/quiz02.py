# 1.
number1 = 33
number2 = 35.325

# 두 수의 곱은 1165.725000 입니다.
print("두 수의 곱은 %g입니다." % (number1 * number2))

# 2. 943 시간은 몇일 몇시간 인지 구하여 출력하세요.
hour = 943
d = hour // 24
h = hour % 24
print("%d시간은 %d일 %d시간 입니다." % (hour, d, h))

# 3. 가로 길이 8 세로 길이 9인 사각형과 삼각형의 넓이를 각각 구하여 출력하세요.
width = 8
height = 9
rectangle_area = width * height
triangle_area = width * height / 2
print("사각형의 넓이는 %d 입니다." % rectangle_area)
print("삼각형의 넓이는 %g 입니다." % triangle_area)

# 4.
# 국어 93점, 수학 88점, 영어 94점
# 평균 91.67 점 입니다.
korean = 93
math = 88
english = 94
print("국어 %d점, 수학 %d점, 영어 %d점" % (korean, math, english))
average = (korean + math + english) / 3
print("평균 %.2f점 입니다." % average)

# 5. 화씨 구하기
# 섭씨 30
#화씨 온도 = 9 / 5 * 섭씨온도 + 32
c = 30
f = 9 / 5 * c + 32
print("섭씨 %d도는 화씨 %g도 입니다." % (c, f))

