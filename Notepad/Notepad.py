from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                        filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt",
                        filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(('<<Cut>>'))

def copy():
    TextArea.event_generate(('<<Copy>>'))

def paste():
    TextArea.event_generate(('<<Paste>>'))

def about():
    showinfo("Notepad about", "Notepad by Aashish Kumar Prasad")

def version():
    showinfo("Notepad version", "Notepad Current version: v1.0.0\nNotepad Latest version: v1.0.0")



if __name__ == '__main__':
    root = Tk()
    root.title("Unititled - Notepad")
    root.wm_iconbitmap(resource_path("book.ico"))
    root.geometry("644x788")
    
    
    # Text Area
    TextArea = Text(root, font="Lucida 13")
    TextArea.pack(expand=True, fill=BOTH)
    file = None
    
    # Menu Bar
    MenuBar = Menu(root)
    
    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To Open a New File
    FileMenu.add_command(label="New", command=newFile)
    # Open an Existing File
    FileMenu.add_command(label="Open", command=openFile)
    # To save Current Fule
    FileMenu.add_command(label="Save", command=saveFile)
    # Adding Seperator
    FileMenu.add_separator()
    FileMenu.add_command(label="exit", command=quitApp)
    
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends
    
    # Edit Menu Starts
    EditMenu = Menu(MenuBar , tearoff=0)
    # Command to Cut Copy and Paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends
    
    # Help menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label="About Notepad", command=about)
    HelpMenu.add_command(label="Version", command=version)
    
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help menu Ends
    
    
    
    root.config(menu=MenuBar)
    
    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(fill=Y, side=RIGHT)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)
    
    
    root.mainloop()
