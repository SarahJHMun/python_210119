a, b, c = input("3개의 수를 입력하세요:").split()
a = int(a)
b = int(b)
c = int(c)

max = a
if max < b:
    max = b
if max < c:
    max = c
print(max)
