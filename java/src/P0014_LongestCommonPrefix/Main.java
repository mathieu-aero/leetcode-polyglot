package P0014_LongestCommonPrefix;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestCommonPrefix(new String[]{"flower", "flow", "flight"}));
        System.out.println(sol.longestCommonPrefix(new String[]{"dog", "racecar", "car"}));
        System.out.println(sol.longestCommonPrefix(new String[]{"python", "java", "csharp", "cpp"}));
        System.out.println(sol.longestCommonPrefix(new String[]{"code", "code", "code"}));
        System.out.println(sol.longestCommonPrefix(new String[]{"flower", "", "flow"}));
        System.out.println("All tests passed successfully!");
    }
}

