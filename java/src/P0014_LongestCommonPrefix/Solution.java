package P0014_LongestCommonPrefix;

class Solution {
    public String longestCommonPrefix(String[] strs) {

        boolean a_prefix_can_exist = true;
        int i = 1;
        String shortest_prefix = strs[0];

        while (i < strs.length && a_prefix_can_exist){
            int j = 0;
            boolean same_letter = true;
            while (j < shortest_prefix.length() && j < strs[i].length() && same_letter){
                if(strs[0].charAt(j) == strs[i].charAt(j)){
                    j += 1;
                }
                else same_letter = false;
            }
            shortest_prefix = shortest_prefix.substring(0, j);
            if (shortest_prefix.isEmpty()){
                a_prefix_can_exist = false;
            }
            i += 1;
        }
        return shortest_prefix;
    }
}