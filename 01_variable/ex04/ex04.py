# format: 문자열 속에 다른 타입의 변수값을 넣을 때 사용한다.

noodle_cup = 850

# 정수(Integer)
print("육개장 하나의 가격은 %d입니다." % noodle_cup)

# 여러개 변수 출력
print("육개장 하나의 가격은 %d이고 3개의 가격은 %d 입니다." % (noodle_cup, noodle_cup * 3))

# 소수(Float)
pi = 3.14
print("원주율 pi는 %f입니다." % pi)
print("원주율 pi는 %g입니다." % pi)
print("원주율 pi는 %d입니다." % pi)

# 문자(Character)
grade = 'A'
print("등급은 %c입니다." % grade)

# 문자열(String)
name = "신보람"
print("내 이름은 %s입니다." % name)

# 소수점 표시
real_pi = 3.141592653
print("원주율: %f" % real_pi)  # 기본으로 6째 자리까지 출력
print("소수점 둘째자리: %.2f" % real_pi)  # 소수점 둘째자리까지 반올림
print("소수점 여덟째자리: %.8f" % real_pi)

# 95%
print("%d%%" % 95)
