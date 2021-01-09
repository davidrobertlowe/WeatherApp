from tkinter import *

from tkinter import *

class Window(Frame):

    def client_exit(self):
        exit()
    
    def _init_(self, master = None):
        Frame._init_(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        
        self.pack(fill=BOTH, expand = 1)

        quitButton = Button(self,text = "Quit", command=self.client_exit)
        quitButton.place(x=360, y=270)
        
        
root = Tk()
root.geometry("400x300")
app = Window(root)
app.init_window()
root.mainloop()