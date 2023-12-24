import tkinter

from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator

    first_number=(result_label['text'])
    operator = op
    result_label.config(text = '')

def get_result():
    global first_number,second_number,operator
    second_number = str(result_label['text'])
    if operator =='+':
        result_label.config(text=str(first_number + second_number))
    elif operator =='_':
        result_label.config(text=str(first_number-second_number))
    elif operator =='*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(first_number/second_number))

root = Tk()
root.title("calculator") # title is the name of the calculator (Calculator)
root.geometry('250x530') # fixing the size of the calculator
root.resizable(0,0) # checking its resizable or not
root.configure(background='black') # setting background colour of the calculator

result_label= Label(root, text= '', bg='black',fg='white')
result_label.grid(row=0, column=0, columnspan=7, pady=(60,45), sticky ='w')
result_label.config(font=('verdana', 30, 'bold'))

butn7 = Button(root,text='7', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(7))
butn7.grid(row=1,column=0)
butn7.config(font=('verdana',16))

butn8 = Button(root,text='8', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(8))
butn8.grid(row=1,column=1)
butn8.config(font=('verdana',16))

butn9 = Button(root,text='9', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(9))
butn9.grid(row=1,column=2)
butn9.config(font=('verdana',16))

butn_add = Button(root,text='+', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_operator('+'))
butn_add.grid(row=1,column=3)
butn_add.config(font=('verdana',16))

butn4 = Button(root,text='4', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(4))
butn4.grid(row=2,column=0)
butn4.config(font=('verdana',16))

butn5 = Button(root,text='5', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(5))
butn5.grid(row=2,column=1)
butn5.config(font=('verdana',16))

butn6 = Button(root,text='6', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(6))
butn6.grid(row=2,column=2)
butn6.config(font=('verdana',16))

butn_sub = Button(root,text='-', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_operator('-'))
butn_sub.grid(row=2,column=3)
butn_sub.config(font=('verdana',16))


butn1 = Button(root,text='1', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(1))
butn1.grid(row=3,column=0)
butn1.config(font=('verdana',16))

butn2 = Button(root,text='2', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(2))
butn2.grid(row=3,column=1)
butn2.config(font=('verdana',16))

butn3 = Button(root,text='3', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(3))
butn3.grid(row=3,column=2)
butn3.config(font=('verdana',16))

butn_mul = Button(root,text='*', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_operator('*'))
butn_mul.grid(row=3,column=3)
butn_mul.config(font=('verdana',16))


butn_clr = Button(root,text='C', bg='#00a65a', fg='white', width=4, height=3, command =lambda :clear())
butn_clr.grid(row=4,column=0)
butn_clr.config(font=('verdana',16))

butn0 = Button(root,text='0', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_digit(0))
butn0.grid(row=4,column=1)
butn0.config(font=('verdana',16))

butn_equal = Button(root,text='=', bg='#00a65a', fg='white', width=4, height=3, command =get_result)
butn_equal.grid(row=4,column=2)
butn_equal.config(font=('verdana',16))

butn_divide = Button(root,text='/', bg='#00a65a', fg='white', width=4, height=3, command=lambda :get_operator('/'))
butn_divide.grid(row=4,column=3)
butn_divide.config(font=('verdana',16))

root.mainloop()