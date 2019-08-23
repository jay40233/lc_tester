class Solution(object):
    def testFunc(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tree = [root]
        out= [[root.val]]
        while tree:
            temp = []
            record = []
            for node in tree:
                if node.left:
                    temp.append(node.left)
                    record.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    record.append(node.right.val)
            tree = temp
            if record:
                out.append(record)
        return out
