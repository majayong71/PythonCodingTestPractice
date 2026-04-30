from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexed = []
        for i in range(len(nums)):
            indexed.append((nums[i], i))

        indexed.sort()

        left  = 0
        right = len(indexed) - 1

        while left < right:
            total = indexed[left][0] + indexed[right][0]

            if total == target:
                return [indexed[left][1], indexed[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    s = Solution()                      # Java: Solution s = new Solution()
    result = s.twoSum([2,7,11,15], 26)  # Java: s.twoSum(new int[]{2,7,11,15}, 9)
    print(result)                       # [0, 1]