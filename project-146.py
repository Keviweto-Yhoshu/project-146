# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:01:48 2022

@author: User
"""
from tkinter import*

root=Tk()

root.title("Fibonacci ")
root.geometry("400x400")

Input = Entry(root)
Input.place(relx=0.5, rely=0.4, anchor=CENTER)

f_s = Label(root)
f_s.place(relx=0.5, rely= 0.6, anchor=CENTER)

f_sum = Label(root)
f_sum.place(relx=0.5, rely=0.7, anchor=CENTER)

def fib_s_sum():
    input_no = int(Input.get())
    first_no=0
    second_no = 1
    sum1 =0
    sum2 =0
    
    counter = 1
    while(counter <= input_no):
        f_s["text"] += str(sum1) + " "
        counter= counter + 1
        first_no = second_no
        second_no = sum1
        sum1= first_no + second_no
        sum2 = sum2 + sum1

"""___________________________________________________________________________________"""

btn= Button(root, text ="Show Fibonacci Series", command=fib_s_sum)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
