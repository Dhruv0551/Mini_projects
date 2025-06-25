from tkinter import *

# Conversion function
def conversion(miles_entry):
    try:
        miles = float(miles_entry.get())
        km = round(miles * 1.609344, 2)  # More accurate conversion factor
        return km
    except ValueError:
        return "Invalid input"

# Button click handler
def onConvert():
    result = conversion(miles)
    kms.config(text=result)

# Create main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Input field
miles = Entry(width=15)
miles.grid(column=1, row=0, padx=5, pady=5)

# Miles label
label = Label(text="Miles")
label.grid(column=2, row=0, padx=5, pady=5)

# "Is Equal to" label
label2 = Label(text="Is Equal to:")
label2.grid(column=0, row=1, padx=5, pady=5)

# Result display
kms = Label(text="0", font=("Arial", 12, "bold"))
kms.grid(column=1, row=1, padx=5, pady=5)

# KM label
label3 = Label(text="KM")
label3.grid(column=2, row=1, padx=5, pady=5)

# Calculate button
calc = Button(text="Calculate", command=onConvert, bg="lightblue")
calc.grid(column=1, row=2, padx=5, pady=10)

# Start the GUI
window.mainloop()