from tkinter import *
from tkinter import messagebox

click = True  # If True --> X || If False --> O
c = 0


def thestart():
    root = Tk()
    root.title('TIC-TAC-TOE Game')
    root.configure(background='black')
    root.geometry('+578+73')
    global_font = ('Consolas', 13)

    def game_reset():  # Function to restart the game after deleting preious records
        game_frame.pack_forget()  # To clear all the buttons
        player_lbl.pack_forget()
        global c, click
        c = 0
        click = True

        game_start()

    def game_start():  # The starter function
        game_start_btn.destroy()
        global player_lbl, game_frame
        player_lbl = Label(root, text='Turn--> Player X', font=('Forte', 13), fg='cyan', bg='black')
        player_lbl.pack(side=TOP)
        game_frame = Frame(root)
        game_frame.pack(padx=(10, 10), pady=(10, 10))

        def win_msg(p, x=0):  # Result declaration
            if x == 1:
                response = messagebox.askyesno('Result', f'---PLAYER {p} WON!!!---\n'
                                                            '===PLAY AGAIN?===')

            else:
                response = messagebox.askyesno('Result', '---IT\'S A TIE !!!---\n'
                                                            '===PLAY AGAIN?===')
            if response == 0:
                root.destroy()
            else:
                game_reset()

        def check():  # Check to see if win/tie
            # For row 1
            if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
                btn1.config(bg='red')
                btn2.config(bg='red')
                btn3.config(bg='red')
                win_msg('X', 1)
            # For row 2
            elif btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
                btn4.config(bg='red')
                btn5.config(bg='red')
                btn6.config(bg='red')
                win_msg('X', 1)
            # For row 3
            elif btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
                btn7.config(bg='red')
                btn8.config(bg='red')
                btn9.config(bg='red')
                win_msg('X', 1)
            # For diagonal from Button1
            elif btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
                btn1.config(bg='red')
                btn5.config(bg='red')
                btn9.config(bg='red')
                win_msg('X', 1)
            # For diagonal from Button 3
            elif btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
                btn3.config(bg='red')
                btn5.config(bg='red')
                btn7.config(bg='red')
                win_msg('X', 1)
            # For column 1
            elif btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
                btn1.config(bg='red')
                btn4.config(bg='red')
                btn7.config(bg='red')
                win_msg('X', 1)
            # For column 2
            elif btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
                btn2.config(bg='red')
                btn5.config(bg='red')
                btn8.config(bg='red')
                win_msg('X', 1)
            # For column 3
            elif btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
                btn3.config(bg='red')
                btn6.config(bg='red')
                btn9.config(bg='red')
                win_msg('X', 1)
            ###############################
            # For row 1
            elif btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
                btn1.config(bg='yellow')
                btn2.config(bg='yellow')
                btn3.config(bg='yellow')
                win_msg('O', 1)
            # For row 2
            elif btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
                btn4.config(bg='yellow')
                btn5.config(bg='yellow')
                btn6.config(bg='yellow')
                win_msg('O', 1)
            # For row 3
            elif btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
                btn7.config(bg='yellow')
                btn8.config(bg='yellow')
                btn9.config(bg='yellow')
                win_msg('O', 1)
            # For diagonal from Button1
            elif btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
                btn1.config(bg='yellow')
                btn5.config(bg='yellow')
                btn9.config(bg='yellow')
                win_msg('O', 1)
            # For diagonal from Button 3
            elif btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
                btn3.config(bg='yellow')
                btn5.config(bg='yellow')
                btn7.config(bg='yellow')
                win_msg('O', 1)
            # For column 1
            elif btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
                btn1.config(bg='yellow')
                btn4.config(bg='yellow')
                btn7.config(bg='yellow')
                win_msg('O', 1)
            # For column 2
            elif btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
                btn2.config(bg='yellow')
                btn5.config(bg='yellow')
                btn8.config(bg='yellow')
                win_msg('O', 1)
            # For column 3
            elif btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
                btn3.config(bg='yellow')
                btn6.config(bg='yellow')
                btn9.config(bg='yellow')
                win_msg('O', 1)

            else:
                if c == 9:
                    win_msg('', 0)

        def bclick(n):  # Keep track of who plays
            global click, c
            if n['text'] == '' and click == True:  # same as <button>.config(text='')
                n['text'] = 'X'
                click = False
                player_lbl.config(text='Turn--> Player O')
                c += 1
                check()
            elif n['text'] == '' and click == False:
                n['text'] = 'O'
                click = True
                player_lbl.config(text='Turn--> Player X')
                c += 1
                check()
            else:
                messagebox.showerror('ERROR!', 'BOX ALREADY USED!!!')
            # if c == 9:
            #     check()

        # global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
        btn1 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn1), font=global_font, border=5)
        btn1.grid(row=0, column=0)
        btn2 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn2), font=global_font, border=5)
        btn2.grid(row=0, column=1)
        btn3 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn3), font=global_font, border=5)
        btn3.grid(row=0, column=2)

        btn4 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn4), font=global_font, border=5)
        btn4.grid(row=1, column=0)
        btn5 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn5), font=global_font, border=5)
        btn5.grid(row=1, column=1)
        btn6 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn6), font=global_font, border=5)
        btn6.grid(row=1, column=2)

        btn7 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn7), font=global_font, border=5)
        btn7.grid(row=2, column=0)
        btn8 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn8), font=global_font, border=5)
        btn8.grid(row=2, column=1)
        btn9 = Button(game_frame, height=3, width=6, command=lambda: bclick(btn9), font=global_font, border=5)
        btn9.grid(row=2, column=2)

    # Button to start the game
    game_start_btn = Button(root, text='Start Game', font=('Forte', 20), bg='#f4f09f', command=game_start)
    game_start_btn.pack(padx=(10, 10), pady=(10, 10))
    mainloop()