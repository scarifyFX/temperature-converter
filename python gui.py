from multiprocessing.sharedctypes import Value
import re
from tkinter import *

def click():
    global count
    count += 1
    print(count)

# Convert from
def toggle_checkbox(): # Celsius
    global var1, checked1  # Use global variables
    checked1 = var1.get()  # Get the current state

    # Uncheck the other checkbox
    checkbox2.deselect()
    var1.set(checked1)  # Update the state of checkbox1

    print(f"Checkbox 1 checked: {var1.get()}")

def toggle_checkbox2(): #Fahrenheit
    global var2, checked2  
    checked2 = var2.get() 

    checkbox1.deselect()
    var2.set(checked2) 

    print(f"Checkbox 2 checked: {var2.get()}")


# Convert to
def toggle_checkbox3(): # Celsius
    global var3, checked3 
    checked3 = var3.get() 

    checkbox4.deselect()
    var3.set(checked3) 

    print(f"Checkbox 3 checked: {var3.get()}")

def toggle_checkbox4(): # Fahrenheit
    global var4, checked4 
    checked4 = var4.get() 

    checkbox3.deselect()
    var4.set(checked4) 

    print(f"Checkbox 4 checked: {var4.get()}")

#defines P
def validate_entry(P):
    if not P: #last attempt made it so I couldn't remove text when there was 1 char left so this makes it possible to remove the string even when empty
        return True

    if any(char not in "01234567890." for char in P): #allowed chars
        return False

    try:
        float(P)
    except ValueError:
        return False
    return P.count(".") <= 1 #only allows one "."

# Actual conversion

def C_to_F(Celsius):
    return (Celsius * 9/5) + 32

def F_to_C(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

def convert_temp():
    try:
        temp = float(entry.get())
        if var1.get() == 1 and var4.get() == 1:
            converted_temp = C_to_F(temp)
            print(f"{temp}°C = {converted_temp:.2f}°F")
        elif var2.get() == 1 and var3.get() == 1:
            converted_temp = F_to_C(temp)
            print(f"{temp}°F = {converted_temp:.2f}°C")
        else:
            print("Select what to convert from to")
    except ValueError:
        print("Must enter a value")


count = 0

window = Tk()  # Starts a window
window.geometry("520x420")
window.resizable(False, False)
window.title("My first GUI and it is for temperature conversion")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#23272A")

button = Button(window,
                 text="Convert temperature!",
                 command=convert_temp,
                 font=("Bahnschrift", 14))
button.pack(side="bottom")
button.pack(anchor="center")
button.pack(padx=0, pady=60)

# Create separate IntVar objects for each checkbox
# Convert from
var1 = IntVar(window)
var2 = IntVar(window)

# Create the checkboxes referencing their respective variables
# Convert from
checkbox1 = Checkbutton(
    window,
    text="Celsius",
    variable=var1,
    command=toggle_checkbox
)
checkbox2 = Checkbutton(
    window,
    text="Fahrenheit",
    variable=var2,
    command=toggle_checkbox2
)

# Position the checkboxes using pack(), grid(), or place()
# Convert from
checkbox1.place(x=50, y=160, 
                #width=120, height=30
                )


checkbox2.place(x=50, y=230, 
                #width=120, height=30
                )

# Convert from end

# Convert to start

var3 = IntVar(window)
var4 = IntVar(window)

checkbox3 = Checkbutton(
    window,
    text="Celsius",
    variable=var3,
    command=toggle_checkbox3
)
checkbox4 = Checkbutton(
    window,
    text="Fahrenheit",
    variable=var4,
    command=toggle_checkbox4
)
checkbox3.place(x=400, y=160, 
                #width=120, height=30
                )
checkbox4.place(x=400, y=230, 
                #width=120, height=30
                )



#convert to end


# Enter temperature with only digits and dot/commas as valid
entry = Entry(window, validate="all", validatecommand=(window.register(validate_entry), "%P"))
#configuration for entry box
entry.config(width=20)
entry.pack(side="top")
entry.pack(anchor="center")
entry.pack(pady=30)





window.mainloop()
