# 20263318 박상준 2026-04-14
import random

print("연산자 연습을 시작합니다. ")

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#1 : ", op1, "+", op2, "=", end=" ")
ans1=int(input(""))
cor1=(op1+op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#2 : ", op1, "*", op2, "=", end=" ")
ans2=int(input(""))
cor2=(op1*op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#3 : ", op1, "/", op2, "=", end=" ")
ans3=float(input(""))
cor3=(op1/op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#4 : ", op1, "%", op2, "=", end=" ")
ans4=int(input(""))
cor4=(op1%op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#5 : ", op1, ">", op2, ":", end=" ")
ans5=bool(input(""))
cor5=(op1>op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#6 : ", op1, "==", op2, ":", end=" ")
ans6=bool(input(""))
cor6=(op1==op2)

op1=random.randint(1,10)
op2=random.randint(1,10)
print("#7 : ", op1, "!=", op2, ":", end=" ")
ans7=bool(input(""))
cor7=(op1!=op2)

print("### 테스트 결과 : ")
if ans1==cor1:
    print("1번 정답")
else:
    print("1번 오답")
if ans2==cor2:
    print("2번 정답")
else:
    print("2번 오답")
if ans3==cor3:
    print("3번 정답")
else:
    print("3번 오답")
if ans4==cor4:
    print("4번 정답")
else:
    print("4번 오답")
if ans5==cor5:
    print("5번 정답")
else:
    print("5번 오답")
if ans6==cor6:
    print("6번 정답")
else:
    print("6번 오답")
if ans7==cor7:
    print("7번 정답")
else:
    print("7번 오답")