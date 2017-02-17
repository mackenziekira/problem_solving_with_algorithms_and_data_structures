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

if __name__ == "__main__":
    import doctest
    doctest.testmod()