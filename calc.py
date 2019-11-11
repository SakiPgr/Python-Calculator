#! python3
import tkinter as tk
# import math

# First thing I want to do is creating the layout of the calculator
# The functionality will come later. As soon as I'm happy with the layout


class CalcPy:

    def __init__(self, master):
        self.master = master
        master.title('Calculator')

        window_position_right = int(master.winfo_screenwidth() / 2 - 500 / 2)
        window_position_down = int(master.winfo_screenheight() / 2 - 300 / 2)

        master.geometry('+{}+{}'.format(window_position_right, window_position_down))

        main_frame = tk.Frame(master)
        main_frame.pack(fill=tk.BOTH)

        def reset():
            pass

        def delete():
            pass

        def add_one():
            pass

        def add_op_parenth():
            pass

        reset_button = tk.Button(main_frame, text='Reset', fg='red', width=8, command=reset)
        reset_button.grid(row=1, rowspan=2, column=0)

        output = tk.Entry(main_frame)
        output.grid(row=1, column=1, columnspan=3, sticky='e', padx=3)

        delete_button = tk.Button(main_frame, text='Delete', width=8, command=delete)
        delete_button.grid(row=1, column=5)

        open_parenth_button = tk.Button(main_frame, text='(', command=add_op_parenth)
        open_parenth_button.grid(row=3, column=0, sticky='ew')

        one_botton = tk.Button(main_frame, text='1', command=add_one)
        one_botton.grid(row=2, column=2, sticky='ew')


window = tk.Tk()
MyCalc = CalcPy(window)

if __name__ == '__main__':
    window.mainloop()
