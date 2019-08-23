import sys
sys.path.append('../src')

from tkinter import *
from TypeEnum import DataType

class TestCaseCell:
    def __init__(self, master, row, column):
        self.cell_frame = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_variable = StringVar(self.cell_frame)
        output_variable = StringVar(self.cell_frame)
        datatype_lst = [e.name for e in DataType]
        self.current_datatype = datatype_lst[0]
        input_variable.set(self.current_datatype)  # default value
        output_variable.set(self.current_datatype)  # default value

        # input data row
        self.input_datatype_dropdown = OptionMenu(self.cell_frame, input_variable, *datatype_lst)
        self.input_datatype_dropdown.grid(row=0, column=0, sticky="W")

        input_lbl = Label(self.cell_frame, text="Input Test Data :")
        input_lbl.grid(row=0, column=1, sticky='E')
        self.input_entry = Entry(self.cell_frame, width = 80)
        self.input_entry.grid(row=0, column=2, sticky="WE")

        # ===============

        # output data row
        self.output_datatype_dropdown = OptionMenu(self.cell_frame, output_variable, *datatype_lst)
        self.output_datatype_dropdown.grid(row=1, column=0, sticky="W")
        output_lbl = Label(self.cell_frame, text="Expected Output :")
        output_lbl.grid(row=1, column=1, sticky='E')
        self.output_entry = Entry(self.cell_frame)
        self.output_entry.grid(row=1, column=2, sticky="WE")

        # ================
        self.cell_frame.grid(row=row, column=column, sticky="NSEW")

    def destroy(self):
        self.cell_frame.grid_forget()


if __name__ == "__main__":
    print('Test TestCaseCell')
    root = Tk()
    t = TestCaseCell(root)
    root.mainloop()
