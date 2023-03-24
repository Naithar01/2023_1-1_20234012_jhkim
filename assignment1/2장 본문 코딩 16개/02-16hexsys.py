# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

inver = input('16진수 정수 입력 >> ')
data = int(inver, 16) # 입력 문자열을 16진수로 인지해 변환
# 여러 진수로 출력
print('2진수', bin(data))
print('8진수', oct(data))
print('10진수', data)
print('16진수', hex(data))
