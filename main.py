#Import the required libraries
from cProfile import label
from tkinter import *
from schedule import schedule
from datetime import timedelta, datetime
from schedule import schedule
from pytz import timezone
from generator import *


# Import the tkinter module
import tkinter

# Create the default window
window = tkinter.Tk()
window.title("KUKL water schedule for Balaju Branch")
window.minsize(width=400, height=400)
window.config(bg='#F26849')
window.config(padx=200,pady=200)


# Create the list of options
options_list = ["Nayabazar", "Mahadev khola", "Banasthali", "Dallu Aawash","Balaju"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(window)

# Set the default value of the variable
value_inside.set("Nayabazar")


# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(window, value_inside, *options_list)
question_menu.grid(column=2,row=3)




# Function to print the submitted option-- testing purpose
  
def schedule_generator():
    place=value_inside.get()
    duration = schedule[place]["duration"]
    day_number = schedule[place]["day"]
    water_coming_first_time = schedule[place]["water_coming_first_time"]
    res=water_schedule_generator(duration,day_number,water_coming_first_time)
    label_result=tkinter.Label(text=res[0])
    label_result.config(bg='#F26654')
    label_result.grid(column=2,row=5)
    label_to=tkinter.Label(text="To")
    label_to.config(bg='#F26654')
    label_to.grid(column=3,row=5)

    label_from=tkinter.Label(text="Water-Coming Date & Time :")
    label_from.grid(column=1,row=5)

    label_result2=tkinter.Label(text=res[1])
    label_result2.config(bg='#F26654')
    label_result2.grid(column=4,row=5)

  # water_schedule_generator(duration,day,water_coming_first_time)
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(window, text='Generate Routine', command=schedule_generator)
submit_button.grid(column=2,row=4)

#Labels
label_select_location = tkinter.Label(text="Select Your Location :")
label_select_location.grid(column=1,row=3)

window.mainloop()

