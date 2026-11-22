package P0009_PalindromeNumber;

class Solution {
    public boolean isPalindrome(int x) {
        String initial_string = String.valueOf(x);
        boolean is_a_palindrome = true;
        int k = 0;
        int max_test = initial_string.length() -1;
        while (is_a_palindrome && k < max_test){
            if (initial_string.charAt(k) == initial_string.charAt(max_test)){
                k += 1;
                max_test -= 1;
            }
            else is_a_palindrome = false;
        }
        return is_a_palindrome;
    }
}
