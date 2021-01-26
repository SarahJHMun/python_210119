weight = int(input("몸무게를 입력하세요:"))

if weight <= 70:
    print("치킨 먹자")
else:
    print("샐러드 먹자")

# if - elif - else
if weight <= 70:     # ~70
    print("치킨")
elif weight <= 75:   # 71 ~ 75
    print("닭가슴살")
elif weight <= 80:   # 76 ~ 80
    print("샐러드")
else:
    print("굶자")
