from display_node import NodeDisplay


class Node(NodeDisplay):
    def __init__(self, key, value, size):
        NodeDisplay.__init__(self, key)
        self.left = None
        self.right = None
        self.value = value
        self.key = key
        self.size = size
