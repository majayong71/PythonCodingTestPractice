"""
잃어버린 괄호
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	107519	60182	46776	55.264%
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고,
5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1
55-50+40
예제 출력 1
-35
예제 입력 2
10+20+30+40
예제 출력 2
100
예제 입력 3
00009-00009
예제 출력 3
0
"""

def solution():
    expression = input() # 수식 입력
    numbers = []         # 숫자를 저장할 리스트
    current_number = ""  # 현재 숫자를 저장할 문자열
    operators = []       # 연산자

    for char in expression:
        if char.isdigit():           # char 가 숫자인 경우
            current_number += char   # current_number 에 대입
        else:
            numbers.append(int(current_number))  # 숫자가 아닌 경우 ( 연산자인 경우 )
            operators.append(char)
            current_number =""

    numbers.append(int(current_number))

    # 최소값 계산
    # - 연산자를 기준으로 분리
    groups = expression.split('-')

    # 첫 번째 그룹은 그대로 계산
    result = sum(int(x) for x in groups[0].split('+'))

    # 나머지 그룹은 각각 괄호로 묶은 효과 (그룹 내 모든 수를 더한 후 뺌)
    for group in groups[1:]:
        result -= sum(int(x) for x in group.split('+'))

    print(result)  # 결과 출력


if __name__ == '__main__':
    solution()
