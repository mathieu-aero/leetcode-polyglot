class Solution:
    def firstUniqChar(self, s: str) -> int:

        char_counts = {}
        still_looking_for_unique_char = True

        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        i = 0
        max_range = len(char_counts)
        result = -1
        my_keys = list(char_counts)

        while i < max_range and still_looking_for_unique_char:
            if char_counts[my_keys[i]] == 1:
                result = s.index(my_keys[i])
                still_looking_for_unique_char = False
            else:
                i += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))
    print(sol.firstUniqChar("loveleetcode"))
    print(sol.firstUniqChar("aabb"))
    print("All tests passed successfully!")