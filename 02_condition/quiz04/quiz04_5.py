# 도 : 1개가 뒤집어진 상태
# 개 : 2개가 뒤집어진 상태
# 걸 : 3개가 뒤집어진 상태
# 윷 : 4개가 뒤집어진 상태
# 모 : 하나도 뒤집어지지 않은 상태
st1, st2, st3, st4 = input("윷 상태를 입력:").split()
st1 = int(st1)
st2 = int(st2)
st3 = int(st3)
st4 = int(st4)
count = st1 + st2 + st3 + st4

if count == 1:
    print("도")
elif count == 2:
    print("개")
elif count == 3:
    print("걸")
elif count == 4:
    print("윷")
else:
    print("모")
