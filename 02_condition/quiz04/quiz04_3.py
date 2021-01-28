score1 = int(input("점수1:"))
score2 = int(input("점수2:"))
average = (score1 + score2) / 2
if average < 60:
    print("불합격")
else:
    if score1 <= 50 or score2 <= 50:
        print("과락")
    else:
        print("합격")
