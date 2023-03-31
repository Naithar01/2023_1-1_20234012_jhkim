# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

# 도전 프로그래밍 5번 문제

enter_C = input("온도 입력 >> ")

print("정확 계산: 섭씨: {}, 화씨: {}".format(enter_C, int(enter_C) * 9/5 + 32))
print("약식 계산: 섭씨: {}, 화씨: {}".format(enter_C, int(enter_C) * 2 + 30))

print("차이: {}".format((int(enter_C) * 9/5 + 32) - (int(enter_C) *2 + 30)))


