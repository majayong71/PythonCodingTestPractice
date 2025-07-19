"""
타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로
 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

출력
제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.

예제 입력 1
380
예제 출력 1
4
예제 입력 2
1
예제 출력 2
15
"""

def solution():
    # 타로가 낸 돈
    taro_paid = 1000

    # 물건 값
    price = int(input())

    # 잔 돈
    changes = taro_paid - price

    # 돈 종류
    money_types =[500, 100, 50, 10, 5, 1]

    # 잔돈의 개수
    total = 0

    # money로 changes를 나누어주고 몫을 total에 누적한다.
    # 그리고 money로 changes를 나눈 나머지값을 changes에 다시 저장한다.

    for money in money_types:
        total += changes // money
        changes = changes % money

    return total

if __name__ == "__main__":
    print(solution())
    # 예제 입력 1: 380
    # 예제 출력 1: 4
    # 예제 입력 2: 1
    # 예제 출력 2: 15