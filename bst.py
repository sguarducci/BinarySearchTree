import random

class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.value = key
  
def insert(root, node):
  if root is None:
    root = node
  else:
    if node.value > root.value:
      if root.right is None:
        root.right = node
      else:
        insert(root.right, node)
    
    elif node.value < root.value or node.value == root.value:
      if root.left is None:
        root.left = node
      else:
        insert(root.left, node)

def inorder(root):
  if root.left is not None:
    inorder(root.left)
  print(root.value)
  if root.right is not None:
    inorder(root.right)
    

def search(root, key):
  if key < root.value:
    return search(root.left, key)

  elif key > root.value:
    return search(root.left, key)

  else:
    return root

r = Node(random.randint(1,10000))
for counter in range(1000):
  insert(r, Node(random.randint(1,10000)))

inorder(r)