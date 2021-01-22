
from tkinter import *
from tkinter import ttk

# create window object
root = Tk()
root.title("Cost Calculator")
root.geometry('500x200')

# create the inner frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# general
# seleccion de plastico

# peso
weigth_num = StringVar()
weight_entry = Entry(root, textvariable=weigth_num)
weigth_label = Label(root, text='Weigth')
weight_entry.grid(row=1, column=1)
weigth_label.grid(row=1, column=0)

# tiempo de impresion
work_label = Label(root, text='Printing Time')
work_label.grid(row=2,column=0)

print_hours_num = StringVar()
print_hours_entry = Entry(root, textvariable=print_hours_num)
print_hours_label = Label(root, text='Hours')
print_hours_entry.grid(row=3, column=1)
print_hours_label.grid(row=3, column=0)

print_minutes_num = StringVar()
print_minutes_entry = Entry(root, textvariable=print_minutes_num)
print_minutes_label = Label(root, text='Minutes')
print_minutes_entry.grid(row=4, column=1)
print_minutes_label.grid(row=4, column=0)

# model designing
work_label = Label(root, text='Working time')
work_label.grid(row=5,column=0)

work_hours_num = StringVar()
work_hours_entry = Entry(root, textvariable=work_hours_num)
work_hours_label = Label(root, text='Hours')
work_hours_entry.grid(row=6, column=1)
work_hours_label.grid(row=6, column=0)

work_minutes_num = StringVar()
work_minutes_entry = Entry(root, textvariable=work_minutes_num)
work_minutes_label = Label(root, text='Minutes')
work_minutes_entry.grid(row=7, column=1)
work_minutes_label.grid(row=7, column=0)

# display cost

# filament cost
# electricity cost
# printer depreciation
# subtotal
# including failures

# display quoted price
# markup
# suggested price



# button 
calculate_btn = ttk.Button(root, text='calculate')
calculate_btn.grid(row=10, column=0)

# start program 
root.mainloop()
