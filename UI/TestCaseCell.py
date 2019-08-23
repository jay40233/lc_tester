import sys
sys.path.append('../src')

from tkinter import *
from TypeEnum import DataType

class TestCaseCell:
    def __init__(self, master, row, column, index):
        self.cell_frame = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=2)

        index_lbl = Label(self.cell_frame, text=str(index))
        index_lbl.grid(row=0, column=0, sticky='E')

        self.input_variable1 = StringVar(self.cell_frame)
        self.input_variable2 = StringVar(self.cell_frame)
        self.input_variable3 = StringVar(self.cell_frame)
        self.input_variable4 = StringVar(self.cell_frame)
        self.output_variable = StringVar(self.cell_frame)
        datatype_lst = [e.name for e in DataType]
        self.input_variable1.set(datatype_lst[0])  # default value
        self.input_variable2.set(datatype_lst[0])  # default value
        self.input_variable3.set(datatype_lst[0])  # default value
        self.input_variable4.set(datatype_lst[0])  # default value
        self.output_variable.set(datatype_lst[0])  # default value

        # input data row
        self.input_datatype_dropdown1 = OptionMenu(self.cell_frame, self.input_variable1, *datatype_lst)
        self.input_datatype_dropdown1.grid(row=0, column=1, sticky="W")
        input_lbl1 = Label(self.cell_frame, text="Input arg 1 :")
        input_lbl1.grid(row=0, column=2, sticky='E')
        self.input_entry1 = Entry(self.cell_frame, width = 80)
        self.input_entry1.grid(row=0, column=3, sticky="WE")

        self.input_datatype_dropdown2 = OptionMenu(self.cell_frame, self.input_variable2, *datatype_lst)
        self.input_datatype_dropdown2.grid(row=1, column=1, sticky="W")
        input_lbl2 = Label(self.cell_frame, text="Input arg 2 :")
        input_lbl2.grid(row=1, column=2, sticky='E')
        self.input_entry2 = Entry(self.cell_frame, width=80)
        self.input_entry2.grid(row=1, column=3, sticky="WE")

        self.input_datatype_dropdown3 = OptionMenu(self.cell_frame, self.input_variable3, *datatype_lst)
        self.input_datatype_dropdown3.grid(row=2, column=1, sticky="W")
        input_lbl3 = Label(self.cell_frame, text="Input arg 3 :")
        input_lbl3.grid(row=2, column=2, sticky='E')
        self.input_entry3 = Entry(self.cell_frame, width=80)
        self.input_entry3.grid(row=2, column=3, sticky="WE")

        self.input_datatype_dropdown4 = OptionMenu(self.cell_frame, self.input_variable4, *datatype_lst)
        self.input_datatype_dropdown4.grid(row=3, column=1, sticky="W")
        input_lbl4 = Label(self.cell_frame, text="Input arg 4 :")
        input_lbl4.grid(row=3, column=2, sticky='E')
        self.input_entry4 = Entry(self.cell_frame, width=80)
        self.input_entry4.grid(row=3, column=3, sticky="WE")

        # ===============

        # output data row
        self.output_datatype_dropdown = OptionMenu(self.cell_frame, self.output_variable, *datatype_lst)
        self.output_datatype_dropdown.grid(row=4, column=1, sticky="W")
        output_lbl = Label(self.cell_frame, text="Expected Output :")
        output_lbl.grid(row=4, column=2, sticky='E')
        self.output_entry = Entry(self.cell_frame)
        self.output_entry.grid(row=4, column=3, sticky="WE")

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
    print('Test TestCaseCell')
    root = Tk()
    t = TestCaseCell(root)
    root.mainloop()
