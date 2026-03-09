# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Use DFS as it goes all the way then back up (depth first)
        result = []
        def DFS(node, path):
            if not node: # if node doesnt exist
                return
            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
            else:
                DFS(node.left, path + "->")
                DFS(node.right, path + "->")
        DFS(root, "")
        return result
