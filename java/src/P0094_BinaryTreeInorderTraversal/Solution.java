package P0094_BinaryTreeInorderTraversal;
import java.util.ArrayList;
import java.util.List;

class Solution {
    private void lookingForNode(TreeNode node, List<Integer> output) {
        if (node != null) {
            lookingForNode(node.left, output);
            output.add(node.val);
            lookingForNode(node.right, output);
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<>();
        lookingForNode(root, output);
        return output;
    }
}



