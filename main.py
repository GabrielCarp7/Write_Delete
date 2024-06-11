from tkinter import *
from tkinter.ttk import *

"""

Desktop App >> The Most Dangerous Writing App

    - Monitor the key presses:
        - If the user stops writing something for 10 sec delete everything they have written up to that point

"""

# 1000 milliseconds = 1 second
typing_delay = 10000
typing_timer = None


def on_key_release(event):
    global typing_timer
    if typing_timer is not None:
        window.after_cancel(typing_timer)
    typing_timer = window.after(typing_delay, on_typing_stopped)


def on_typing_stopped():
    print("User has stopped typing.")
    text.delete(1.0, END)


window = Tk()
window.title("The Most Dangerous Writing App")
window.minsize(500, 500)

# Description label
label = Label(text="Write everything you want, "
                   "but keep in mind that if you stop writing for more than 10 sec everything will be deleted",
              font=("Ariel", 24, "bold"), padding=50)
label.grid(column=0, row=0, columnspan=3)

# Text
text = Text(height=30, width=100, padx=10, pady=10, font=("Ariel", 18))
text.focus()
text.grid(column=0, row=1, columnspan=3)

text.bind('<KeyRelease>', on_key_release)

window.mainloop()
