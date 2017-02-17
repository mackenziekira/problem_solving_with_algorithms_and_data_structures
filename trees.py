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

    def insertLeft(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

if __name__ == "__main__":
    import doctest
    doctest.testmod()