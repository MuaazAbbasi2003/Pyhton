
import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=500)

# Label settings
my_label = tkinter.Label(
    text="Is Equal To",
    font=("Arial", 14, "bold")
)
my_label.place(x=50, y=150)

# Entry settings
input_field = tkinter.Entry(width=30)
input_field.place(x=200, y=150)

miles_label = tkinter.Label(
    text="Miles",
    font=("Arial", 10, "bold")
)
miles_label.place(x=350, y=150)

# Result label
result_label = tkinter.Label(
    text="0",
    font=("Arial", 10, "bold")
)
result_label.place(x=200, y=200)

km_label = tkinter.Label(
    text="Km",
    font=("Arial", 10, "bold")
)
km_label.place(x=350, y=200)


# Getting the input
def get_input():
    value = float(input_field.get())
    result = value * 1.60934
    result_label.config(text=str(round(result, 2)))


# Button settings
calculate_button = tkinter.Button(
    text="Calculate",
    command=get_input
)
calculate_button.place(x=200, y=250)

window.mainloop()
