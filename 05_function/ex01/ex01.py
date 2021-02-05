# 함수 사용하기
# input ->  ?  -> output

# 1. 출력 함수
print()   # 줄바꿈
print("안녕")

# 2. 길이 구하기
length = len("python")
print("python length:", length)
print(len("python"))

t1 = (5, 6, 7)
print(len(t1))

# 3. 나눈 몫과 나머지 구하기
q, r = divmod(20, 3)   # 전달 인자값, 인수, argument
print("몫:%d 나머지:%d" % (q, r))
