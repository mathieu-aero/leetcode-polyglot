class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        scout_index = 0
        write_index = 0
        max_length = len(nums)

        while scout_index < max_length:
            if nums[scout_index] == val:
                scout_index += 1
            else:
                nums[write_index] = nums[scout_index]
                write_index += 1
                scout_index += 1

        return write_index


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3, 2, 2, 3], 3))
    print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print("All tests passed successfully!")
