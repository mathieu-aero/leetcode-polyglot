class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size_initial_list = len(nums)
        size_without_duplicate = len(set(nums))

        if size_initial_list == size_without_duplicate:
            return False
        else:
            return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix([1, 2, 3, 1]))
    print(sol.longestCommonPrefix([1, 2, 3, 4]))
    print(sol.longestCommonPrefix([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print("All tests passed successfully!")