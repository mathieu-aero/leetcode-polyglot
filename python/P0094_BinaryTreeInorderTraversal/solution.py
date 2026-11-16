from tree_node import TreeNode

class Solution(object):

    def looking_for_node(self, node, output):
        if node:
            self.looking_for_node(node.left, output)
            output.append(node.val)
            self.looking_for_node(node.right, output)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        output = []
        self.looking_for_node(root, output)
        return output


if __name__ == "__main__":
    sol = Solution()
    tree_node1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    tree_node2 =  TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        TreeNode(3, None, TreeNode(8, TreeNode(9)))
    )


    print(sol.inorderTraversal(tree_node1))
    print(sol.inorderTraversal(tree_node2))
    print("All tests passed successfully!")