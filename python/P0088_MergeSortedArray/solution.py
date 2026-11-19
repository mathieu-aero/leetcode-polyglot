class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        if m == 0 and n == 1:
            nums1[0] = nums2[0]
        else:
            while k >= 0 and i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1

            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard merge (Example 1)
    nums1_1 = list((1, 2, 3, 0, 0, 0))
    sol.merge(nums1_1, 3, list((2, 5, 6)), 3)
    assert nums1_1 == list((1, 2, 2, 3, 5, 6)), f"Test 1 failed: got {nums1_1}"

    # Test 2: nums2 is empty (Example 2)
    nums1_2 = list((1,))
    sol.merge(nums1_2, 1, [], 0)
    assert nums1_2 == list((1,)), f"Test 2 failed: got {nums1_2}"

    # Test 3: nums1 has no initial elements (Example 3)
    nums1_3 = list((0,))
    sol.merge(nums1_3, 0, list((1,)), 1)
    assert nums1_3 == list((1,)), f"Test 3 failed: got {nums1_3}"

    # Test 4: All elements in nums2 are smaller than nums1
    nums1_4 = list((4, 5, 6, 0, 0, 0))
    sol.merge(nums1_4, 3, list((1, 2, 3)), 3)
    assert nums1_4 == list((1, 2, 3, 4, 5, 6)), f"Test 4 failed: got {nums1_4}"

    # Test 5: Minimal case with second while loop needed
    nums1_5 = list((2, 0))
    sol.merge(nums1_5, 1, list((1,)), 1)
    assert nums1_5 == list((1, 2)), f"Test 5 failed: got {nums1_5}"

    # Test 6: Negative numbers and zeros as real values
    nums1_6 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    sol.merge(nums1_6, 6, list((1, 2, 2)), 3)
    assert nums1_6 == [-1, 0, 0, 1, 2, 2, 3, 3, 3], f"Test 6 failed: got {nums1_6}"

    print("All tests passed successfully!")
