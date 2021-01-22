# 3. 초를 입력 받아서 ?분?초 형태로 출력 하세요.
seconds = int(input("초:"))
min = seconds // 60
sec = seconds % 60
print("%d분 %d초" % (min, sec))
