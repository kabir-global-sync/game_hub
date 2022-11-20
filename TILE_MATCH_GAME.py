from tkinter import *
from tkinter import messagebox
import random

count = 0
answer_list = []
answer_dic = {}
final = 0
def thestart():
    root = Tk()
    root.title('TILE-MATCH')
    root.geometry('500x500+578+73')
    root.configure(bg='black')
    Label(root, text='Welcome to The Gam-iles', font=('Forte', 20),bg='black',fg='gold').pack()
    messagebox.showinfo('INSTRUCTIONS', '1.There will be 12 tiles in total\n2.Each tile has a number under it\n'
                                        '3.Click on the tiles and try to match their numbers\n'
                                        '4.When two tiles match they get disabled\n'
                                        '5.The game ends when all the tiles match\n'
                                        'TIP: Try remembering the number under each tile once you clicked')

    btn_frm = Frame(root)
    btn_frm.pack(padx=(10, 10), pady=(10, 10))

    button_font = ('Consolas', 20)
    match = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(match)  # shuffling the numbers

    def heart(button, number):
        global count, answer_dic, answer_list, final
        if button['text'] == "" and count < 2:
            button['text'] = match[number]
            answer_list.append(number)
            answer_dic[button] = match[number]
            count += 1
        if len(answer_list) == 2:
            if match[answer_list[0]] == match[answer_list[1]]:  # checks if the numbers on tiles match
                final += 1
                count = 0
                answer_list = []
                for key in answer_dic:
                    key['state'] = DISABLED
                    key.configure(bg='turquoise')
                answer_dic = {}
            else:
                messagebox.showinfo('RESULT', 'TILES NOT MATCH')
                count = 0
                answer_list = []
                # reset button
                for key in answer_dic:
                    key['text'] = ''
                answer_dic = {}
        if final == len(match) // 2:
            response = messagebox.askyesno('RESULT', 'MATCHED ALL TILES\n---PLAY AGAIN?')
            if response:
                root.destroy()
                count=0
                answer_dic={}
                answer_list=[]
                final=0
                thestart()
            else:
                root.destroy()

    btn1 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn1, 0), height=3, width=6)
    btn1.grid(row=0, column=0)
    btn2 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn2, 1), height=3, width=6)
    btn2.grid(row=0, column=1)
    btn3 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn3, 2), height=3, width=6)
    btn3.grid(row=0, column=2)
    btn4 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn4, 3), height=3, width=6)
    btn4.grid(row=0, column=3)

    btn5 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn5, 4), height=3, width=6)
    btn5.grid(row=1, column=0)
    btn6 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn6, 5), height=3, width=6)
    btn6.grid(row=1, column=1)
    btn7 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn7, 6), height=3, width=6)
    btn7.grid(row=1, column=2)
    btn8 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn8, 7), height=3, width=6)
    btn8.grid(row=1, column=3)

    btn9 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn9, 8), height=3, width=6)
    btn9.grid(row=2, column=0)
    btn10 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn10, 9), height=3, width=6)
    btn10.grid(row=2, column=1)
    btn11 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn11, 10), height=3, width=6)
    btn11.grid(row=2, column=2)
    btn12 = Button(btn_frm, text='', font=button_font, border=4, command=lambda: heart(btn12, 11), height=3, width=6)
    btn12.grid(row=2, column=3)

    
    mainloop()
