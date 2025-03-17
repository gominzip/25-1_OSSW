# 사칙연산 함수 정의
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

def get_number(prompt):
    """숫자 입력을 받을 때, 올바른 값이 입력될 때까지 반복"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ 숫자를 입력하세요.")
            
if __name__ == '__main__' :
    ### 사용자 입력
    input1 = get_number('\n첫번째 숫자를 입력하세요: ')

    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
    act = input('기호: ')

    input2 = get_number('\n두번째 숫자를 입력하세요: ')

    ### 연산 수행
    if act == '+':
        result = plus(input1, input2)
    elif act == '-':
        result = minus(input1, input2)
    elif act == '*':
        result = mul(input1, input2)
    elif act == '/':
        result = divide(input1, input2)
    else:
        result = "잘못된 연산 기호입니다."
        
    print(f'사칙연산 결과는 {result}입니다.')
