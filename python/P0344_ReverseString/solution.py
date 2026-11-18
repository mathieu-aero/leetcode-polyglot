class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        max_range = len(s)//2
        temp = ''

        for i in range(max_range):
            temp = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = temp


if __name__ == "__main__":
    sol = Solution()

    test_1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(test_1)
    assert test_1 == ["o", "l", "l", "e", "h"], f"Test 1 failed: got {test_1}"

    # Test 2: Even length
    test_even = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(test_even)
    assert test_even == ["h", "a", "n", "n", "a", "H"], f"Test 2 failed: got {test_even}"

    # Test 3: Single character
    test_single = ["A"]
    sol.reverseString(test_single)
    assert test_single == ["A"], f"Test 3 failed: got {test_single}"

    # Test 4: Empty list
    test_empty = []
    sol.reverseString(test_empty)
    assert test_empty == [], f"Test 4 failed: got {test_empty}"

    print("All tests passed successfully!")