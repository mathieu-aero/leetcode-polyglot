class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a_prefix_can_exist = True
        i = 1
        shortest_prefix = strs[0]

        while i < len(strs) and a_prefix_can_exist:
            j = 0
            same_letter = True
            while j < len(shortest_prefix) and j < len(strs[i]) and same_letter:
                if strs[0][j] == strs[i][j]:
                    j += 1
                else:
                    same_letter = False
            shortest_prefix = shortest_prefix[:j]
            if shortest_prefix == "":
                a_prefix_can_exist = False
            i += 1
        return shortest_prefix


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix(["python", "java", "csharp", "cpp"]))
    print(sol.longestCommonPrefix(["code", "code", "code"]))
    print(sol.longestCommonPrefix(["flower", "", "flow"]))
    print("All tests passed successfully!")