from TypeEnum import DataType
from TypeEnum import ResultType


class AnswerChecker(object):
    def __init__(self):
        pass

    def check(self, result, expected_res, output_type, is_res_any_order):
        try:
            isPassed = False
            msg = ""
            if is_res_any_order:
                result.sort()
                expected_res.sort()
            if output_type in [DataType.LIST_OF_LIST, DataType.LIST, DataType.FLOAT, DataType.INTEGER, DataType.STRING]:
                isPassed = (result == expected_res)
            elif output_type == DataType.TREE:
                isPassed = (self._treeFlattener(result) == self._treeFlattener(expected_res))
            elif output_type == DataType.LINKED_LIST:
                isPassed = (self._linkedListFlattener(result) == self._linkedListFlattener(expected_res))

            if isPassed:
                return (ResultType.PASSED, msg)
            msg = "Your output is : \n{0}\nThe expected output is :\n{1}".format(result, expected_res)
            return (ResultType.FAILED, msg)
        except Exception as e:
            return (ResultType.ERROR, str(e))

    def _treeFlattener(self, node):
        if not node:
            return "N"
        l = self._treeFlattener(node.left)
        r = self._treeFlattener(node.right)
        return str(node.val)+l+r

    def _linkedListFlattener(self, node):
        res = ""
        while node:
            res += str(node.val)
            node = node.next
        return res