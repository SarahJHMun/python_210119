# 사용자로부터 입력을 받는 함수 - 입력 받은 모든 값은 문자열 형태로 받아진다.
noodle_cup = input("육개장 가격:")
print(noodle_cup)
print(type(noodle_cup))

#print(noodle_cup + 100)     # 문자열이기 때문에 숫자와 연산을 할 수 없다.

# 문자 -> 숫자: 자료형 변환 (casting)
noodle_cup = int(noodle_cup)
print(noodle_cup + 100)
print("육개장 가격은 %d 입니다." % noodle_cup)

# 입력 받은 문자를 숫자로 한번에 변환(casting)
count = int(input("육개장 개수:"))
sum = noodle_cup * count
print("육개장 %d개의 가격은 %d 입니다." % (count, sum))
