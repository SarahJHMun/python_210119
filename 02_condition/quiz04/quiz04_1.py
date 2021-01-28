# 1. 두 점수를 입력 받고, 평균이 70점 이상이면 합격 그렇지 않으면 불합격을 출력하세요.
score1, score2 = input("두 점수를 입력하세요:").split()
score1 = int(score1)
score2 = int(score2)
average = (score1 + score2) / 2

if average >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")
