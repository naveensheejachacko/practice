# # check is bst or not
# previous = None


# def isBST(root):
#     global previous
#     previous = None
#     return isBST_inorder(root)


# def isBST_inorder(root):
#     global previous
#     if root is None:
#         return True
#     if isBST_inorder(root.left) is False:
#         return False
#     if previous is not None and previous.data > root.data:
#         return False
#     previous = root
#     return isBST_inorder(root.right)


# # check for BST
# if(isBST(root)):
#    print("Binary Tree is BST")
# else:
#      print("Binary Tree is not Bst")


class TreeNode:
    def __init__(self, val,left = None,right = None):
        self.val = val
        self.left = None
        self.right = None

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    
    # Check if the current node's value is within the valid range
    if root.val <= min_val or root.val >= max_val:
        return False
    
    # Recursively check the left and right subtrees
    return (
        isBST(root.left, min_val, root.val) and
        isBST(root.right, root.val, max_val)
    )

# Example usage
# Construct your tree here
root = TreeNode(40)
root.left = TreeNode(30)
root.right = TreeNode(50)
root.left.left = TreeNode(25)
root.left.right = TreeNode(35)
root.right.left = TreeNode(45)
root.right.right = TreeNode(55)




# Call the function
is_bst = isBST(root)
if is_bst:
    print("The given tree is a Binary Search Tree.")
else:
    print("The given tree is not a Binary Search Tree.")
