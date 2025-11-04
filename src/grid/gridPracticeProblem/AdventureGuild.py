"""
<문제> 모험가 길드 : 문제설명
- 한 마을에 모험가가 N명 있습니다.
모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
'공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
- 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야
여행을 떠날 수 있도록 규정했습니다.
- 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.
N명의 모험가에 대한 정보가 주어졌을 때,
여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
"""
def solution (fear_levels):
    fear_levels.sort() # 공포도를 오름차순으로 정렬
    group_count = 0 # 그룹의 수
    current_group_size = 0 # 현재 그룹에 모인 인원 수

    for fear in fear_levels:
        current_group_size += 1 # 현재 그룹에 한 명 추가 모험가 한명 포함한다는 뜻
        if current_group_size >= fear:
            group_count += 1 # 현재 그룹의 인원 수가 공포도 이상이면 그룹을 완성
            current_group_size = 0 # 현재 그룹 초기화 다음 그룹 준비
    return group_count # 완성된 그룹의 수 반환
# Test cases
print(solution([2, 3, 1, 2, 2]))  # Output: 2
print(solution([1,1,1,1]))  # Output: 4
print(solution([4,4,4,4]))  # Output: 1
print(solution([1,2,2,3,3]))  # Output: 2
"""
 풀이 : 공포도를 오름차순으로 정렬한 후, 각 모험가의 공포도에 따라 그룹을 구성한다.
 - 공포도가 낮은 모험가부터 시작하여 현재 그룹에 모인 인원 수를 증가시킨다.
 - 현재 그룹의 인원 수가 해당 모험가의 공포도 이상이 되면 그룹을 완성하고, 그룹 수를 증가시킨다.
 - 현재 그룹의 인원 수를 초기화하여 다음 그룹을 준비한다.
 - 최종적으로 완성된 그룹의 수를 반환한다.
 - 시간복잡도는 O(N log N) (정렬에 의한) + O(N) (그룹 구성에 의한) = O(N log N)
"""

# 입력 방식 으로 푸는 경우
if __name__ == '__main__':

    n = int(input())  # 모험가의 수
    fear_levels = list(map(int, input().split()))  # 각 모험가의 공포도 입력
    fear_levels.sort()  # 공포도를 오름차순으로 정렬

    result = 0 # 총 그룹의 수
    count = 0  # 현재 그룹에 포함된 모험가의 수

    for i in fear_levels:
        count += 1
        if count >= i:
            result += 1
            count = 0

    print(result)  # 최종 그룹의 수 출력
