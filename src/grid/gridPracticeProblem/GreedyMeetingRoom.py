# 어렵다 이 문제 여러번 봐 보자.
"""
회의실 배정
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	257348	87503	60236	31.553%

문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""
"""
한 개의 회의실이 있고 이를 사용하고자 하는 N개의 회의가 있다.
각 회의 I에 대해 시작시간과 끝나는시간이 주어지고
각 회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수를 구하자.

N개의 회의 입력받고
각 회의 I에 대해 시작시간 , 끝나는시간을 입력받는다.

N = int(input())  # 회의 개수
meetings = [] 데이터를 저장할 배열 선언해두기.

for _ in range(N) : # 입력받은 N개의 회의 개수만큼 반복하는 반복문 선언
start, end = map(int, input().split()) # 각 회의의 시작시간 , 끝나는시간 입력받기
meetings.append((start, end)) # 입력받은 시작시간 , 끝나는시간을 튜플로 묶어서 배열에 저장

# 끝나는 시간 순으로 정렬하는게 효율적인 풀이 접근이기 때문에, 회의 시간이 끝나는 시간 순으로 정렬 
meetings.sort(key=lambda x: (x[1], x[0]))
count = 0 # 선택한 회의 갯수
end_time = 0 # 마지막 회의가 끝나는 시간

# meetings 배열의 각 회의를 하나씩 꺼내서 확인하는 반복문 선언
for start, end in meetings : 
# 시작 시간이 회의가 끝나는 시간과 같거나 크면
# end 값을 end_time 에 대입하고 count 1 증가
if start >= end_time :
    end_time = end
    count += 1
    
    print(count)


"""
"""
입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고
회의의 시작시간과 끝나는 시간이 주어진다.
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력 한다.

예제 입력 1
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
예제 출력 1
4
"""

def solution():
    n = int(input())  # 회의 개수
    meetings = []

    # 회의 시작시간과 끝나는 시간 입력 받기
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    # 끝나는 시간을 기준으로 오름차순 정렬 끝나는 시간이 같다면
    # 시작이 빠른 회의를 먼저 본다.
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0  # 선택한 회의 개수
    end_time = 0  # 마지막 회의 끝난 시간

    for start, end in meetings:
        if start >= end_time:  # 현재 회의가 이전 회의 끝난 이후 시작하면
            count += 1  # 회의 선택
            end_time = end  # 끝나는 시간 갱신

    print(count)
"""

def solution():
    n = int(input())  # 회의 개수
    meetings = []

    # 회의 시작시간과 끝나는 시간 입력 받기
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    # 끝나는 시간을 기준으로 오름차순 정렬 끝나는 시간이 같다면
    # 시작이 빠른 회의를 먼저 본다.
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0  # 선택한 회의 개수
    end_time = 0  # 마지막 회의 끝난 시간

    # meetings 배열의 각 회의를 하나씩 꺼내서 확인하는 반복문 선언
    for start, end in meetings:
        # 현재 회의의 시작시간이 이전 회의의 끝나는 시간과 겹치지 않는지 확인
        if start >= end_time:  # 현재 회의가 이전 회의 끝난 이후 시작하면
            count += 1  # 회의 선택
            end_time = end  # 끝나는 시간 갱신

    # 출력 ..! 
    print(count)

if __name__ == '__main__':
    solution()
"""

# 3차 풀이

"""
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다.
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""

def solution2():
    n = int(input())
    meetings = []

    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    meetings.sort(key=lambda x: (x[1], x[0]))
    count = 0
    end_time =0

    for start, end in meetings :
        if start >= end_time :
            count += 1
            end_time = end

    print(count)


if __name__ == '__main__':
    solution2()
