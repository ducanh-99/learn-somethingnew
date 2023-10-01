# Definition for a binary tree node.
from typing import Optional


def array_to_tree(arr, index, n):
    # Base case: If the current index is out of bounds or the element is None, return None.
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = array_to_tree(arr, 2 * index + 1, n)
        root.right = array_to_tree(arr, 2 * index + 2, n)
        return root
    return None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursive(root: TreeNode, min_value=float("-inf"), max_value=float("inf")):

            if root is None:
                return True
            val = root.val
            if val <= min_value or max_value <= val:
                return False
            return recursive(root.left, min_value, val) and recursive(root.right, val, max_value)


        return recursive(root)


arr = [5, 4, 6, None, None, 3, 7]
n = len(arr)

# Convert the array to a binary tree
root = array_to_tree(arr, 0, n)
print(Solution().isValidBST(root))
