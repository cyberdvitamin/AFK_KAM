import tkinter as tk
from tkinter import ttk
import pyautogui, keyboard, numpy, time, random

ScreenX, ScreenY = pyautogui.size()


def time_on_entry_click(event):
    """Function that gets called when the entry field is clicked"""
    if time_entry.get() == 'Enter time HH:MM':
       time_entry.delete(0, "end") # delete all the text in the entry field


def time_on_focusout(event):
    """Function that gets called when the entry field loses focus"""
    if time_entry.get() == '':
        time_entry.insert(0, 'Enter time HH:MM')


def print_shutdown_checkbox_value():
    """Function that gets called when the checkbox is clicked"""
    print(shutdown_var.get())


def print_keyboard_checkbox_value():
    """Function that gets called when the checkbox is clicked"""
    print(keyboard_var.get())


def keyboard_on_entry_click(event):
    """Function that gets called when the entry field is clicked"""
    if keyboard_entry.get() == 'Enter any text here':
       keyboard_entry.delete(0, "end") # delete all the text in the entry field


def keyboard_on_focusout(event):
    """Function that gets called when the entry field loses focus"""
    if keyboard_entry.get() == '':
        keyboard_entry.insert(0, 'Enter any text here')


def hour_error_window():
    new_window = tk.Toplevel(root)
    new_window.title("Time ERROR")
    new_window.geometry("300x50")
    new_label = tk.Label(new_window, text="You have entered a non existing hour!")
    new_label.pack()


def minute_error_window():
    new_window = tk.Toplevel(root)
    new_window.title("Time ERROR")
    new_window.geometry("300x50")
    new_label = tk.Label(new_window, text="You have entered a non existing minute!")
    new_label.pack()


def EMKey_error_window():
    new_window = tk.Toplevel(root)
    new_window.title("Key ERROR")
    new_window.geometry("300x50")
    new_label = tk.Label(new_window, text="You have entered a non existing key!")
    new_label.pack()


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def valid_time():
    time_hour, time_minute = time_entry.get().split(":")
    if(is_int(time_hour) == False or int(time_hour) > 23 or int(time_hour) < 0):
        hour_error_window()
    elif(is_int(time_minute) == False or int(time_minute) > 59 or int(time_minute) < 0):
        minute_error_window()
    else:
        return True


def start_button():
    keyboardText = keyboard_entry.get()


    if valid_time() is True:
        root.iconify()
        print(keyboardText)

        while keyboard.is_pressed(listbox.get("active")) is False:
            now = time.localtime(time.time())
            time_hour, time_minute = time_entry.get().split(":")
            if now.tm_hour >= int(time_hour) and now.tm_min >= int(time_minute):
                break
            else:
                MoveToX = numpy.random.randint(0, ScreenX)
                MoveToY = numpy.random.randint(0, ScreenY)
                MoveToTime = numpy.random.uniform(0.2, 2)
                pyautogui.moveTo(MoveToX, MoveToY, MoveToTime)

                if random.randint(0, 100) <= 40:
                    pyautogui.write(keyboardText, interval=round(random.uniform(0.01, 0.30), 2))


# Create a list of options for the dropdown
options = ["esc", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "0", "-", "=", "q", "w", "e", "r", "t", "y", "u",
            "i", "o", "p", "[", "]", "'\'", "a", "s", "d", "f",
            "g", "h", "j", "k", "l", ";", "'", "z", "x", "c",
            "v", "b", "n", "m", ",", ".", "/", "tab", "capslock",
            "shift", "ctrl", "alt", "space", "enter", "backspace"]


# Create the main window
root = tk.Tk()

# Set the window size and position
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_pos, y_pos))

# Set the window title
root.title("AFK KAM v1.0")

# Create a label
label = ttk.Label(root, text="Keyboard And Mouse Script", font=("Arial", 20))
label.pack()

label_font = ("Helvetica", 16)

# Create a label widget
label = tk.Label(root, text="Select an option:")

# Create a variable to store the selected option
var = tk.StringVar(root)
var.set(options[0])  # Set the default value to the first option

# Create a listbox widget
listbox = tk.Listbox(root, selectmode="single", font=label_font, height=5, width=19)

# Add the options to the listbox
for option in options:
    listbox.insert("end", option)

# Create a button widget to get the selected option
button = tk.Button(root, text="Get selected option", command=lambda: print(listbox.get("active")))

# Pack the widgets onto the window
label.pack()
listbox.pack()
button.pack()


entry_font = ("Helvetica", 15)


time_entry = tk.Entry(root, font=entry_font)
time_entry.config(borderwidth=3, highlightthickness=1, highlightbackground="black")
time_entry.insert(0, 'Enter time HH:MM') # set the default value of the entry field
time_entry.bind('<FocusIn>', time_on_entry_click) # bind the click event
time_entry.bind('<FocusOut>', time_on_focusout) # bind the focus out event
time_entry.pack()


shutdown_var = tk.IntVar()

shutdown_checkbox = tk.Checkbutton(root, text="Auto Shutdown", variable=shutdown_var, onvalue=1, offvalue=0, command=print_shutdown_checkbox_value, font=label_font, padx=20, pady=5)
shutdown_checkbox.pack()

keyboard_var = tk.IntVar()

keyboard_checkbox = tk.Checkbutton(root, text="Keyboard text", variable=keyboard_var, onvalue=1, offvalue=0, command=print_keyboard_checkbox_value, font=label_font, padx=20, pady=5)
keyboard_checkbox.pack()

keyboard_entry = tk.Entry(root, font=entry_font)
keyboard_entry.config(borderwidth=3, highlightthickness=1, highlightbackground="black")
keyboard_entry.insert(0, 'Enter any text here') # set the default value of the entry field
keyboard_entry.bind('<FocusIn>', keyboard_on_entry_click) # bind the click event
keyboard_entry.bind('<FocusOut>', keyboard_on_focusout) # bind the focus out event
keyboard_entry.pack()

# Create a start button
start_button = ttk.Button(root, text="Start", command=start_button) # change the function
start_button.pack()


# Run the main event loop
root.mainloop()
