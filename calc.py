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

        def reset():    # This will reset the label to just '0'
            output.config(text='0')

        def delete():   # This will delete the last input
            pass

        def equals():   # Will show the result of the computation
            pass

        def add_this(sign):     # Adds the pressed sign
            if output['text'] == '0':
                output.config(sign)
            else:
                output['text'] += sign

        def show():     # Will be executed on every buttonpress to show
            pass

        def execute_this(op):   # Executing the chosen operation
            pass

        def memory():
            pass

        stick = (tk.N, tk.E, tk.S, tk.W)

        buttons = [['', '7', '8', '9', '/', 'mem'],
                   ['(', '4', '5', '6', '*', 'x**2'],
                   [')', '1', '2', '3', '-', 'π'],
                   ['+/-', '0', '', '.', '+', 'root']]

        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                if not buttons[i][j]:
                    pass
                elif buttons[i][j] == '0':
                    btn = tk.Button(main_frame, text=buttons[i][j], bg='lavender',
                                    command=lambda name=buttons[i][j]: add_this(name), height=2)
                    btn.grid(row=i + 2, column=j, columnspan=2, padx=2, pady=2, sticky=stick)
                else:
                    btn = tk.Button(main_frame, textvariable=buttons[i][j], text=buttons[i][j],
                                    width=8, bg='lavender', height=2,
                                    command=lambda name=buttons[i][j]: add_this(name))
                    btn.grid(row=i + 2, column=j, padx=2, pady=2, sticky=stick)

        label = tk.Label(main_frame, text='Calculator', height=3, font=4, bg='lavender')
        label.grid(row=0, column=0, columnspan=6, sticky=stick)

        reset_button = tk.Button(main_frame, text='Reset', textvariable='Reset',
                                 fg='red', height=2, command=reset, bg='lavender')
        reset_button.grid(row=1, rowspan=2, column=0, padx=2, pady=2, sticky=stick)

        output = tk.Label(main_frame, text='5', anchor='e', relief='sunken', bg='lavender')
        output.grid(row=1, column=1, columnspan=3, padx=3, pady=3, sticky=stick)

        delete_button = tk.Button(main_frame, text='←', font=4, textvariable='←',
                                  height=2, command=delete, bg='lavender')
        delete_button.grid(row=1, column=4, columnspan=2, padx=2, pady=2, sticky=stick)

        equals_button = tk.Button(main_frame, text='=', textvariable='=',
                                  command=equals, height=3, bg='lavender')
        equals_button.grid(row=6, column=0, columnspan=6, padx=2, pady=2, sticky=stick)


window = tk.Tk()
MyCalc = CalcPy(window)

if __name__ == '__main__':
    window.mainloop()
