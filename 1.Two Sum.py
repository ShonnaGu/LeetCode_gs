# 1. Two Sum
# Easy
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        ans = []
        for a_index, a in enumerate(nums):
            b = target - a
            if b in nums:
                b_index = nums.index(b)
                if a_index != b_index:
                    ans.append(a_index)
                    ans.append(b_index)
                    break
        return ans


if __name__ == '__main__':
    nums = [2, 7, 11, 14]
    target = 9
    s = Solution()

    print(s.twoSum(nums, target))