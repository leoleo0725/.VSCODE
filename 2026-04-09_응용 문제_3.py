# 20263318 박상준 2026-04-09

import random

num_of_correct=0
total=0

print("덧셈 연산 테스트를 시작합니다. (총 5문제) ")
print("======================================")

num1=random.randint(1,100)
num2=random.randint(1,100)
answer=int(input(f"{num1}+{num2} = "))

if answer==(num1+num2):
    print("정답입니다!.")
    num_of_correct+=1
else: 
    print("땡!!")

num1=random.randint(1,100)
num2=random.randint(1,100)
answer=int(input(f"{num1}-{num2} = "))

if answer==(num1-num2):
    print("정답입니다!.")
    num_of_correct+=1
else: 
    print("땡!!")

num1=random.randint(1,100)
num2=random.randint(1,100)
answer=int(input(f"{num1}*{num2} = "))

if answer==(num1*num2):
    print("정답입니다!.")
    num_of_correct+=1
else: 
    print("땡!!")

num1=random.randint(1,100)
num2=random.randint(1,100)
answer=int(input(f"{num1}%{num2} = "))

if answer==(num1%num2):
    print("정답입니다!.")
    num_of_correct+=1
else: 
    print("땡!!")

num1=random.randint(1,100)
num2=random.randint(1,100)
answer=int(input(f"{num1}+{num2} = "))

if answer==(num1+num2):
    print("정답입니다!.")
    num_of_correct+=1
else: 
    print("땡!!")

print("======================================")

total=num_of_correct*20
print(f"총 {num_of_correct}개의 문제를 맞췄고, {total}점 입니다.")
