# class Node:
#     def __init__(self, data):
#         self.left= None
#         self.right= None
#         self.data= data
#
#     def Insert(self,data):
#             if root is None:
#                 if self.left is None:
#                    self.left = self.data
#
#                 else:
#                     self.right.insert(data)
#
#
# root = Node(1)
# root.Insert(3)
# root.Insert(5)
# root.Insert(6)
#
# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
# # Insert Node
#    def insert(self, data):
#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          else:
#             data > self.data
#             if self.right is None:
#                self.right = Node(data)
#             else:
#                self.right.insert(data)
#       else:
#          self.data = data
# # Print the Tree
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data),
#       if self.right:
#          self.right.PrintTree()
# # Inorder traversal
# # Left -> Root -> Right
#    def inorderTraversal(self, root):
#       res = []
#       if root:
#          res = self.inorderTraversal(root.left)
#          res.append(root.data)
#          res = res + self.inorderTraversal(root.right)
#       return res
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.inorderTraversal(root))

class Node:
    def __init__(self, label = True):
      #  self.data = data
        self.right = None
        self.left = None
        self.root = None
        self.label = True

    def rightnode(self, right):
        self.right = right

    def leftnode(self, left):
        self.left = left


# 14 nodes and root
# maybe automate this process so that it takes longer and shorter L
r = root = Node( False)
#accepting
r1 =root.left = Node( True)
r2 =root.left.left = Node( True)
r3 =root.left.left.left = Node( True)
r4 =root.left.left.right = Node( True)
r5 =root.left.right = Node( True)
#rejected
r6 =root.left.right.left = Node( False)
r7 =root.left.right.right = Node( False)
#accepting
r8 =root.right = Node( True)
r9 =root.right.right = Node(True)
r10 =root.right.right.left = Node( True)
r11 =root.right.left = Node( True)
r12 =root.right.left.left = Node( True )
# rejected
r13 =root.right.left.right = Node(False)
r14 =root.right.right.right = Node(False)

def mergenodes(mergablenode, uniquenodes):
    pass

unique_nodes = [1]
#
# def checklabelsofnodes(Node, uniquenodes):
#     #if unique_nodes.label == Node:
#     c = 1
#     for i in unique_nodes:
#         if i.label == Node.label:
#             mergenodes(i, unique_nodes)
#             c+=1
#         elif i.label != Node.label:
#             unique_nodes.append(i)


def checklabelsofsubtree(uniquenodes, node):
    pass
#    if Node.leftnode() = uniquenodes pass and
 #   Node.rightnode()= uniquenodes:

x = Node()
print (x.root.left)
#print(checklabelsofnodes(r2,unique_nodes))







