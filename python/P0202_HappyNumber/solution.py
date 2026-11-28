class Solution(object):

    def sum_of_squares(self, num):
        result = 0
        for char in str(num):
            digit = int(char)
            result += digit * digit
        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        searching_for_a_happy_number = True
        is_a_happy_number = False
        tortoise = n
        hare = n

        while searching_for_a_happy_number:
            tortoise = self.sum_of_squares(tortoise)
            hare = self.sum_of_squares(self.sum_of_squares(hare))

            if tortoise == 1 or hare == 1:
                searching_for_a_happy_number = False
                is_a_happy_number = True
            elif tortoise == hare:
                searching_for_a_happy_number = False
                is_a_happy_number = False

        return is_a_happy_number


if __name__ == "__main__":
    sol = Solution()

    # Example 1: happy number (19 -> 82 -> 68 -> 100 -> 1)
    assert sol.isHappy(19) is True, "Failed on 19 (expected True)"

    # Example 2: unhappy number entering a cycle
    assert sol.isHappy(2) is False, "Failed on 2 (expected False)"

    # Edge case: starting directly at 1
    assert sol.isHappy(1) is True, "Failed on 1 (expected True)"

    # Happy number reaching 1 in a single step
    assert sol.isHappy(10) is True, "Failed on 10 (expected True)"
    assert sol.isHappy(7) is True, "Failed on 7 (expected True)"

    # Unhappy numbers with multiple digits
    assert sol.isHappy(4) is False, "Failed on 4 (expected False)"
    assert sol.isHappy(116) is False, "Failed on 116 (expected False)"

    print("All tests passed successfully!")
