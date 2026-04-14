# 20263318 박상준 2026-04-14

print("성적 처리 프로그램을 실작합니다.")
py_score=int(input("파이썬 점수 입력 : "))
eng_score=int(input("대학 영어 점수 입력 : "))
cup_engg_score=int(input("컴퓨터공학개론 점수 입력 : "))
total=py_score + eng_score + cup_engg_score
ave=(py_score + eng_score + cup_engg_score)/3
print("------점수 출력------")
print("파이썬 점수 : ")
print("대학 영어 점수 : ")
print("컴퓨터공학개론 점수 : ")
print("--------------------")
print("총 점수 : ", total, "평균 점수 : ", "%.2f" %ave)

