"""
ㅁ

거스름돈 문제
500 100 50 10 원 동전이 있다.
 거스름돈 n을 최소한의 동전으로 거슬러 주는 방법을 구하는 함수 매개변수로 거스름돈 n이 주어질 때,
 최소한의 동전 개수를 return하도록 solution 함수를 완성해주세요.
 제한사항
 n은 10의 배수입니다.
 0 ≤ n ≤ 1,000,000
"""

"""
n 이 임의의 값으로 주어진다 ex) 1260
이 숫자를 최소한의 동전 개수로 거스름돈을 만들어주는 함수를 완성하자.

거스름 돈
n = 1260 
동전 갯수
count = 0

동전값을 갖고있는 배열을 만든다.
coins = [500, 100, 50, 10]

이 배열을 반복하여 1260을 동전으로 나눈 몫을 구한다.
for coin in coins :
count = n // coin      n 을 coin 값으로 나눈 몫을 구해서 count 에 넣는 코드
n = n % coin           n 을 coin 값으로 나눈 나머지를 n 에 다시 넣는 코드

return count

"""

# n값이 주어질 때 ( 입력이든 , 함수의 매개변수든 )
# 최소한의 동전 개수를 return 하도록 solution을 완성
# 500 , 100 , 50 , 10 이 있고
# n을 최소한의 동저 갯수를 구하자

def solution(n):
    coins = [500, 100, 50, 10]
    return sum(n // coin for coin in coins if (n := n % coin) or True)


def solution2():
    n = int(input())
    count = 0

    # 큰 단위의 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]

    # % 는 나머지를 구하는 연산자이고, //은 정수 나눗셈을 의미합니다.
    # 즉 1260 // 500 = 2 이고
    # 1260 % 500 = 260 이 됩니다. ( 2 나머지 260 이니까 )
    for coin in coin_types:
        count += n // coin
        n = n % coin

    return print(count)

# /은 몫을 구하는 연산자이고, //은 정수 나눗셈을 의미합니다.

if __name__ == '__main__':
    solution2()