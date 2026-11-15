class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_index = 0
        needle_index = 0
        start_index = 0
        max_range_haystack = len(haystack)
        max_range_needle = len(needle)
        while haystack_index < max_range_haystack:
            if haystack[haystack_index] == needle[needle_index]:
                if needle_index == 0:
                    start_index = haystack_index
                needle_index += 1
                haystack_index += 1
                if needle_index == max_range_needle:
                    return start_index
            else:
                if needle_index > 0:
                    haystack_index = start_index + 1
                    needle_index = 0
                else:
                    haystack_index += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))
    print(sol.strStr("leetcode", "leeto"))
    print("All tests passed successfully!")