class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1
        # max_loops = len(nums)
        # counter = 0
        # max_numbers = 0

        # for i in range(max_loops):
        # if nums[i] == 1:
        # counter += 1
        # if counter > max_numbers:
        # max_numbers = counter
        # else:
        # counter = 0

        # return max_numbers

        # Solution 2
        # Exit ASAP

        max_loops = len(nums)
        remaining_digits = max_loops
        counter = 0
        max_numbers = 0
        still_needed_to_loop = True
        i = 0

        while i < max_loops and still_needed_to_loop:
            if nums[i] == 1:
                counter += 1
                remaining_digits -= 1
                if counter > max_numbers:
                    max_numbers = counter
            else:
                counter = 0
                remaining_digits -= 1
                if max_numbers > remaining_digits:
                    still_needed_to_loop = False

            i += 1

        return max_numbers


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    print(sol.findMaxConsecutiveOnes([1,1,1,1,0,0]))