package com.mathieu.leetcode;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.mergeAlternately("abc", "pqr"));   // Expected output: "apbqcr"
        System.out.println(solution.mergeAlternately("ab", "pqrs"));   // Expected output: "apbqrs"
        System.out.println(solution.mergeAlternately("abcd", "pq"));   // Expected output: "apbqcd"
    }
}
