class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        element_counts = {}
        majority_element_research_ongoing = True
        i = 0
        max_iterations = len(nums)
        majority_threshold = len(nums)//2

        while i < max_iterations and majority_element_research_ongoing:
            if nums[i] in element_counts:
                element_counts[nums[i]] += 1
            else:
                element_counts[nums[i]] = 1
            if element_counts[nums[i]] > majority_threshold:
                majority_element_research_ongoing = False
            else:
                i += 1
        return nums[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print("All tests passed successfully!")