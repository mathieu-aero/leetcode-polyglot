class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_length = len(nums)
        counter = 1
        longest_continuous_subsequence = 1
        starting_value = nums[0]

        for i in range(1, max_length):
            if nums[i] > starting_value:
                counter += 1
                if counter > longest_continuous_subsequence:
                    longest_continuous_subsequence = counter
            else:
                counter = 1
            starting_value = nums[i]

        return longest_continuous_subsequence


if __name__ == "__main__":
        sol = Solution()
        assert sol.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
        assert sol.findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
        assert sol.findLengthOfLCIS([2, 1, 2, 3, 2]) == 3
        assert sol.findLengthOfLCIS([2, 1, 2, 3, 4]) == 4
        assert sol.findLengthOfLCIS([1, 3, 5, 7, 9]) == 5
        print("All tests passed successfully!")