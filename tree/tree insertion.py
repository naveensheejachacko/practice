class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val<key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end =" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.val,end = " ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end = " ")
if __name__ == '__main__':
    r = Node(20)
    r1 = insert(r,23)
    r2 = insert(r,2)
    r3 = insert(r,1)
    r4 = insert(r,5)
    r5 = insert(r,25)

    print("inorder\n")
    inorder(r)
    print("\n")
    print("preorder\n")
    preorder(r)
    print("\n")
    print("postorder\n")
    postorder(r)