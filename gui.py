from tkinter import *
import data
import api_req

def click():
    entered_text = textentry.get()

    textentry.delete(0,END)

    output1.delete(1.0, END)
    output2.delete(1.0, END)
    output3.delete(1.0, END)

    api_req.city(entered_text)
    if data.checkIfInCA():
        
        weather = data.weatherMain()
        temperature = data.temperature()
        wind = data.wind()
        
    else:
        weather = "N/A for non-Canadian cities"
        temperature = "N/A for non-Canadian cities"
        wind = "N/A for non-Canadian cities"
    output1.insert(END, weather)
    output2.insert(END, temperature)
    output3.insert(END, wind)
    
   
    

#Main
window = Tk()
window.title("Weather Report")
window.configure(background = "grey")

#Prompt Label
Label (window, text = "Canadian Weather Report", bg = "grey", fg = "white", font = "none 12 bold").grid(row = 0, column = 0, sticky = S)
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
output1 = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output1.grid(row=5,column = 0, columnspan = 2, sticky = W)

output2 = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output2.grid(row=7,column = 0, columnspan = 2, sticky = W)

output3 = Text(window, width = 30, height = 1, wrap = WORD, background = "white")
output3.grid(row=9,column = 0, columnspan = 2, sticky = W)

#Exit
def close_window():
    window.destroy()
    exit()
Button(window, text = "EXIT", width = 4, command = close_window).grid(row=10, column=0, sticky = E)



#Run the Main Loop
window.mainloop()
