import tkinter as tk
import random
import subprocess

def clearFunction(event):
    window.destroy()
    subprocess.run(["python","rpsg.py"])
def botRandomizer():
    bot=random.randint(0,2)
    if bot==0:
        return "Rock"
    elif bot==1:
        return "Paper"
    else:
        return "Scissors"
def rockChoice(event):
    rockText1=tk.Label(text="You made a Rock symbol with thy hand",bg="green", fg="white")
    rockText1.pack()
    botPlay=botRandomizer()
    rockText2=tk.Label(text=f"Bot played {botPlay}",bg="red",fg="white")
    rockText2.pack()
    if botPlay=="Rock":
        rockText3=tk.Label(text="That's a draw!",bg="yellow",fg="black")
        rockText3.pack()
    elif botPlay=="Paper":
        rockText4=tk.Label(text="You lost...",bg="red",fg="white")
        rockText4.pack()
    else:
        rockText5=tk.Label(text="You won!!!",bg="green",fg="white")
        rockText5.pack()
    return

def paperChoice(event):
    paperText1=tk.Label(text="You made a Paper symbol with thy hand",bg="green", fg="white")
    paperText1.pack()
    botPlay=botRandomizer()
    paperText2=tk.Label(text=f"Bot played {botPlay}",bg="red",fg="white")
    paperText2.pack()
    if botPlay=="Paper":
        paperText3=tk.Label(text="That's a draw!",bg="yellow",fg="black")
        paperText3.pack()
    elif botPlay=="Scissors":
        paperText4=tk.Label(text="You lost...",bg="red",fg="white")
        paperText4.pack()
    else:
        paperText5=tk.Label(text="You won!!!",bg="green",fg="white")
        paperText5.pack()
    return

def scissorsChoice(event):
    scissorsText1=tk.Label(text="You made a Scissors symbol with thy hand",bg="green", fg="white")
    scissorsText1.pack()
    botPlay=botRandomizer()
    scissorsText2=tk.Label(text=f"Bot played {botPlay}",bg="red",fg="white")
    scissorsText2.pack()
    if botPlay=="Scissors":
        scissorsText3=tk.Label(text="That's a draw!",bg="yellow",fg="black")
        scissorsText3.pack()
    elif botPlay=="Rock":
        scissorsText4=tk.Label(text="You lost...",bg="red",fg="white")
        scissorsText4.pack()
    else:
        scissorsText5=tk.Label(text="You won!!!",bg="green",fg="white")
        scissorsText5.pack()
    return

def continueProgram(event):
    text1=tk.Label(text="Lets get started then...\nchoose a symbol:")
    text1.pack()
    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)
    rockButton=tk.Button(master=window,text="Rock")
    rockButton.pack()
    rockButton.bind("<Button-1>",rockChoice)
    paperButton=tk.Button(master=window,text="Paper")
    paperButton.pack()
    paperButton.bind("<Button-1>",paperChoice)
    scissorsButton=tk.Button(master=window,text="Scissors")
    scissorsButton.pack()
    scissorsButton.bind("<Button-1>",scissorsChoice)
    return
window=tk.Tk()
window.title="RPS THE GAME"
title=tk.Label(text="Rock Paper Scissors The Game")
title.pack()
startButton=tk.Button(text="Start",width=5,height=1,bg="black",fg="white")
startButton.bind("<Button-1>", continueProgram)
startButton.pack()
clearButton=tk.Button(text="Clear",width=5,height=1,bg="black",fg="white")
clearButton.bind("<Button-1>", clearFunction)
clearButton.pack()
window.mainloop()
