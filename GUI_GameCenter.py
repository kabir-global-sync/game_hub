from tkinter import *
import GUIRockPapSci as rps
import GUItic_tac_toe as ttt
import GUI_WordJumbo as jmb
import GUI_Number_Guessing as gng
import TILE_MATCH_GAME as tile

wid = Tk()
wid.configure(bg='black')
btn_font = ('FixedSys', 15)
lbl = Label(wid, text='Choose Your Game', font=('Fixedsys', 20), bg='black', fg='cyan')
lbl.pack(pady=(10, 0), padx=10)
frm1 = LabelFrame(wid, text='Games-List', bg='black', fg='white')
frm1.pack(pady=(10, 10), padx=10)

def buttonHover(button,onEnter,onLeave):
    button.bind('<Leave>',func=lambda e:button.config(background=onEnter,fg='#70fe8f'))
    button.bind('<Enter>', func=lambda e: button.config(background=onLeave,fg='black'))

    ...
def game1():
    rps.thestart()


def game2():
    ttt.thestart()


def game3():
    jmb.thestart()


def game4():
    gng.thestart()


def game5():
    tile.thestart()


btn1 = Button(frm1, text='Tic-Tac-Toe', font=btn_font, border=2, command=game2, bg='black', fg='#70fe8f')
buttonHover(btn1,'black','#00ffff')

btn2 = Button(frm1, text='Rock-Pap-Sci', font=btn_font, border=2, command=game1, bg='black', fg='#70fe8f')
buttonHover(btn2,'black','#00ffff')
btn3 = Button(frm1, text='Number-Guess', font=btn_font, border=2, command=game4, bg='black', fg='#70fe8f')
buttonHover(btn3,'black','#00ffff')
btn4 = Button(frm1, text='Word-Jumble', font=btn_font, border=2, command=game3, bg='black', fg='#70fe8f')
buttonHover(btn4,'black','#00ffff')
btn5 = Button(frm1, text='Tile Match', font=btn_font, border=2, command=game5, bg='black', fg='#70fe8f')
buttonHover(btn5,'black','#00ffff')
btn1.pack(padx=10, ipadx=61, pady=5)
btn2.pack(padx=10, ipadx=52, pady=5)
btn3.pack(padx=10, ipadx=43, pady=5)
btn4.pack(padx=10, ipadx=51, pady=5)
btn5.pack(padx=10, ipadx=51, pady=5)

mainloop()
