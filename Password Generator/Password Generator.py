from tkinter import *
import tkinter.messagebox
from random import choices, sample
from string import ascii_uppercase, ascii_lowercase, digits
from os import path

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    
    return path.join(base_path, relative_path)

# basic Setup for Windows 
root = Tk()
root.title("Passord Generator | Manager")
root.geometry("400x420")
root.wm_iconbitmap(resource_path("Password Generator.ico"))
root.configure(bg='lightblue')

# Creating password file if not pressent in CWD
if path.isfile("password")==False: open('password', 'w')

def generatePass():
    """
    Generate a random password made up of lowercase and might contain Uppercase, Special Symbol, Numbers
    """
    global lastPass
    
    # generating Characters
    if Upper.get() == 1:
        rUpper = choices(ascii_uppercase, k=5)
    else:
        rUpper = []
    if Special.get() == 1:
        rSpecial = choices("-_@!?#$%^&*.", k=5)
    else:
        rSpecial = []
    if Number.get() == 1:
        rNumber = choices(digits, k=5)
    else:
        rNumber = []
        
    # Making password with the sampled characters
    randomGen = sample(rUpper+rSpecial+rNumber+choices(ascii_lowercase, k=16), k=int(length.get()))
    
    TxtBox.config(state="normal")
    newpass = f"{"".join(randomGen)}\n"
    
    # Writing new Password in TextBox
    TxtBox.insert(1.0, newpass)
    lastPass = newpass.strip()
    TxtBox.config(state="disabled")
    
    # Appending New Password in password file
    with open('password', 'a') as file:
        file.write(newpass)

def getHistory():
    """Get all previously generated password"""
    TxtBox.config(state="normal")
    
    # Writing all password in decending order of time
    TxtBox.insert(1.0, "".join(open('password').readlines()[::-1]))
    TxtBox.config(state="disabled")
    
def cleanHistory():
    """Clean Text Box and Delete Previouly Generated Password"""
    TxtBox.config(state="normal")
    TxtBox.delete(1.0, "end")
    with open('password', 'w') as f:
        pass
    TxtBox.config(state="disabled")

def copied():
    """Copy Recently Generated Password to Clipboard and Showing a Popup Toast Message"""
    # Coping to clipboard
    root.clipboard_clear()
    root.clipboard_append(lastPass)
    
    # Creating a Popup Toast message
    root2 = Tk()
    root2.withdraw()
    root2.after(2000, root2.destroy)
    tkinter.messagebox.showinfo("Password Copied", f'"{lastPass}" Copied Successfully!', master=root2)


lastPass = ""   # Recent Generated Password
Frame0 = Frame(root, bg='lightblue')    # Contain Option and Length of password
    

Frame1 = LabelFrame(Frame0, text="Options") # Contain Different Options
Upper, Special, Number = IntVar(), IntVar(), IntVar()

# Different options available to make a stronge password
A2Z = Checkbutton(Frame1, text="Upper Case", onvalue=1, offvalue=0, variable=Upper, font="Sans-sarif 11")
Sym = Checkbutton(Frame1, text="Special Symbol", onvalue=1, offvalue=0, variable=Special, font="Sans-sarif 11")
Num = Checkbutton(Frame1, text="Number", onvalue=1, offvalue=0, variable=Number, font="Sans-sarif 11")


Frame2 = LabelFrame(Frame0, text="Length of Password")  # Contains different lenght of password
length = IntVar()

# Different length preset of password
low = Radiobutton(Frame2, text="Low (8)", value=8, variable=length, font="Sans-sarif 11")
med = Radiobutton(Frame2, text="Mid (12)", value=12, variable=length, font="Sans-sarif 11")
high = Radiobutton(Frame2, text="High (16)", value=16, variable=length, font="Sans-sarif 11")
length.set("8")

# Different Buttons 
Frame3 = Frame(root, bg='lightblue')    # Contain different buttons and TextBox
gen = Button(Frame3, text="Generate Pass", width=12, command=generatePass, font="Sans-sarif 11")
cpy = Button(Frame3, text="Copy", width=12, command=copied, font="Sans-sarif 11")
History = Button(Frame3, text="View History", width=12, command=getHistory, font="Sans-sarif 11")
Clear = Button(Frame3, text="Clear", width=12, command=cleanHistory, font="Sans-sarif 11")
TxtBox = Text(Frame3, width=32, height=8, relief=SOLID, font="Sans-sarif 11")

# Positional Layout of buttons
gen.grid(row=0, column=0, pady=5, padx=10)
cpy.grid(row=0, column=1, pady=5, padx=10)
History.grid(row=1, column=0, pady=5, padx=10)
Clear.grid(row=1, column=1, pady=5, padx=10)
TxtBox.grid(row=2, column=0, columnspan=2, pady=5)

for item in [A2Z, Sym, Num, low, med, high]:
    item.pack(pady=5, anchor=W)
    
# Position of main Frames
Frame0.pack()
Frame1.grid(row=0, column=0, pady=20, padx=5)
Frame2.grid(row=0, column=1, pady=20, padx=5)
Frame3.pack()

root.mainloop()
