package P0020_ValidParentheses;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("()"));
        System.out.println(sol.isValid("(]"));
        System.out.println(sol.isValid("([])"));
        System.out.println(sol.isValid("([)]"));
        System.out.println(sol.isValid("((("));
        System.out.println(sol.isValid("((())"));

        System.out.println("All tests Leetcode 20 passed successfully!");
    }
}
