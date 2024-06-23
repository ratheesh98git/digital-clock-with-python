from tkinter import Label, Tk 
import time

app_window = Tk() 
app_window.title("Digital Clock with Date") 
app_window.geometry("420x200") 
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label_time = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label_time.grid(row=0, column=0, columnspan=2)

label_date = Label(app_window, font=("Helvetica", 24, 'bold'), bg=background, fg=foreground)
label_date.grid(row=1, column=0, columnspan=2)

def digital_clock(): 
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")
    label_time.config(text=current_time) 
    label_date.config(text=current_date)
    label_time.after(200, digital_clock)

digital_clock()
app_window.mainloop()
