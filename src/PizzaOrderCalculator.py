"""
문제 설명
머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를
return 하도록 solution 함수를 완성해보세요.

제한사항
2 ≤ slice ≤ 10
1 ≤ n ≤ 100
입출력 예
slice	n	result
7	10	2
4	12	3
입출력 예 설명
입출력 예 #1

10명이 7조각으로 자른 피자를 한 조각 이상씩 먹으려면 최소 2판을 시켜야 합니다.
입출력 예 #2

12명이 4조각으로 자른 피자를 한 조각 이상씩 먹으려면 최소 3판을 시켜야 합니다.
"""
import math
def solution(slice, n):
    return math.ceil(n/slice)
print(solution(2,2))
print(solution(10,4))
print(solution(12,3))

"""
math.ceil 은 올림함수 즉, 소수점이 있으면 무조건 위로 올려 정수를 만든다)
math.ceil(1.1) = 2
math.ceil(1.9) = 2
math.ceil(2.01) = 3
"""