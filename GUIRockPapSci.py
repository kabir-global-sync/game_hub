from tkinter import *


def thestart():
    import random

    root = Tk()
    root.title('ROCK-PAPER-SCI')
    root.geometry('400x400+578+73')
    root.configure(background='black')

    frame1 = LabelFrame(root, text='Your Choice',bg='black',fg='cyan')
    frame1.pack(pady=(10, 10))

    font_stysl = ('Fixedsys', 20)
    result_lbl = Label(root, font=font_stysl, fg='gold', bg='black')
    comp_ch = Label(root, font=font_stysl, fg='red')

    def buttonHover(button,onEnter,onLeave):
        button.bind('<Leave>',func=lambda e:button.config(background=onEnter,fg='black'))
        button.bind('<Enter>', func=lambda e: button.config(background=onLeave,fg='black'))


    # Reset game when click 'PLAY AGAIN' button
    def game_reset():
        result_lbl.pack_forget()
        comp_ch.pack_forget()
        gm_rst.destroy()
        rock_btn['state'] = NORMAL
        paper_btn['state'] = NORMAL
        scissor_btn['state'] = NORMAL
        game_start()

    def game_start():
        start_game_btn.destroy()
        greet_lbl.destroy()
        options = ['rock', 'paper', 'scissor', 'scissor', 'rock', 'paper', 'paper', 'rock']
        comp = random.choice(options)

        # Main gameplay function
        def game_play(user):

            if user == comp:
                result_lbl.config(text='IT\'S A TIE')
            elif comp == 'paper' and user == 'scissor':
                result_lbl.config(text='YOU WIN!')
            elif comp == 'paper' and user == 'rock':
                result_lbl.config(text='YOU LOOSE!')
            elif comp == 'rock' and user == 'paper':
                result_lbl.config(text='YOU WIN!')
            elif comp == 'rock' and user == 'scissor':
                result_lbl.config(text='YOU LOOSE!')
            elif comp == 'scissor' and user == 'paper':
                result_lbl.config(text='YOU LOOSE!')
            elif comp == 'scissor' and user == 'rock':
                result_lbl.config(text='YOU WIN!')
            comp_ch.config(text=f'Computer chose {comp}\n'f'You chose {user}', font=font_stysl, bg='black',
                            fg='cyan')
            comp_ch.pack()
            result_lbl.pack()
            rock_btn['state'] = DISABLED
            paper_btn['state'] = DISABLED
            scissor_btn['state'] = DISABLED

            # Game replaying button, linked to game_reset() function
            global gm_rst
            gm_rst = Button(root, text='Play Again', bg='Black', fg='white', font=font_stysl, command=game_reset)
            gm_rst.pack(pady=30)

        global rock_btn
        global paper_btn
        global scissor_btn
        # Buttons for user choice(ROCK/PAPER/SCISSOR)
        rock_btn = Button(frame1, text='ROCK', font=font_stysl, command=lambda: game_play('rock'), bg='#46fb4a',
                            fg='black')#a05e9e/a0fe9e
        rock_btn.grid(row=0, column=0, pady=10, padx=10)
        buttonHover(rock_btn,'#46fb4a','#a0fe9e')
        paper_btn = Button(frame1, text='PAPER', font=font_stysl, command=lambda: game_play('paper'), bg='#46fb4a',
                            fg='black')
        paper_btn.grid(row=0, column=1)
        buttonHover(paper_btn,'#46fb4a','#a0fe9e')
        scissor_btn = Button(frame1, text='SCISSOR', font=font_stysl, command=lambda: game_play('scissor'), bg='#46fb4a',
                                fg='black')
        scissor_btn.grid(row=0, column=2, pady=10, padx=10)
        buttonHover(scissor_btn,'#46fb4a','#a0fe9e')

    # Button to start the game
    start_game_btn = Button(root, text='Start Game', font=('Fixedsys', 20), bg='maroon', fg='gold',
                            command=game_start)
    start_game_btn.pack(pady=10)
    greet_lbl = Label(root, text='Welcome User', font=('Fixedsys', 30), bg='black',fg='gold')
    greet_lbl.pack(pady=80)

    # Button to close the game
    close = Button(root, text='Exit Game', font=('Fixedsys', 20),  bg='maroon', fg='gold', command=root.destroy)
    close.pack(side=BOTTOM, fill='both')

    mainloop()
