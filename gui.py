from tkinter import *

def click():
    entered_text = textentry.get()

#Main
window = Tk()
window.title("Weather Report")
window.configure(background = "grey")

#Prompt Label
Label (window, text = "Please enter a city:", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 0, column = 0, sticky = S)

#Textbox
textentry = Entry(window, width = 50, bg = "white")
textentry.grid(row=2,column = 0, sticky = S)

#Submit
Button(window, text = "SUBMIT", width = 6, command = click).grid(row=3, column=0, sticky = S)

#Run the Main Loop
window.mainloop()
