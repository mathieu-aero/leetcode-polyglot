class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        word1_length = len(word1)
        word2_length = len(word2)
        rtype = []
        end_for_loop = min(word1_length, word2_length)
        for i in range(end_for_loop):
            rtype.append(word1[i])
            rtype.append(word2[i])

        rtype.append(word2[end_for_loop:])
        rtype.append(word1[end_for_loop:])
        return "".join(rtype)


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))   # Expected: "apbqcr"
    print(sol.mergeAlternately("ab", "pqrs"))   # Expected: "apbqrs"
    print(sol.mergeAlternately("abcd", "pq"))   # Expected: "apbqcd"