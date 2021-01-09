from tkinter import *
import data

def click():
    entered_text = textentry.get()
    output.delete(0,0, END)
    

#Main
window = Tk()
window.title("Weather Report")
window.configure(background = "grey")

#Prompt Label
Label (window, text = "Weather Report", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 0, column = 0, sticky = S)
Label (window, text = "Please enter a city:", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 1, column = 0, sticky = S)

#Textbox
textentry = Entry(window, width = 50, bg = "white")
textentry.grid(row=2,column = 0, sticky = E)

#Submit
Button(window, text = "SUBMIT", width = 6, command = click).grid(row=3, column=0, sticky = S)

#Results Label
Label (window, text = "\nWeather:", bg="grey", fg = "white", font=" none 12 bold").grid(row=4, column = 0, sticky = W)
Label (window, text = "\nTemperature:", bg="grey", fg = "white", font=" none 12 bold").grid(row=6, column = 0, sticky = W)
Label (window, text = "\nWind:", bg="grey", fg = "white", font=" none 12 bold").grid(row=8, column = 0, sticky = W)

#Ouput
output = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output.grid(row=5,column = 0, columnspan = 2, sticky = W)

output = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output.grid(row=7,column = 0, columnspan = 2, sticky = W)

output = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output.grid(row=9,column = 0, columnspan = 2, sticky = W)

#Exit
def close_window():
    window.destroy()
    exit()
Button(window, text = "EXIT", width = 4, command = close_window).grid(row=10, column=0, sticky = E)



#Run the Main Loop
window.mainloop()
