import tkinter as tk
from tkinter import *
from tkinter import ttk

calculation=""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        pass

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
    
root = tk.Tk()
root.geometry("300x275")
root.title('Calculator')
text_result=tk.Text(root,height=2,width=20, font=("Arial",20),bg='gray')
text_result.grid(columnspan=5)

btn_1=tk.Button(root, text="1", command=lambda: add_to_calculation(1),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_1.grid(row=2, column=1)

btn_2=tk.Button(root, text="2", command=lambda: add_to_calculation(2),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_2.grid(row=2, column=2)

btn_3=tk.Button(root, text="3", command=lambda: add_to_calculation(3),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_3.grid(row=2, column=3)

btn_4=tk.Button(root, text="4", command=lambda: add_to_calculation(4),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_4.grid(row=3, column=1)

btn_5=tk.Button(root, text="5", command=lambda: add_to_calculation(5),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_5.grid(row=3, column=2)

btn_6=tk.Button(root, text="6", command=lambda: add_to_calculation(6),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_6.grid(row=3, column=3)

btn_7=tk.Button(root, text="7", command=lambda: add_to_calculation(7),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_7.grid(row=4, column=1)

btn_8=tk.Button(root, text="8", command=lambda: add_to_calculation(8),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_8.grid(row=4, column=2)

btn_9=tk.Button(root, text="9", command=lambda: add_to_calculation(9),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_9.grid(row=4, column=3)

btn_0=tk.Button(root, text="0", command=lambda: add_to_calculation(0),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_0.grid(row=5, column=2)

btn_plus=tk.Button(root, text="+", command=lambda: add_to_calculation("+"),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_plus.grid(row=2, column=4)

btn_min=tk.Button(root, text="-", command=lambda: add_to_calculation("-"),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_min.grid(row=3, column=4)

btn_mul=tk.Button(root, text="*", command=lambda: add_to_calculation("*"),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_mul.grid(row=4, column=4)

btn_div=tk.Button(root, text="/", command=lambda: add_to_calculation("/"),width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_div.grid(row=5, column=4)

btn_equ=tk.Button(root, text="=", command= evaluate_calculation,width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_equ.grid(row=5, column=3)

btn_clr=tk.Button(root, text="Clr", command=clear_field ,width=5,font="Arial,14",bd=5,bg='deepskyblue', fg='black')
btn_clr.grid(row=6, column=2)

btn_poi=tk.Button(root, text=".", command=lambda: add_to_calculation("."),width=5,font="Arial,20'bold'",bd=5,bg='deepskyblue', fg='black')
btn_poi.grid(row=5, column=1)

root.mainloop()