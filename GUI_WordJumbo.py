from tkinter import *
def thestart():
    import random

    root = Tk()
    root.geometry('600x300+578+73')
    root.configure(background='indigo')
    my_label = Label(root, text='', font=('Roboto', 30))
    my_label.pack()


    def suffel():
        ans.pack_forget()
        e.delete(0, END)
        states = ['Punjab', 'Kerala', 'Tripura', 'Rajasthan', 'English', 'Assam', 'Dispur', 'Bihar', 'Patna', 'Hindi',
                  'Chhattisgarh', 'Raipur', 'Chhattisgarh', 'Bengal']
        global word
        word = random.choice(states)  # Original randomly choosed word

        break_apart = list(word)
        random.shuffle(break_apart)
        global jumb_wd
        jumb_wd = "".join(break_apart)  # Jumbled word
        my_label.config(text=jumb_wd)


    e = Entry(root, width=30, font=('Consolas', 20))
    e.pack(pady=10)


    def check(w):
        if w == word:
            ans.config(text='CORRECT')

        else:
            ans.config(text='INCORRECT')
        ans.pack(pady=10)


    answer_btn = Button(root, text='CHECK', font=('Consolas', 14), command=lambda: check(e.get()))
    answer_btn.pack(pady=10, ipadx=50)
    btn = Button(root, text='Pick Word', command=suffel)
    btn.pack(ipadx=25, pady=20)

    ans = Label(root, text='', font=('Roboto,20'), bg='maroon', fg='beige')

    suffel()
    mainloop()
