import sys
sys.path.append('../src')

from tkinter import *
from TypeEnum import DataType
from TypeEnum import ResultType

class TestResultCell:
    def __init__(self, master, row, column, index, result):
        self.cell_frame = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        res = result[0]
        msg = result[1]
        res_lbl_color = 'green' if res == ResultType.PASSED else 'red'

        index_lbl = Label(self.cell_frame, text=str(index))
        index_lbl.grid(row=0, column=0, sticky='W')

        # Test result (passed, failed, etc)
        res_lbl = Label(self.cell_frame, text=res.name, width=30, foreground=res_lbl_color)
        res_lbl.grid(row=0, column=1, sticky='W')
        # ===============

        # if failed, show actual/expected output
        if res != ResultType.PASSED:
            msg_lbl = Label(self.cell_frame, text=msg, height=10, width=30, anchor="nw", justify='left')
            msg_lbl.grid(row=1, column=1, sticky='W')
        # ================
        self.cell_frame.grid(row=row, column=column, sticky="NSEW")

    def destroy(self):
        self.cell_frame.grid_forget()

    def getTestDataAndType(self):
        return {'input': [(self.input_entry1.get(), DataType[self.input_variable1.get()]),
                          (self.input_entry2.get(), DataType[self.input_variable2.get()]),
                          (self.input_entry3.get(), DataType[self.input_variable3.get()]),
                          (self.input_entry4.get(), DataType[self.input_variable4.get()])],
                'output': (self.output_entry.get(), DataType[self.output_variable.get()])}


if __name__ == "__main__":
    print('Test TestResultCell')
    root = Tk()
    t = TestResultCell(root, 0, 0, 1, (ResultType.FAILED,"Test Failed.\nYour output is : \n3\nThe expected output is :\n2"))
    root.mainloop()
