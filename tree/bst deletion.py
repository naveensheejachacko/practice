class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
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
def preorder(root):
    if root:
        print(root.val,end = " ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end = " ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end =" ")

def delete_node(root,key):
    if root is None:
        return root
    if key<root.val:
        root.left = delete_node(root.left,key)
    elif key>root.val:
        root.right = delete_node(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_node(root.right)
        root.val = temp.val
        root.right = delete_node(root.right,temp.val)
    return root
def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

if __name__ == '__main__':
    r = Node(100)
    r = insert(r,20)
    r = insert(r,200)
    r = insert(r,10)
    r= insert(r,30)
    r = insert(r,150)
    r = insert(r,300)
    print("preorder/n")
    postorder(r)
    root =  delete_node(r,30)
    print()
    print("after deletion:")
    postorder(r)

