# 2. 교체
x = int(input("x:"))    # 6
y = int(input("y:"))    # 4
#print("x는 %d이고 y는 %d입니다." % (y, x))

temp = x
x = y
y = temp
print("x는 %d이고 y는 %d입니다." % (x, y))
