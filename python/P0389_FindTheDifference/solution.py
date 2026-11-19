class Solution:
    def findTheDifference(self, s, t):
        i = 0
        max_range = len(s)
        count_char = {}
        still_looking_for_difference = True
        result = ""

        while i < max_range:
            if s[i] in count_char:
                count_char[s[i]] += 1
            else:
                count_char[s[i]] = 1
            i += 1

        i = 0
        while i < max_range and still_looking_for_difference:
            if t[i] in count_char:
                if count_char[t[i]] == 0:
                    result = t[i]
                    still_looking_for_difference = False
                else:
                    count_char[t[i]] -= 1
                    i += 1
            else:
                result = t[i]
                still_looking_for_difference = False

        if result == "":
            result = t[i]

        return result

        # Test 1: Added letter at the end (Example 1)
        res_1 = sol.findTheDifference("abcd", "abcde")
        assert res_1 == "e", f"Test 1 failed: got '{res_1}'"

        # Test 2: Empty string s (Example 2)
        res_2 = sol.findTheDifference("", "y")
        assert res_2 == "y", f"Test 2 failed: got '{res_2}'"

        # Test 3: Shuffled string with new letter at the beginning
        res_3 = sol.findTheDifference("abc", "zabc")
        assert res_3 == "z", f"Test 3 failed: got '{res_3}'"

        # Test 4: Shuffled string with duplicate letter
        res_4 = sol.findTheDifference("ae", "aea")
        assert res_4 == "a", f"Test 4 failed: got '{res_4}'"

        # Test 5: Duplicate letter at the beginning
        res_5 = sol.findTheDifference("ab", "bba")
        assert res_5 == "b", f"Test 5 failed: got '{res_5}'"

        print("All tests passed successfully!")