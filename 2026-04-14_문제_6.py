# 20263318 박상준 2026-04-14

num=int(input("변환할 10진수 입력 : "))
print("진법 변환 결과 출력")
print("### 10진수 : ", num)

num1=bin(num)
print("### 2진수 : ",num1)

num2=oct(num)
print("### 8진수 : ",num2)

num3=hex(num)
print("### 16진수 : ",num3)