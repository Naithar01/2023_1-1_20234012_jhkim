# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

'''
    1. 무슨 진수인지 입력받음.
    2. 입력 받은 진수에 맞는 정수를 입력 받음
    3. 입력된 정수를 4가지 진수에 맞는 값 출력
'''

base = int(input("입력할 정수의 진수는? (base) >> "))
invert = input('{}진수 정수 입력: >> '.format(base))

data = int(invert, base)

print('2진수: ', bin(data))
print('8진수: ', oct(data))
print('10진수: ', data)
print('16진수: ', hex(data))