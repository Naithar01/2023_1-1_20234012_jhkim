# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

# 도전 프로그래밍 7번 문제

inver1 = input('첫 번째 16진수 실수 입력 >> ')
inver2 = input('두 번쨰 16진수 실수 입력 >> ')

data1 = float.fromhex(inver1)
data2 = float.fromhex(inver2)

print("실수1: {} 실수2: {}".format(data1, data2))

print("합: {}\n차ㅣ {}\n곱하기: {}\n나누기: {}\n ".format(data1 + data2, data1 - data2, data1 * data2, data1 / data2))
