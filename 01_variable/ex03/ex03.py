# 산술 연산
noodle_cup = 850
print("육개장 가격:", noodle_cup)

# 육개장 3개의 가격 계산
sum = noodle_cup * 3
print("육개장 3개의 가격:", sum)

# 가격 상승
noodle_cup = noodle_cup + 100
print("가격 상승 후 육개장 가격:", noodle_cup)

print("육개장 3개의 가격:", noodle_cup * 3)

# 변수 여러개
# 육개장 하나의 가격은 OO원 이고, 육개장 3개의 가격은 OO원 입니다.
print('육개장 하나의 가격은', noodle_cup, "원 이고, 육개장 3개의 가격은",
      noodle_cup * 3, "원 입니다.")

# 10,000원으로 육개장 3개를 산 후 거스름돈 구하기
money = 10000
change = money - sum
print("거스름돈:", change)

# 5,000원으로 육개장 몇 개를 살 수 있고, 거스름돈은 얼마나 남는가?
money = 5000
buy_noodle_cup = money / noodle_cup
print('살 수 있는 개수:', buy_noodle_cup)   # 소수로 나온다.

buy_noodle_cup = money // noodle_cup
print("살 수 있는 개수:", buy_noodle_cup)   # 몫만 구한다.

change = money % noodle_cup    # 나머지를 구한다.
print("거스름돈:", change)

# 제곱
# 5^3
print("5의 3제곱", 5 ** 3)
