from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_result.config(text=f"{km}")
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result = Label(text="0")
kilo_result.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculated_button = Button(text="Calculate",command=convert)
calculated_button.grid(column=1, row=2)

window.mainloop()