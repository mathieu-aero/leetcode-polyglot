class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1: n = 3 (includes Fizz)
    assert sol.fizzBuzz(3) == ["1", "2", "Fizz"], "Failed on n = 3"

    # Example 2: n = 5 (includes Fizz and Buzz)
    assert sol.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"], "Failed on n = 5"

    # Example 3: n = 15 (includes FizzBuzz)
    assert sol.fizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ], "Failed on n = 15"

    # Edge case: minimum constraint n = 1
    assert sol.fizzBuzz(1) == ["1"], "Failed on n = 1"

    print("All tests passed successfully!")
