class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count_s_letters = {}
        count_t_letters = {}

        if len(s) == len(t):
            for letter_s, letter_t in zip(s, t):
                if letter_s in count_s_letters:
                    count_s_letters[letter_s] += 1
                else:
                    count_s_letters[letter_s] = 1
                if letter_t in count_t_letters:
                    count_t_letters[letter_t] += 1
                else:
                    count_t_letters[letter_t] = 1
            if count_s_letters == count_t_letters:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))
    print("All tests passed successfully!")
