"""
5와 6의 차이 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	14640	10944	9940	76.157%
문제
상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)

출력
첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

예제 입력 1
11 25
예제 출력 1
36 37
예제 입력 2
1430 4862
예제 출력 2
6282 6292
예제 입력 3
16796 58786
예제 출력 3
74580 85582
"""


def solution():
    a, b = input().split()  # 문자열로 받기!

    # 각 숫자에 대해 최솟값/최댓값 버전 만들기
    a_min = a.replace('6', '5')  # a에서 6을 5로 바꾼 버전
    b_min = b.replace('6', '5') # b에서 6을 5로 바꾼 버전

    a_max = a.replace('5', '6') # b에서 6을 5로 바꾼 버전
    b_max = b.replace('5', '6') # b에서 5를 6으로 바꾼 버전

    minimum = int(a_min) + int(b_min)
    maximum = int(a_max) + int(b_max)

    print(minimum, maximum)

if __name__ == '__main__' :
    solution()