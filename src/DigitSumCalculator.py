# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# 제한사항
# 0 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 1234	10
# 930211	16
# 입출력 예 설명
# 입출력 예 #1

# 1 + 2 + 3 + 4 = 10을 return합니다.
# 입출력 예 #2

# 9 + 3 + 0 + 2 + 1 + 1 = 16을 return합니다.



def solution(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def solution2 (n) :
    return sum(int(digit) for digit in str(n))



# Test cases
print(solution2(1234))
print(solution2(930211))
print(solution2(0))
print(solution2(1000000))
