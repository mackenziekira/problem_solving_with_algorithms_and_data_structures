# TREE CHAPTER
################### SECTION 6.4 ######################

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# Q26 tree chapter: Write a function buildTree that returns a tree using the list of lists functions that looks like this: 
def buildTree():
    """selfcheck from tree chapter, Q26

    >>> print(buildTree())
    ['a', ['b', [], ['d', [], []]], ['c', ['e', [], []], ['f', [], []]]]
    """
    x = BinaryTree('a')
    insertLeft(x, 'b')
    insertRight(getLeftChild(x), 'd')
    insertRight(x, 'c')
    r = getRightChild(x)
    insertLeft(r, 'e')
    insertRight(r, 'f')
    return x

################### SECTION 6.5 ######################

class BinaryTree(object):
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.key)

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

def buildTree():
    """selfcheck from tree chapter, section 6.5

    >>> t = buildTree()
    >>> print(t)
    a

    >>> t.get_left_child()
    b

    >>> t.get_right_child()
    c

    >>> t.get_right_child().get_right_child()
    f

    >>> t.get_left_child().get_right_child()
    d

    >>> t.get_right_child().get_left_child()
    e

    """
    x = BinaryTree('a')
    x.insert_left(BinaryTree('b'))
    x.insert_right(BinaryTree('c'))
    l = x.get_left_child()
    r = x.get_right_child()
    l.insert_right(BinaryTree('d'))
    r.insert_right(BinaryTree('f'))
    r.insert_left(BinaryTree('e'))
    return x

################### SECTION 6.6 ######################

class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

def build_parse_tree(expression):
    expression_lst = expression.split()
    my_stack = Stack()
    expression_tree = BinaryTree('')
    my_stack.push(expression_tree)
    current_tree = expression_tree
    for item in expression_lst:
        if item == '(':
            current_tree.insert_left('')
            my_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif item not in {'+', '-', '*', '/', ')'}:
            current_tree.set_root_val(int(item))
            parent = my_stack.pop()
            current_tree = parent
        elif item in {'+', '-', '*', '/'}:
            current_tree.set_root_val(item)
            current_tree.insert_right('')
            my_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif item == ')':
            current_tree = my_stack.pop()
        else:
            raise ValueError

    return expression_tree

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")

import operator 
def evaluate(pt):
    if isinstance(pt.get_root_val(), int):
        return pt.get_root_val()
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    l = evaluate(pt.get_left_child())
    r = evaluate(pt.get_right_child())
    op = opers[pt.get_root_val()]
    return op(l, r)

print evaluate(pt)

# preorder traversal
def preorder(tree):
    if tree is not None:
        print(tree)
        preorder(tree.left_child)
        preorder(tree.right_child)

def postorder(tree):
    if tree is not None:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree)

def inorder(tree):
    if tree is not None:
        inorder(tree.left_child)
        print tree
        inorder(tree.right_child)

inorder(pt)

if __name__ == "__main__":
    import doctest
    doctest.testmod()