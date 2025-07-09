"""
거스름돈 문제
500 100 50 10 원 동전이 있다.
 거스름돈 n을 최소한의 동전으로 거슬러 주는 방법을 구하는 함수
 매개변수로 거스름돈 n이 주어질 때, 최소한의 동전 개수를 return하도록 solution 함수를 완성해주세요.
 제한사항
 n은 10의 배수입니다.
 0 ≤ n ≤ 1,000,000
"""


def solution(n):
    coins = [500, 100, 50, 10]
    return sum(n // coin for coin in coins if (n := n % coin) or True)


def solution2(n):
    count = 0

    # 큰 단위의 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]

    # % 는 나머지를 구하는 연산자이고, //은 정수 나눗셈을 의미합니다.
    # 즉 1260 // 500 = 2 이고
    # 1260 % 500 = 260 이 됩니다. ( 2 나머지 260 이니까 )
    for coin in coin_types:
        count += n // coin
        n %= coin
    return count


print(solution2(1260))
print(solution2(2660))

print(solution(1260))
print(solution(2660))

# /은 몫을 구하는 연산자이고, //은 정수 나눗셈을 의미합니다.
