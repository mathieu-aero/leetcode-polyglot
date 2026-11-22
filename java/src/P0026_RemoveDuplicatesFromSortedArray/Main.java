package P0026_RemoveDuplicatesFromSortedArray;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] test1 = new int[]{1, 1, 2};
        int k1 = sol.removeDuplicates(test1);
        System.out.println("Dans le tableau " + Arrays.toString(test1) + " il y a " + k1 + " valeurs différentes." );

        int[] test2 = new int[]{0, 0, 1, 1, 2, 2, 3, 3, 4};
        int k2 = sol.removeDuplicates(test2);
        System.out.println("Dans le tableau " + Arrays.toString(test2) + " il y a " + k2 + " valeurs différentes." );

        int[] test3 = new int[] {1, 1, 2};
        int k3 = sol.removeDuplicates(test3);
        System.out.println("Dans le tableau " + Arrays.toString(test3) + " il y a " + k3 + " valeurs différentes." );

        int[] test4 = new int[] {1, 2, 3, 3};
        int k4 = sol.removeDuplicates(test4);
        System.out.println("Dans le tableau " + Arrays.toString(test4) + " il y a " + k4 + " valeurs différentes." );

        System.out.println("All tests passed successfully!");
    }
}
