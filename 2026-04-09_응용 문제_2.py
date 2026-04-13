# 20263318 박상준 2026-04-09

num1=int(input("num1 입력 : "))
num2=int(input("num2 입력 : "))
num3=int(input("num3 입력 : "))

if num1>num2 : 
    num_high=num1
elif num2>num1 : 
    num_high=num2


if num3>num_high :
    print(f"가장 큰 수는 {num3}입니다.")
elif num_high>num3 :
    print(f"가장 큰 수는 {num_high}입니다.")