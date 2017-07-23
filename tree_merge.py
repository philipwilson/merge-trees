

class Node():
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        return 'Node(left = %s, right = %s, data = %s)' % (repr(self.left), repr(self.right), repr(self.data))

class Tree():
    def __init__(self, nodes=None):
        if nodes:
            self.root = nodes
        else:
            self.root = Node()

    def __repr__(self):
        return 'Tree(nodes = %s)' %  (repr(self.root))


    """  Well, our toy tree is a collection, so it should be iterable....
    """

    def __iter__(self, branch=None):
        branch = branch or self.root

        if branch.left:
            yield from self.__iter__(branch.left)

        yield branch.data

        if branch.right:
            yield from self.__iter__(branch.right)


    """  Print self for visual debugging only
    """

    def print_self(self, branch=None, depth=0):
        branch = branch or self.root

        if branch.left:
            self.print_self(branch.left, depth + 1)

        print('-' * depth +  ' ' + str(branch.data))

        if branch.right:
            self.print_self(branch.right, depth + 1)

    
    def add_node(self, branch, new_node):
        if new_node.data < branch.data:
            if branch.left is None:
                branch.left = new_node
            else:
                self.add_node(branch.left, new_node)
        else:
            if branch.right is None:
                branch.right = new_node
            else:
                self.add_node(branch.right, new_node)

    def add(self, data):
        if not self.root.data:
            self.root.data = data

        else:
            self.add_node(self.root, Node(data=data))


"""  Merge two sorted lists into a single sorted list (in linear time)
"""

def merge_lists(first, second):
    merged = []
    while first or second:
        if first and second:
            source = first if first[0] < second[0] else second
            merged.append(source.pop(0))
        else:
            remaining = first if first else second
            merged.extend(remaining)
            return merged


"""  Build a balanced binary tree from a sorted list recursively; this runs in O(n)
"""

def tree_from_list(node, data_list):

    """ Add middle datum to current node
    """
    
    midpoint = int(len(data_list)/2)
    node.data = data_list[midpoint]


    """ If data remains to the left or right in the sorted list, add new node(s) for it then recurse 
    """
    
    
    left_data = data_list[: midpoint]
    right_data = data_list[midpoint + 1 : ]

    if left_data:
        node.left = Node()
        tree_from_list(node.left, left_data)

    if right_data:
        node.right = Node()
        tree_from_list(node.right, right_data)


def merge_trees(first, second):
    merged_list = merge_lists([x for x in first], [x for x in second])

    root = Node()
    tree_from_list(root, merged_list)

    return Tree(root)
    

def demo():
    first_unbalanced = Tree()
    second_unbalanced = Tree()

    for i in range(1, 6):
        first_unbalanced.add(i)

    for i in range(6, 21):
        second_unbalanced.add(i)

    print("first tree:")
    first_unbalanced.print_self()
    print("second tree:")
    second_unbalanced.print_self()
    
    merged_balanced = merge_trees(first_unbalanced, second_unbalanced)

    print("merged tree:")

    merged_balanced.print_self()
    print(",".join(str(x) for x in merged_balanced))


demo()
