class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        result = "".join(letter for letter in s if letter.isalnum()).lower()
        left = 0
        right = len(result) - 1
        is_a_palindrome = True

        while left <= right and is_a_palindrome:
            if result[left] == result[right]:
                left += 1
                right -= 1
            else:
                is_a_palindrome = False

        return is_a_palindrome


if __name__ == "__main__":
    sol = Solution()

    # Example 1: classic palindrome with punctuation, spaces, and mixed case
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True, "Failed on Panama palindrome"

    # Example 2: non-palindrome with spaces
    assert sol.isPalindrome("race a car") is False, "Failed on 'race a car'"

    # Example 3: empty string after removing non-alphanumeric characters
    assert sol.isPalindrome(" ") is True, "Failed on whitespace-only string"

    # Edge case: alphanumeric mix (digit + letter)
    assert sol.isPalindrome("0P") is False, "Failed on '0P' (digit vs letter)"

    # Numeric palindrome
    assert sol.isPalindrome("12321") is True, "Failed on numeric palindrome '12321'"

    # Single character and symbols only
    assert sol.isPalindrome("a") is True, "Failed on single character"
    assert sol.isPalindrome(".,!@#") is True, "Failed on symbols-only string"

    print("All tests passed successfully!")
