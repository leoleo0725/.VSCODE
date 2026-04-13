# 20263318 박상준 2026-04-09


print("=========================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("메뉴 4번: 콜라")
print("=========================")
menu=int(input("메뉴 번호를 입력하에요 : "))
if menu==1:
    print('치즈 버거를 선택하셨습니다.')
    menu=6000
elif menu==2:
    print('치킨 버거를 선택하셨습니다.')
    menu=5000
elif menu==3:
    print('불고기 버거를 선택하셨습니다.')
    menu=7000
elif menu==4:
    print('콜라를 선택하셨습니다.')
    menu=2000
else:
    print("다시 입력하세요.")

count=int(input("수량을 입력하세요 : "))
total=menu*count
print("총 주문 금액은", total, "원 입니다.")
