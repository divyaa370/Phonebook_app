from tkinter import*

class Phonebook(object):
    def __init__(self, master):
        self.master = master
        top = Frame(master, height = 150, bg = "pink", bd = 8, relief = GROOVE)
        top.pack(fill = X)

def main() :
    win = Tk()
    app = Phonebook(win)
    win.title('Myphonebookapp')
    win.geometry('650x570+300+100')
    win.resizable(False, False)
    win.mainloop()
    
main()
