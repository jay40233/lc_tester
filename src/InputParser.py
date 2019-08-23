import ast
import collections
from TypeEnum import DataType


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class InputParser(object):
    @staticmethod
    def parseInput(data, dataType):
        res = None
        if dataType == DataType.LIST_OF_LIST:
            res = ast.literal_eval(data)
        elif dataType == DataType.LIST:
            res = ast.literal_eval(data)
        elif dataType == DataType.STRING:
            res = data
        elif dataType == DataType.INTEGER:
            res = int(data)
        elif dataType == DataType.FLOAT:
            res = float(data)
        elif dataType == DataType.TREE:
            res = ParserUtils.treeDeserializer(ast.literal_eval(data))
        elif dataType == DataType.LINKED_LIST:
            res = ParserUtils.buildLinkedList(ast.literal_eval(data))
        return res


class ParserUtils(object):
    @staticmethod
    def treeDeserializer(node_list):
        q = collections.deque(node_list)
        res = collections.deque([])
        root = None
        while q:
            if not root:
                cur_val = q.popleft()
                root = TreeNode(cur_val)
                res.append(root)
                continue
            cur_node = res.popleft()
            if q:
                next_left_val = q.popleft()
                if next_left_val:
                    next_left = TreeNode(next_left_val)
                    cur_node.left = next_left
                    res.append(next_left)
            if q:
                next_right_val = q.popleft()
                if next_right_val:
                    next_right = TreeNode(next_right_val)
                    cur_node.right = next_right
                    res.append(next_right)
        return root

    @staticmethod
    def buildLinkedList(node_list):
        head = LinkNode(-1)
        cur = head
        for n in node_list:
            cur.next = LinkNode(n)
        return head.next
