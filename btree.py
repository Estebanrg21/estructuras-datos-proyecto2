from btree_node import Node


class Tree:
    def __init__(self, node):
        self.root = node

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        return 0 if not node else node.size

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if not key: raise Exception("get(): invalid key")
        if not node: return None
        if key != node.key:
            result = self._get(node.left, key)
            if not result:
                result = self._get(node.right, key)
            return result
        else:
            return node

    def get_parent_of_node(self, key_to_find):
        return self._get_parent_of_node(self.root, key_to_find)

    def _get_parent_of_node(self, parent_node: Node, key_to_find):
        if not parent_node: return None
        if parent_node.left:
            if key_to_find == parent_node.left.key:
                return 'L', parent_node
        if parent_node.right:
            if key_to_find == parent_node.right.key:
                return 'D', parent_node
        result = self._get_parent_of_node(parent_node.left, key_to_find)
        if not result:
            result = self._get_parent_of_node(parent_node.right, key_to_find)
        return result

    def determine_orientation(self, node1, node2):
        """ :returns parent Node if vertical orientation, so if horizontal then None"""
        result_node1 = self._get(node1, node2.key)
        result_node2 = None
        if not result_node1:
            result_node2 = self._get(node2, node1.key)
        if not result_node2 and not result_node1:
            return None
        elif result_node1:
            return node1
        elif result_node2:
            return node2

    def insert_into_node(self, parent_node, node, direction):
        if direction == 'L':
            parent_node.left = node
        if direction == 'D':
            parent_node.right = node

    def interchange_nodes(self, node1: Node, node2: Node):
        p1_dir, parent_node1 = self.get_parent_of_node(node1.key)
        p2_dir, parent_node2 = self.get_parent_of_node(node2.key)
        node = self.determine_orientation(node1, node2)
        if not node:
            self.insert_into_node(parent_node1, node2, p1_dir)
            self.insert_into_node(parent_node2, node1, p2_dir)
        else:
            if node == node1:
                self.insert_into_node(parent_node1, node2, p1_dir)
                self.insert_into_node(parent_node2, None,p2_dir)
                self._insert(node2,node1)
            if node == node2:
                self.insert_into_node(parent_node2, node1, p2_dir)
                self.insert_into_node(parent_node1, None, p1_dir)
                self._insert(node1, node2)

    def insert(self, node_to_insert):
        if not node_to_insert: raise Exception("insert(): invalid value")
        self.root = self._insert(self.root, node_to_insert)

    def _insert(self, parent_node, node_to_insert):
        if not parent_node: return node_to_insert
        if not parent_node.left:
            parent_node.left = node_to_insert
        elif not parent_node.right:
            parent_node.right = node_to_insert
        else:
            comparison = parent_node.left.size < parent_node.right.size
            if comparison:
                parent_node.left = self._insert(parent_node.left, node_to_insert)
            elif not comparison:
                parent_node.right = self._insert(parent_node.right, node_to_insert)
        parent_node.size = 1 + self._size(parent_node.left) + self._size(parent_node.right)
        return parent_node

    def insert_question(self, question, answer, node=None):
        node_check = self.get(question)
        if not node_check:
            question_node = Node(question, question, 2)
            question_node.right = Node(answer, answer, 1)
            if node:
                self._insert(node, question_node)
            else:
                self.insert(question_node)
        else:
            self._insert(node_check, Node(answer, answer, 1))

    def print(self):
        return self.root.display()
