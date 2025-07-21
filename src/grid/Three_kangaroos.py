"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	6925	2831	2468	42.246%
문제
캥거루 세 마리가 사막에서 놀고 있다. 사막에는 수직선이 하나 있고, 캥거루는 서로 다른 한 좌표 위에 있다.

한 번 움직일 때, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프한다.
한 좌표 위에 있는 캥거루가 두 마리 이상일 수는 없다.

캥거루는 최대 몇 번 움직일 수 있을까?

입력
여러개의 테스트 케이스로 이루어져 있으며, 세 캥거루의 초기 위치 A, B, C가 주어진다. (0 < A < B < C < 100)

출력
각 테스트에 대해 캥거루가 최대 몇 번 움직일 수 있는지 출력한다.

예제 입력 1
2 3 5
3 5 9
예제 출력 1
1
3
"""
import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())
    moves = 0

    while True:
        left_gap = b - a - 1 # A와 B 사이 빈 공간
        right_gap = c - b - 1 # B 와 C 사이 빈 공간

        # 빈 공간이 없다면 루프 종료
        if left_gap == 0 and right_gap == 0:
            break

        if left_gap >= right_gap:
            # C를 A와 B 사이로 이동
            a, b, c = a, a+1, b
        else:
            # A를 B와 C 사이로 이동
            a, b, c = b, c-1, c
        moves += 1

    print(moves)