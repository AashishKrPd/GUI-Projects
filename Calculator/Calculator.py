from tkinter import *
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            var = scvalue.get()
            try:
                if "^0.5" in var:
                    var = var.replace("^0.5", "**(0.5)")
                if "^-1" in var:
                    var = var.replace("^-1", "**(-1)")
                if "^" in var:
                    var = var.replace("^", "**")
                if "x" in var:
                    var = var.replace("x", "*")
                value = eval(var)
            except Exception as e:
                value = "Error"
                print(e)
        scvalue.set(value)
        
    elif text == "C":
        scvalue.set("")
    
    elif text == "B":
        scvalue.set(scvalue.get()[:-1])
    else:
        if scvalue.get() == "Error":
            scvalue.set("")
        scvalue.set(scvalue.get()+text)
    screen.update()


# def random():
#     n = list(range(0, 9))+['a', 'b' , 'c', 'd', 'e']
#     from random import choice
#     st = "#"
#     for i in range(6):
#         st+=str(choice(n))
#     return st


# color = random()


bColor = "#caf0f8"
kColor = "#edf6f9"
kbColor = "#00b4d8"
dColor = "#2b2d42"


root = Tk()
root.geometry("400x650")
root.title("Calculator by Aashish Kumar Prasad")
root.wm_iconbitmap(resource_path("calc.ico"))
root.configure(background = bColor)

scvalue = StringVar()
scvalue.set("")


screen = Entry(root, textvar = scvalue, font = "Lucida 40 bold", fg=dColor)
screen.pack(fill=X,  padx = 10, pady = 10)


buts = [["%", "^-1", "C", "B"], 
        ["^", "^0.5", "//", "/"], 
        ["7", "8", "9", "x"], 
        ["4", "5", "6", "-"], 
        ["1", "2", "3", "+"], 
        ["00", "0", ".", "="]]


for i in range(len(buts)):
    f = Frame(root , bg = bColor)
    
    for j in range(len(buts[i])):
        b = Button(f, text = buts[i][j], font="Lucida 25 bold", width=3, relief=RAISED, fg=kColor, bg=kbColor)
        b.grid(row=i, column = j, padx = 10)
        b.bind("<Button-1>", click)
    f.pack(pady = 10)
    
root.mainloop()
