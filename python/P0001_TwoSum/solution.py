class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        solution_still_not_found = True
        index_first_number = 0
        index_second_number = 0
        values_considered = {}

        while i < len(nums) and solution_still_not_found:
            if target - nums[i] in values_considered:
                index_first_number = i
                index_second_number = values_considered[target - nums[i]]
                solution_still_not_found = False
            else:
                values_considered[nums[i]] = i
                i += 1
        return [index_first_number, index_second_number]


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([-3, 4, 3, 90], 0))
    print(sol.twoSum([2, 7, 11, 15], 18))
    print(sol.twoSum([2, 7, 11, 15], 26))
    print(sol.twoSum([2, 7, 11, 15], 22))