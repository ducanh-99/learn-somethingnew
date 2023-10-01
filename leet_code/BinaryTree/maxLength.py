from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def array_to_tree(arr, index, n):
    # Base case: If the current index is out of bounds or the element is None, return None.
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = array_to_tree(arr, 2 * index + 1, n)
        root.right = array_to_tree(arr, 2 * index + 2, n)
        return root
    return None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is not None and q is None:
                return False
            if p is None and q is not None:
                return False
            if p.value != q.value:
                return False
            isSame(p.left, q.left)
            isSame(p.right, q.right)
            return True
        return isSame(p, q)


# Example array
arr = [3, 9, 20, None, None, 15, 7]
n = len(arr)

# Convert the array to a binary tree
root = array_to_tree(arr, 0, n)
print(Solution().isSameTree(
    p=array_to_tree([1, 2, 3], 0, 3),
    q=array_to_tree([1, 2, 3], 0, 3),

))
