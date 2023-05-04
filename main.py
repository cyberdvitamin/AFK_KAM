import tkinter as tk
from tkinter import ttk

import keyboard
import numpy
import pyautogui
import random
import time

# Getting screen size

ScreenX, ScreenY = pyautogui.size()


# Function for autofill with "Enter time HH:MM" from the start

def time_on_entry_click(event):
    if time_entry.get() == 'Enter time HH:MM':
        time_entry.delete(0, "end")


# Function for autofill with "Enter time HH:MM" if the entry is empty

def time_on_focusout(event):
    if time_entry.get() == '':
        time_entry.insert(0, 'Enter time HH:MM')


# Function for autofill with "Enter any text here" from the start

def keyboard_on_entry_click(event):
    if keyboard_entry.get() == 'Enter any text here':
        keyboard_entry.delete(0, "end")


# Function for autofill with "Enter any text here" if the entry is empty

def keyboard_on_focusout(event):
    if keyboard_entry.get() == '':
        keyboard_entry.insert(0, 'Enter any text here')


# Function for shutdown checkbox to shut down the computer

def shutdown_checkbox_value():
    if shutdown_var.get() == 1:
        pyautogui.hotkey('win', 'r')
        pyautogui.write("shutdown /s")
        pyautogui.press("enter")


# Function for hour error window

def hour_error_window():
    hour_error = tk.Toplevel(root)
    hour_error.title("Time ERROR")
    hour_error.geometry("300x50")
    hour_error.resizable(False, False)
    hour_error_label = tk.Label(hour_error, text="You have entered a non existing hour!")
    hour_error_label.pack()


# Function for hour error window

def minute_error_window():
    minute_error = tk.Toplevel(root)
    minute_error.title("Time ERROR")
    minute_error.geometry("300x50")
    minute_error.resizable(False, False)
    minute_error_label = tk.Label(minute_error, text="You have entered a non existing minute!")
    minute_error_label.pack()


# Function for EMKey error window

def EMKey_error_window():
    EMKey_error = tk.Toplevel(root)
    EMKey_error.title("Key ERROR")
    EMKey_error.geometry("300x50")
    EMKey_error.resizable(False, False)
    EMKey_error_label = tk.Label(EMKey_error, text="You have entered a non existing key!")
    EMKey_error_label.pack()


# Function for checking if a string is an integer

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Function for splitting the string in 2 parts, hours and minutes, also validating the time to be correct

def valid_time():
    time_hour, time_minute = time_entry.get().split(":")
    if is_int(time_hour) is False or int(time_hour) > 23 or int(time_hour) < 0:
        hour_error_window()
    elif is_int(time_minute) is False or int(time_minute) > 59 or int(time_minute) < 0:
        minute_error_window()
    else:
        return True


# Function for the Start button that gets everything imputed and creates the loop for the script

def start_button():
    keyboardText = keyboard_entry.get()

    if valid_time() is True:
        root.iconify()
        time.sleep(5)

        while keyboard.is_pressed(listbox.get("active")) is False:
            now = time.localtime(time.time())
            time_hour, time_minute = time_entry.get().split(":")
            if now.tm_hour >= int(time_hour) and now.tm_min >= int(time_minute):
                shutdown_checkbox_value()
                break
            else:
                MoveToX = numpy.random.randint(0, ScreenX)
                MoveToY = numpy.random.randint(0, ScreenY)
                MoveToTime = numpy.random.uniform(0.2, 2)
                pyautogui.moveTo(MoveToX, MoveToY, MoveToTime)

                if keyboard_var.get() == 1 and random.randint(0, 100) <= 40:
                    pyautogui.write(keyboardText, interval=round(random.uniform(0.01, 0.30), 2))


# The options for the listbox

options = ["esc", "1", "2", "3", "4", "5", "6", "7", "8", "9",
           "0", "-", "=", "q", "w", "e", "r", "t", "y", "u",
           "i", "o", "p", "[", "]", "'\'", "a", "s", "d", "f",
           "g", "h", "j", "k", "l", ";", "'", "z", "x", "c",
           "v", "b", "n", "m", ",", ".", "/", "tab", "capslock",
           "shift", "ctrl", "alt", "space", "enter", "backspace"]

# Creating the main window

root = tk.Tk()

# Setting the window size and position

window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_pos, y_pos))
root.resizable(False, False)

# Setting the window title

root.title("AFK KAM v1.0")


# Creating the title label

title_label = ttk.Label(root, text="Keyboard And Mouse Script", font=("Arial", 20))
title_label.pack()

# Setting a font for listbox widget label

label_font = ("Helvetica", 16)

# Creating the option label

option_label = tk.Label(root, text="Select an Emergency Key:")

# Creating a variable to store the selected option

var = tk.StringVar(root)
var.set(options[0])  # Set the default value to the first option

# Creating a listbox widget for the EMKey option

listbox = tk.Listbox(root, selectmode="single", font=label_font, height=5, width=19)

# Add the options to the listbox

for option in options:
    listbox.insert("end", option)

# Pack the widgets onto the window

option_label.pack()
listbox.pack()

# Setting a font for time and keyboard entry

entry_font = ("Helvetica", 15)

time_entry = tk.Entry(root, font=entry_font)
time_entry.config(borderwidth=3, highlightthickness=1, highlightbackground="black")
time_entry.insert(0, 'Enter time HH:MM')  # set the default value of the entry field
time_entry.bind('<FocusIn>', time_on_entry_click)  # bind the click event
time_entry.bind('<FocusOut>', time_on_focusout)  # bind the focus out event
time_entry.pack()

# Setting up shutdown checkbox and the variable for it

shutdown_var = tk.IntVar()

shutdown_checkbox = tk.Checkbutton(root, text="Auto Shutdown", variable=shutdown_var, onvalue=1, offvalue=0,
                                   font=label_font, padx=20, pady=5)
shutdown_checkbox.pack()

# Setting up keyboard checkbox and the variable for it

keyboard_var = tk.IntVar()

keyboard_checkbox = tk.Checkbutton(root, text="Keyboard text", variable=keyboard_var, onvalue=1, offvalue=0,
                                   font=label_font, padx=20, pady=5)
keyboard_checkbox.pack()

keyboard_entry = tk.Entry(root, font=entry_font)
keyboard_entry.config(borderwidth=3, highlightthickness=1, highlightbackground="black")
keyboard_entry.insert(0, 'Enter any text here')  # set the default value of the entry field
keyboard_entry.bind('<FocusIn>', keyboard_on_entry_click)  # bind the click event
keyboard_entry.bind('<FocusOut>', keyboard_on_focusout)  # bind the focus out event
keyboard_entry.pack()

# Creating a start button

start_button = ttk.Button(root, text="Start", command=start_button)
start_button.pack()

# Running the main event loop

root.mainloop()

# This script was created by cyberdvitamin
