
QUESTION = 0
ANSWER = 1

class Node:
    def __init__(self, key, value, size, type):
        self.left = None
        self.right = None
        self.value = value
        self.key = key
        self.size = size
        self.type = type


def node_to_dict(node):
    node_dict = getattr(node, '__dict__').copy()
    node_dict.pop("size", None)
    node_dict.pop("type", None)
    node_dict.pop("value", None)
    if node:
        key = node_dict["key"]
        node_dict.pop("key", None)
        node_dict = {key: node_dict}
    return node_dict
