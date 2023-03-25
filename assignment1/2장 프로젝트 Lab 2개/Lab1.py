# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

'''
    1. 두 개의 실수를 입력 받는다.
        - input, float 사용
    2. 두 실수의 사칙연산 결과를 출력한다.
    3. 하나의 연산식을 입력받아 그 결과를 출력 
        - expression 연산식 저장, eval 사용 출력
'''

num1 = input('첫 번째 수 입력 >>')
num2 = input('두 번째 수 입력 >>')

num1 = float(num1)
num2 = float(num2)

print('합: {}\n차: {}\n곱하기: {}\n나누기: {}'
      .format(num1 + num2, num1 - num2, num1 * num2, num1 / num2))

expression = input('연산식 입력(예 3.2 + 4 * 1.5) >> ')
print('연산식: {} 결과: {}'.format(expression, eval(expression)))
