from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 값과 원본 인덱스를 쌍으로 묶어 저장할 빈 리스트
        indexed = []

        # nums를 순회하며 (값, 원본인덱스) 쌍을 indexed에 추가
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
            elif total < target:
                # 합이 target보다 작으면 왼쪽 포인터를 오른쪽으로 이동 (값 키우기)
                left += 1
            else:
                # 합이 target보다 크면 오른쪽 포인터를 왼쪽으로 이동 (값 줄이기)
                right -= 1

if __name__ == '__main__':
    # Solution 인스턴스 생성 (Java: Solution s = new Solution())
    s = Solution()

    # twosum 호출 후 결과 저장
    result = s.twosum([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 68)

    # 결과 출력
    print(result)                    # [ , ]