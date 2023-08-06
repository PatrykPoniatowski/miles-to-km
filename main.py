from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20) 

input_text = Entry(width=10)
input_text.insert(0, "0")
input_text.grid(row=0, column=2)

miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(row=0, column=3)

equal_label = Label(text="is equal to", font=("Arial", 14))
equal_label.grid(row=1, column=1)

result_label = Label(text="0", font=("Arial", 14))
result_label.grid(row=1, column=2)

km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(row=1, column=3)

def button_clicked():
    miles = float(input_text.get())
    conversion = 1.609 * miles
    conversion = round(conversion, 2)
    result_label["text"] = f"{conversion} Km"

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=2, column=2)


for col in range(4):
    window.columnconfigure(col, weight=1)

window.mainloop()
