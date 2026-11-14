class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        scout_index = 1
        write_index = 0
        max_length = len(nums)

        while scout_index < max_length:
            if nums[write_index] == nums[scout_index]:
                scout_index += 1
            else:
                write_index += 1
                nums[write_index] = nums[scout_index]
                scout_index += 1

        return write_index + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2]))
    print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(sol.removeDuplicates([1, 1, 2]))
    print(sol.removeDuplicates([1, 2, 3, 3]))
    print("All tests passed successfully!")
