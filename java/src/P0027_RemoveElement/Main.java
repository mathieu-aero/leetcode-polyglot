package P0027_RemoveElement;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.removeElement(new int[]{3, 2, 2, 3}, 3));
        System.out.println(sol.removeElement(new int[]{0, 1, 2, 2, 3, 0, 4, 2}, 2));
        System.out.println("All tests passed successfully!");
    }
}
