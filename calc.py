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

        def add_number():
            pass

        def add_op_parenth():
            pass

        def plus_minus():
            pass

        def add_comma():
            pass

        def divide():
            pass

        def multiply():
            pass

        def minus():
            pass

        stick = (tk.N, tk.E, tk.S, tk.W)

        reset_button = tk.Button(main_frame, text='Reset', fg='red', width=8, height=2, command=reset)
        reset_button.grid(row=1, rowspan=2, column=0, sticky=stick)

        output = tk.Label(main_frame, relief='sunken', width=30)
        output.grid(row=1, column=1, columnspan=3, padx=3, sticky=stick, pady=3)

        delete_button = tk.Button(main_frame, text='Delete', width=8, height=2, command=delete)
        delete_button.grid(row=1, column=4)

        open_parenth_button = tk.Button(main_frame, text='(', command=add_op_parenth, height=2)
        open_parenth_button.grid(row=3, column=0, sticky=stick)

        close_parenth_button = tk.Button(main_frame, text=')', command=add_op_parenth, height=2)
        close_parenth_button.grid(row=4, column=0, sticky=stick)

        # for i in range(1, 10):
        one_button = tk.Button(main_frame, text='1', command=add_number, height=2)
        one_button.grid(row=2, column=1, sticky='we')

        two_button = tk.Button(main_frame, text='2', command=add_number, height=2)
        two_button.grid(row=2, column=2, sticky='we')

        three_button = tk.Button(main_frame, text='3', command=add_number, height=2)
        three_button.grid(row=2, column=3, sticky='we')

        four_button = tk.Button(main_frame, text='4', command=add_number, height=2)
        four_button.grid(row=3, column=1, sticky='we')

        five_button = tk.Button(main_frame, text='5', command=add_number, height=2)
        five_button.grid(row=3, column=2, sticky='we')

        six_button = tk.Button(main_frame, text='6', command=add_number, height=2)
        six_button.grid(row=3, column=3, sticky='we')

        seven_button = tk.Button(main_frame, text='7', command=add_number, height=2)
        seven_button.grid(row=4, column=1, sticky='we')

        eight_button = tk.Button(main_frame, text='8', command=add_number, height=2)
        eight_button.grid(row=4, column=2, sticky='we')

        nine_button = tk.Button(main_frame, text='9', command=add_number, height=2)
        nine_button.grid(row=4, column=3, sticky='we')

        zero_button = tk.Button(main_frame, text='0', command=add_number, height=2)
        zero_button.grid(row=5, column=1, columnspan=2, sticky='we')

        plus_minus_button = tk.Button(main_frame, text='+/-', command=plus_minus)
        plus_minus_button.grid(row=5, column=0, sticky=stick)

        comma_button = tk.Button(main_frame, text='.', command=add_comma)
        comma_button.grid(row=5, column=3, sticky=stick)

        divide_button = tk.Button(main_frame, text='/', command=divide)
        divide_button.grid(row=2, column=4, sticky=stick)

        multiply_button = tk.Button(main_frame, text='*', command=multiply)
        multiply_button.grid(row=3, column=4, sticky=stick)

        minus_button = tk.Button(main_frame, text='-', command=minus)
        minus_button.grid(row=4, column=4, sticky=stick)

        add_button


window = tk.Tk()
MyCalc = CalcPy(window)

if __name__ == '__main__':
    window.mainloop()
