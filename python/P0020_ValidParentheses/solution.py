class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_length = len(s)
        pairs = {'(': ')', '[': ']', '{': '}'}
        pile = []
        still_valid = True
        i = 0

        if max_length % 2 == 0:
            while i < max_length and still_valid:
                char = s[i]
                if char in pairs:
                    pile.append(pairs[char])
                else:
                    if pile and pile[-1] == char:
                        pile.pop()
                    else:
                        still_valid = False
                i += 1
            return still_valid and len(pile) == 0
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("(]"))
    print(sol.isValid("([])"))
    print(sol.isValid("([)]"))
    print(sol.isValid("((("))
    print(sol.isValid("((())"))
    print("All tests Leetcode 20 passed successfully!")