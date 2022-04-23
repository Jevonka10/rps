from tkinter import *
import random
tk = Tk()


tk.geometry('1200x650')
tk.resizable(False, False)
tk.title('rock paper scissor program')
ro = PhotoImage(file='rock.png')
pa = PhotoImage(file='paper.png')
sc = PhotoImage(file='scissor.png')
p1 = PhotoImage(file='p1.png')
rf = [ro, sc, p1]
tk.iconphoto(True, random.choice(rf))
def spin():
    i = score.get()
    btn1.config(text='try again')
    comp = random.choice(rps)
    you = mm.get()
    lb2.config(text='you', compound='bottom', font=('', 25))
    lb3.config(text='comp', compound='bottom', font=('', 25))
    lb1.config(text=f'you: {you}, comp: {comp}')
    if you == r:
        lb2.config(image=ro)
    if comp == r:
        lb3.config(image=ro)
    if you == p:
        lb2.config(image=pa)
    if comp == p:
        lb3.config(image=pa)
    if you == s:
        lb2.config(image=sc)
    if comp == s:
        lb3.config(image=sc)
    if you == comp:
        lb4.config(text='tie')
    if you == r:

        if comp == p:
            lb4.config(text='you lose')
            return False
        if comp == s:
            lb4.config(text='you won')
            return score.set(i+1)
    if you == p:
        if comp == s:
            lb4.config(text='you lose')
            return False
        if comp == r:
            lb4.config(text='you won')
            return score.set(i+1)
    if you == s:
        if comp == r:
            lb4.config(text='you lose')
            return None
        if comp == p:
            lb4.config(text='you won')
            score.set(i+1)

score = IntVar()
score.set(0)
lb6 = Label(tk, font=('Comic Sans MS', 25),text='score: ')
lb6.grid(row=6, column=1)
lb5 = Label(tk, font=('Comic Sans MS', 25),textvariable=score)
lb5.grid(row=6, column=2)

mm = StringVar(tk)
mm.set('paper')
rps = [ r:='rock', p:='paper', s:='scissor']
label = Label(tk, text='choose any option').grid(row=0, column=0)
youbox = OptionMenu(tk, mm, *rps)
youbox.grid(row=1, column=0)
label1 = Label(tk, text='-------------------------').grid(row=3, column=0)
lb1 = Label(tk, font=('Comic Sans MS', 25))
lb1.grid(row=4, column=0)
lb2 = Label(tk)
lb2.grid(row=4, column=1)
lb3 = Label(tk)
lb3.grid(row=4, column=2)
lb4 = Label(tk, font=('Comic Sans MS', 25))
lb4.grid(row=5, column=0)

btn1 = Button(tk, command=spin, text='play')

btn1.grid()

tk.mainloop()

