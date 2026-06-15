# TWOSUM 문제 ,
# 배열 안에 있는 값 을 더해
# 타겟의 값이 나오게 해라
# ex) [1,3,5,7,9] , target:16
# 3, 4

#1. 두 개의 합계
#정수 배열 nums 과 정수 가 주어졌을 때 target, 두 숫자의 합이 가 되도록 하는 두 숫자의 인덱스를target 반환합니다 .
#각 입력값에는 정확히 하나의 해답이 있으며 , 동일한 요소를 두 번 사용할 수 없다고 가정할 수 있습니다 .
#답변은 어떤 순서로든 반환하셔도 됩니다.

#예시 1:
#입력: nums = [2,7,11,15], target = 9
#출력: [0,1]
#설명: nums[0] + nums[1] == 9이므로 [0, 1]을 반환합니다.
#예시 2:
#입력: nums = [3,2,4], 목표값 = 6
#출력: [1,2]
#예시 3:
#입력: nums = [3,3], 목표 = 6
#출력: [0,1]


class Solution:
    def twosum(self, nums,target):

        # 값과 원본 인덱스를 쌍으로 묶어 저장할 빈 리스트
        indexed = []

        # nums를 순회하며 (값, 원본인덱스) 쌍을 indexed에 추가 (튜플 사용)
        for i in range(len(nums)):
            indexed.append((nums[i], i))
        # 투포인터를 쓰기 위해 값 기준으로 오름차순 정렬
        indexed.sort()
        # 제일 작은 값을 가리키는 왼쪽 포인터
        left = 0
        # 제일 큰 값을 가리키는 오른쪽 포인터
        right = len(indexed) - 1
        # 두 포인터가 만나기 전까지 반복
        while left < right:

            # 현재 왼쪽 값 + 오른쪽 값의 합계
            total = indexed[left][0] + indexed[right][0]

            if total == target:
                # 정답 찾음 → 두 값의 원본 인덱스 반환
                return [indexed[left][1], indexed[right][1]]
                # 합이 target보다 작으면 왼쪽 포인터를 오른쪽으로 이동 (값 키우기)
            elif total < target:
                # 합이 target보다 크면 오른쪽 포인터를 왼쪽으로 이동 (값 줄이기)
                left += 1

            else:
                right -= 1

if __name__ == '__main__':
    s = Solution()                      # Java: Solution s = new Solution()
    result = s.twosum([2,3,5,7,11,13,17,19,23,29,31,37], 68)  # Java: s.twoSum(new int[]{2,3,5,7,11,13,17,19,23,29,31,37}, 68)
    print(result)
