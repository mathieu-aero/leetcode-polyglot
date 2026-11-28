class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        max_range = len(t)
        max_loop = len(s)
        i = 0
        j = 0
        subsequence_possible = False

        while i < max_range and max_loop > 0:
            if t[i] == s[j]:
                max_loop -= 1
                j += 1
            i += 1

        if max_loop == 0:
            subsequence_possible = True

        return subsequence_possible


if __name__ == "__main__":
    sol = Solution()

    # Example 1: valid subsequence
    assert sol.isSubsequence("abc", "ahbgdc") is True, "Failed on 'abc' in 'ahbgdc'"

    # Example 2: invalid subsequence (missing 'x')
    assert sol.isSubsequence("axc", "ahbgdc") is False, "Failed on 'axc' in 'ahbgdc'"

    # Wrong order of characters
    assert sol.isSubsequence("aec", "abcde") is False, "Failed on wrong character order"

    # Edge case: empty subsequence s (always True)
    assert sol.isSubsequence("", "ahbgdc") is True, "Failed on empty s"
    assert sol.isSubsequence("", "") is True, "Failed on both empty strings"

    # Edge case: non-empty s with empty target t
    assert sol.isSubsequence("a", "") is False, "Failed on non-empty s with empty t"

    # Identical strings
    assert sol.isSubsequence("abc", "abc") is True, "Failed on identical strings"

    print("All tests passed successfully!")
