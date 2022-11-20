from tkinter import *
from random import randint
from tkinter import messagebox


def thestart():
    root = Tk()
    root.geometry('300x300+578+73')
    
    messagebox.showinfo('Instructions', '1.Guess a number between 1-10\n'
                                        '2.Red: You\'re closer\n'
                                        '3.Green: You\'re in midway\n'
                                        '4.Blue: You\'re far')
    root.configure(bg='black')
    lbl1 = Label(root, text='Enter Guess\nBetween 1-10',
                    font=('Fixedsys', 20))
    lbl1.pack(pady=10)

    bc = ''

    def game_play(x):
        if x.isdigit() and (int(x) >= 0 and int(x) <= 10):
            dif = abs(comp_num - int(x))

            if int(x) == comp_num:
                lbl1.config(text='Correct')
                bc = '#ff0000'
            elif dif == 5:
                bc = '#00ff00'

            elif dif < 5:  # red
                bc = f'#ff{dif}{dif}{dif}{dif}'
            else:  # blue
                bc = f'#{dif}{dif}{dif}{dif}ff'
            root.configure(background=bc)
        else:
            lbl1.config(text='Invalid Input')
            e.delete(0, END)

    def newnumber():
        root.configure(background='SystemButtonFace')
        lbl1.config(text='Enter Guess\nBetween 1-10')

        global comp_num
        comp_num = randint(1, 10)
        e.delete(0, END)

    e = Entry(root, width=5, font=('Consolas', 30), justify=CENTER, bg='blue', fg='white')
    e.pack(pady=20)

    submit = Button(root, text='Submit Guess', command=lambda: game_play(e.get()))
    submit.pack(pady=20)

    close = Button(root, text='Close', command=root.destroy, font=('FixedSys', 20),bg='maroon',fg='gold')
    close.pack(side=LEFT, ipadx=28)
    rand_btn = Button(root, text='Reset', command=newnumber, font=('FixedSys', 20),bg='maroon',fg='gold')
    rand_btn.pack(side=RIGHT, ipadx=28)

    newnumber()

    mainloop()
