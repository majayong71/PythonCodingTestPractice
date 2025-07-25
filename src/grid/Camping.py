"""
캠핑 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	36257	14519	12338	39.574%
문제
등산가 김강산은 가족들과 함께 캠핑을 떠났다. 하지만, 캠핑장에는 다음과 같은 경고문이 쓰여 있었다.

캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있습니다.

강산이는 이제 막 28일 휴가를 시작했다. 이번 휴가 기간 동안 강산이는 캠핑장을 며칠동안 사용할 수 있을까?

강산이는 조금 더 일반화해서 문제를 풀려고 한다.

캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다.
강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다.
모든 입력 정수는 int범위이다. 마지막 줄에는 0이 3개 주어진다.

출력
각 테스트 케이스에 대해서, 강산이가 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.

예제 입력 1
5 8 20
5 8 17
0 0 0
예제 출력 1
Case 1: 14
Case 2: 11
"""

def solution():
    case_num = 1

    while True:
        L, P, V = map(int, input().split())

        # 종료 조건: 0 0 0이 입력되면 프로그램 종료
        if L == 0 and P == 0 and V == 0:
            break

        # 완전한 주기 수: V를 P로 나눈 몫
        full_cycles = V // P

        # 완전한 주기에서 캠핑 가능한 총 일수
        camping_days_from_full_cycles = full_cycles * L

        # 남은 날들: V를 P로 나눈 나머지
        remaining_days = V % P

        # 남은 날들에서 추가로 캠핑 가능한 일수
        # L일까지만 캠핑 가능하므로 min(remaining_days, L)
        additional_camping_days = min(remaining_days, L)

        # 총 캠핑 가능한 일수
        total_camping_days = camping_days_from_full_cycles + additional_camping_days

        print(f"Case {case_num}: {total_camping_days}")
        case_num += 1


# 한 줄 공식으로도 가능
def solution_short():
    case_num = 1

    while True:
        L, P, V = map(int, input().split())

        if L == 0 and P == 0 and V == 0:
            break

        # 공식: (V // P) * L + min(V % P, L)
        result = (V // P) * L + min(V % P, L)

        print(f"Case {case_num}: {result}")
        case_num += 1


if __name__ == '__main__':
    solution()
