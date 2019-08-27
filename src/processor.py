import sys
sys.path.append('../UI')

from InputParser import InputParser
from TypeEnum import DataType
from TypeEnum import ResultType
from AnswerCheck import AnswerChecker

class Processor(object):
    def __init__(self, codeStr, is_res_any_order = False):
        self.inputs_list = []
        self.expected_res = None
        self.output_type = None
        self.is_res_any_order = is_res_any_order
        f = open("Solution.py", "w")
        f.write(codeStr)
        f.close()

    def setInputs(self, arg_list):
        self.inputs_list = []
        for arg in arg_list:
            if not arg[1] or arg[1] == DataType.UNKNOWN:
                continue
            self.inputs_list.append(InputParser.parseInput(arg[0],arg[1]))
        return self.inputs_list

    def setOutput(self, res):
        self.expected_res = None
        if not res[1] or res[1] == DataType.UNKNOWN:
            return self.expected_res
        self.expected_res = InputParser.parseInput(res[0], res[1])
        self.output_type = res[1]
        return self.expected_res

    def startTest(self):
        from Solution import Solution
        s = Solution()

        result = s.testFunc(*self.inputs_list)
        checker = AnswerChecker()
        return checker.check(result, self.expected_res, self.output_type, self.is_res_any_order)


if __name__ == '__main__':
    arg1 = ("[3,9,20,None,None,15,7]", DataType.TREE)
    arg2 = (None, DataType.UNKNOWN)
    arg3 = (None, DataType.UNKNOWN)
    arg4 = (None, DataType.UNKNOWN)
    arg5 = (None, DataType.UNKNOWN)
    arg6 = (None, DataType.UNKNOWN)
    arg7 = (None, DataType.UNKNOWN)
    arg8 = (None, DataType.UNKNOWN)
    ins = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8]
    out = ("[[3],[9,20],[15,7]]", DataType.LIST_OF_LIST)
    codeStr = ""
    f = open("testCode.txt", "r")
    codeStr = f.read()
    f.close()

    p = Processor(codeStr)
    print(p.setInputs(ins))
    print(p.setOutput(out))
    print(p.startTest())
