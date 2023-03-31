# 2023-03-24 | 20:18 학번: 20234012 | 이름: 김정호 | 컴퓨터정보공학과 재직자 과정

# 도전 프로그래밍 6번 문제

num1 = input('첫 번째 수 입력 >>')
num2 = input('두 번째 수 입력 >>')

num1 = int(num1)
num2 = int(num2)

print('{} / {} ==> {}\n{} % {} ==>{}\n{} // {} ==>{}\n{} ** {} ==>{}'
      .format(num1, num2, float(num1) / float(num2),num1, num2, num1 % num2,num1, num2, num1 // num2,num1, num2, num1 ** num2))
