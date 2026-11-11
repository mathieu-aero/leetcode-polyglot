package com.mathieu.leetcode;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder mergedString = new StringBuilder();
        int lengthWord1 = word1.length();
        int lengthWord2 = word2.length();
        int i = 0;
        int j = 0;
        while ((i <lengthWord1) || (j < lengthWord2)){
            if (i < lengthWord1){
                mergedString.append(word1.charAt(i));
                i++;
            }
            if (j < lengthWord2){
                mergedString.append(word2.charAt(j));
                j++;
            }
        }
        return mergedString.toString();
    }
}