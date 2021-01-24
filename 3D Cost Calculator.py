
from tkinter import *
from tkinter import ttk

# Dictionaries with hardcoded data

printer = {'printer': 'Creality Ender 3', 'depreciation': 24.0, 'energy consumption': 0.150, 'price': 72000, 'material diameter': 1.75}

plastics = {'Grilon PLA': {'price': 2050, 'density': '', 'diameter': ''},
            'Grilon PETG': {'price': 2207, 'density': '', 'diameter': ''},
            'Grilon ABS': {'price': '', 'density': '', 'diameter': ''}}

general = {'energy cost': 0.35, 'labor cost': 200, 'failure rate': 10}

# create window object
root = Tk()
root.title("Cost Calculator")
root.geometry('500x700')

# create the inner frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# seleccion de plastico
filament_choice = Listbox(root)

# insert listbox loop
counter = 1
for k in plastics.keys():
    filament_choice.insert(counter, k)
    counter += 1

filament_label = Label(root, text='Choose Filament')

filament_label.grid(row=0, column=0)
filament_choice.grid(row=0, column=1)
filament_choice.config(height=3)

# peso
weigth_num = StringVar()
weight_entry = Entry(root, textvariable=weigth_num)
weigth_label = Label(root, text='Weigth')

weigth_label.grid(row=1, column=0)
weight_entry.grid(row=1, column=1)

# tiempo de impresion
work_label = Label(root, text='Printing Time')
work_label.grid(row=2,column=0)

print_hours_num = StringVar()
print_hours_entry = Entry(root, textvariable=print_hours_num)
print_hours_label = Label(root, text='Hours')

print_hours_label.grid(row=3, column=0)
print_hours_entry.grid(row=3, column=1)

print_minutes_num = StringVar()
print_minutes_entry = Entry(root, textvariable=print_minutes_num)
print_minutes_label = Label(root, text='Minutes')

print_minutes_label.grid(row=4, column=0)
print_minutes_entry.grid(row=4, column=1)


# model designing
work_label = Label(root, text='Working time')
work_label.grid(row=5,column=0)

work_hours_num = StringVar()
work_hours_entry = Entry(root, textvariable=work_hours_num)
work_hours_label = Label(root, text='Hours')

work_hours_label.grid(row=6, column=0)
work_hours_entry.grid(row=6, column=1)


work_minutes_num = StringVar()
work_minutes_entry = Entry(root, textvariable=work_minutes_num)
work_minutes_label = Label(root, text='Minutes')

work_minutes_label.grid(row=7, column=0)
work_minutes_entry.grid(row=7, column=1)

# display cost

# work total
work_cost = StringVar()
work_cost_label = Label(root, textvariable=work_cost)
work_cost_label.grid(row= 8, column= 0)

# filament cost
filament_cost = StringVar()
filament_label = Label(root, textvariable=filament_cost)
filament_label.grid(row=9, column=0)

# electricity cost
electricity_cost = StringVar()
electricity_label = Label(root, textvariable=electricity_cost)
electricity_label.grid(row=10, column=0)

# printer depreciation
depreciation = StringVar()
depreciation_label = Label(root, textvariable=depreciation)
depreciation_label.grid(row=11, column=0)

# subtotal
subtotal = StringVar()
subtotal_label = Label(root, textvariable=subtotal)
subtotal_label.grid(row=12, column=0)

# including failures
failures_cost = 0
failures_label = Label(root, textvariable=failures_cost)
failures_label.grid(row=13, column=0)

# display quoted price

# markup
markup = StringVar()
markup_entry = Entry(root, textvariable='markup')
markup_label = Label(root, text='Markup')

markup_label.grid(row=14, column=0)
markup_entry.grid(row=14, column=1)

# suggested price
suggested = StringVar()
suggested_label = Label(root, textvariable=suggested)
suggested_label.grid(row=15, column=0)


# button 
calculate_btn = ttk.Button(root, text='calculate', command=lambda: all())
calculate_btn.grid(row=16, column=1)

# calculation functions

def all():
    filament_price_cost()
    energy_cost()
    printer_depreciation()
    labor_time()
    subtotal_function()
    failures_included()
    suggested_price()


def filament_price_cost():

    # local variables
    filament_price = plastics['Grilon PLA']['price']
    weight = weigth_num.get()

    # Calculate the price
    calc = int(weight)/1000 * filament_price

    # Write and return
    filament_cost.set(str(calc))

    # return calc;
    print(calc)


def energy_cost():

    # local variables
    energy_consumption = printer['energy consumption']
    energy_cost = general['energy cost']

    # time variables
    hours = print_hours_num.get()
    minutes = print_minutes_num.get()


    # Calculate the time
    time_calc = (int(hours) * 60 + int(minutes)) / 60

    # Calculate the price.
    calc = energy_consumption * energy_cost * time_calc

    # Write and return.
    electricity_cost.set(str(calc))

    # return calc;
    print(calc)


def printer_depreciation():

    # Variables declaration, and get the values
    depreciation_cost = printer['depreciation']

    # time variables
    hours = print_hours_num.get()
    minutes = print_minutes_num.get()


    # Calculate the time
    time_calc = (int(hours) * 60 + int(minutes)) / 60

    # Calculate the depreciation
    calc = time_calc * int(depreciation_cost)

    # Write and return
    depreciation.set(str(calc))


def labor_time():

    # Declare the variables with their values.
    labor_cost = general['labor cost']

    # time variables
    hours = work_hours_num.get()
    minutes = work_minutes_num.get()


    # Calculate the time
    time_calc = (int(hours) * 60 + int(minutes)) / 60

    # Calculate the time.
    calc = time_calc * labor_cost

    # Write and return.
    work_cost.set(str(calc))


def subtotal_function():

    # Variable declaration.
    filament = filament_cost.get()
    electricity = electricity_cost.get()
    printer_depreciation = depreciation.get()
    work = work_cost.get()
    
    # Arithmetic.
    sum = filament + electricity + printer_depreciation + work

    # Write and return
    subtotal.set(str(sum))

def failures_included():

    # Declare variables
    failure_rate = general['failure rate']
    subtotal_cost = subtotal.get()

    # Arithmetic
    calculated_percentage = (int(subtotal)*failure_rate)/100
    sum = subtotal + calculated_percentage

    # Write and return
    failures_cost.set(str(sum))


def suggested_price():

    # Variable declaration.
    including_failures = failures_cost.get()
    markup = markup.get()

    # Arithmetic.
    suggested_cost =  (int(including_failures)*int(markup))/100

    # Write and return
    suggested.set(str(suggested_cost))


# start program 
root.mainloop()
