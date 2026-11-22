package P0094_BinaryTreeInorderTraversal;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Example 1 : [1, null, 2, 3] -> Expected result: [1, 3, 2]
        TreeNode treeNode1 = new TreeNode(
                1,
                null,
                new TreeNode(2, new TreeNode(3), null)
        );

        // Example 2 : [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9] -> Expected result: [4, 2, 6, 5, 7, 1, 3, 9, 8]
        TreeNode treeNode2 = new TreeNode(
                1,
                new TreeNode(2, new TreeNode(4), new TreeNode(5, new TreeNode(6), new TreeNode(7))),
                new TreeNode(3, null, new TreeNode(8, new TreeNode(9), null))
        );

        // Example 3 : Empty tree [] -> Expected result: []
        TreeNode treeNode3 = null;

        // Example 4 : Only one node [1] -> Expected result: [1]
        TreeNode treeNode4 = new TreeNode(1);

        System.out.println(sol.inorderTraversal(treeNode1));
        System.out.println(sol.inorderTraversal(treeNode2));
        System.out.println(sol.inorderTraversal(treeNode3));
        System.out.println(sol.inorderTraversal(treeNode4));
        System.out.println("All tests passed successfully!");
    }
}


