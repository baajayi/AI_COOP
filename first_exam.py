# class TreeNode:
#     def __init__(self, value, left = None, right = None):
#         self.left = left
#         self.right = right
#         self.value = value
        
# def find_max(root):
#     if root == None:
#         return float("-inf")
#     max_root=root.value
#     left_max=find_max(root.left)
#     right_max=find_max(root.right)
    
#     return max(max_root, left_max, right_max)

# perfect_tree = TreeNode(11,TreeNode(4, TreeNode(100), TreeNode(1)),
#                                TreeNode(-2, TreeNode(99), TreeNode(-101)))
# unbalanced_tree = TreeNode(54, TreeNode(4, TreeNode(-10, TreeNode(2, None, TreeNode(9)), TreeNode(45)), TreeNode(1)))

# print(find_max(perfect_tree))
# print(find_max(unbalanced_tree))

# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# def preOrder(root):
#     if root is None:
#         return []
    
#     result = []
#     result.append(root.data)
#     result.extend(preOrder(root.left))
#     result.extend(preOrder(root.right))
    
#     return result

# def inOrder(root):
#     if root is None:
#         return []
    
#     result = []
#     result.extend(inOrder(root.left))
#     result.append(root.data)
#     result.extend(inOrder(root.right))
    
#     return result

# def postOrder(root):
#     if root is None:
#         return []
    
#     result = []
#     result.extend(postOrder(root.left))
#     result.extend(postOrder(root.right))
#     result.append(root.data)
    
#     return result

# a = Node(5)
# b = Node(10)
# c = Node(2)
# d = Node("leaf")
# a.left = b
# a.right = c
# c.left = d

# print(preOrder(a)) #[a.data, b.data, c.data, d.data]
# print(preOrder(b)) # [b.data]
# print(preOrder(c)) #, [c.data, d.data]
# print(preOrder(None))


def count_developers(lst):
    count=0
    for i in lst:
        program=i["language"]
        continent=i["continent"]
        if program=="JavaScript" and continent=="Europe":
            count+=1
    return count
def greet_developers(lst): 
    for i in lst:
        i['greeting']=f"Hi {i['firstName']}, what do you like the most about {i['language']}?"
    return lst

print(greet_developers([
          { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
          { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
          { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
          { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        ]))

print(count_developers([
          { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
          { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
        ]))

# Matrix Creation
def get_matrix(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix
    pass
print(get_matrix(3))
def some_not(seq, pred):
     return any(pred(x) for x in seq) and not all(pred(x) for x in seq)
print(some_not('abcdefg&%$', str.isalpha))