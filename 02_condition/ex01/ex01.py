weight = int(input("몸무게를 입력하세요:"))

# 만약에 몸무게가 55키로 미만이면 "치킨"
if weight < 55:
    print("치킨 먹자!")

# 만약에 몸무게가 100키로 이상이면 "다이어트 시작"
if weight >= 100:
    print("다이어트 시작")

if 100 <= weight:
    print("다이어트 시작")

# 만약에 몸무게가 68키로 이면 "68키로 이군요"
if weight == 68:
    print("68키로 이군요")

# 만약에 몸무게가 75키로가 아니면 "75키로가 아니다"
if weight != 75:
    print("75키로가 아니다")

# 두 개의 수 입력받고 비교하기
n1, n2 = input("두 개의 수를 입력하세요:").split()
n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    print("%d이 %d보다 더 크다" % (n1, n2))
if n1 < n2:
    print("%d가 %d보다 작다" % (n1, n2))
if n1 == n2:
    print("%d와 %d는 같다" % (n1, n2))

condition = n1 != n2
if condition:
    print("%d과 %d는 같지 않다." % (n1, n2))




