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

        buttons = [['', '7', '8', '9', '/'],
                   ['(', '4', '5', '6', '*'],
                   [')', '1', '2', '3', '-'],
                   ['+/-', '0', '', '.', '+']]

        def reset():    # This will reset the label to just '0'
            output.config(text='0')

        def delete():   # This will delete the last input
            if len(output['text']) > 1:
                new_output = output['text'][:-1]
                output.config(text=new_output)
            else:
                reset()

        def equals():   # Will show the result of the computation
            output.config(text=str(eval(output['text'])))

        def add_this(sign):     # Adds the pressed sign
            if sign == '+/-' and '-' in output['text']:
                output['text'] = output['text'][1:]
            elif sign == '+/-' and output['text'] != '0':
                output['text'] = '-' + output['text']
            elif output['text'] == '0' and sign != '+/-':
                output.config(text=sign)
            elif output['text'] == '0' and sign == '+/-':
                pass
            else:
                output['text'] += sign    

        stick = (tk.N, tk.E, tk.S, tk.W)

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
        label.grid(row=0, column=0, columnspan=5, sticky=stick)

        reset_button = tk.Button(main_frame, text='Reset', textvariable='Reset',
                                 fg='red', height=2, command=reset, bg='lavender')
        reset_button.grid(row=1, rowspan=2, column=0, padx=2, pady=2, sticky=stick)

        output = tk.Label(main_frame, text='0', anchor='e', relief='sunken', bg='lavender')
        output.grid(row=1, column=1, columnspan=3, padx=3, pady=3, sticky=stick)

        delete_button = tk.Button(main_frame, text='←', font=4, textvariable='←',
                                  height=2, command=delete, bg='lavender')
        delete_button.grid(row=1, column=4, columnspan=2, padx=2, pady=2, sticky=stick)

        equals_button = tk.Button(main_frame, text='=', textvariable='=',
                                  command=equals, height=3, bg='lavender')
        equals_button.grid(row=6, column=0, columnspan=5, padx=2, pady=2, sticky=stick)


window = tk.Tk()
MyCalc = CalcPy(window)

if __name__ == '__main__':
    window.mainloop()
