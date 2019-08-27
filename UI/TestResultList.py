import sys
sys.path.append('../src')

import tkinter as tk
from TestResultCell import TestResultCell
from TypeEnum import ResultType

# ************************
# Scrollable Frame Class
# ************************
class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")  # place canvas on self
        self.viewPort = tk.Frame(self.canvas,
                                 background="#ffffff")  # place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)  # place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set)  # attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)  # pack canvas to left of self and expand to fil
        self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",  # add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>",
                           self.onFrameConfigure)  # bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))  # whenever the size of the frame changes, alter the scroll region respectively.


class TestResultList(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)  # add a new scrollable frame.
        self.cell_count = 0
        self.cells = []

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def addTestResult(self, result):
        # Now add some controls to the scrollframe.
        # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
        self.cells.append(TestResultCell(self.scrollFrame.viewPort, self.cell_count, 0, self.cell_count+1, result))
        self.cell_count += 1

    def getTestInAndOut(self):
        return [self.cells[i].getTestDataAndType() for i in range(len(self.cells))]


if __name__ == "__main__":
    root = tk.Tk()
    t = TestResultList(root)
    t.pack(side="top", fill="both", expand=True)
    t.addTestResult((ResultType.PASSED, ""))
    t.addTestResult((ResultType.FAILED, "Test Failed.\nYour output is : \n3\nThe expected output is :\n2"))
    t.addTestResult((ResultType.FAILED, "Test Failed.\nYour output is : \n3\nThe expected output is :\n2"))
    t.addTestResult((ResultType.FAILED, "Test Failed.\nYour output is : \n3\nThe expected output is :\n2"))
    t.addTestResult((ResultType.FAILED, "Test Failed.\nYour output is : \n3\nThe expected output is :\n2"))
    root.mainloop()
