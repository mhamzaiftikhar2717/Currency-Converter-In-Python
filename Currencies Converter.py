from tkinter import *
from tkinter import ttk
import requests

# initialize tkinter window
window = Tk()
window.title("Currencies Converter")
window.config(padx=10, pady=10, bg="Black")

# main heading of GUI
heading = Label(text="Currencies Converter", font=("Times New Roman", 20,), fg="#F0F0FF", bg="Black")
heading.grid(column=2, row=1, pady=30)

# initializing currencies to use in the program
currencies = ['Australian Dollar (AUD)', 'Chinese Yuan (CNY)', 'Euro (EUR)', 'Japanese Yen (JPY)', 'Pakistani Rupee ('
                                                                                                   'PKR)',
              'Pound sterling (GBP)', 'Russian Ruble (RUB)', 'Saudi Riyal (SAR)', 'United Arab Emirates Dirham ('
                                                                                  'AED)', 'United States Dollar (USD)']

# labeling and setting the dropdown/combobox for currency selection
n = StringVar()
currency_select_label = Label(text="Select Currency you want to convert", font=("Times New Roman", 12,), bg="green", fg="#ffffff")
currency_select_label.grid(column=2, row=2, pady=10)

currency_select = ttk.Combobox(window, values=currencies, width=32, textvariable=n)
currency_select.grid(column=2, row=3)

# entry box for user to enter amount he/she wants to convert
enter_amount = Label(text="Select Amount You Want to Convert", font=("Times New Roman", 12,), bg="green", fg="#ffffff")
enter_amount.grid(column=2, row=4, pady=10)

amount_to_convert = Entry(width=20)
amount_to_convert.grid(column=2, row=5)

# dropdown for currency to convert into
convert_into_label = Label(text=f"Currency you want to convert into", font=("Times New Roman", 12, ), bg="green", fg="#ffffff")
convert_into_label.grid(column=2, row=6, pady=10)
m = StringVar()
convert_into = ttk.Combobox(window, values=currencies, width=20, textvariable=m)
convert_into.grid(column=2, row=7)
converted = Label()


# convert button function
def convert():
    global converted
    # converted currency label
    converted = Label(font=("Times New Roman", 12,), fg="#ffffff", bg="#1F2124", pady=10)

    try:
        # save amount
        amount = int(amount_to_convert.get())

        # saving the user input of currency to convert from
        currency_1 = currency_select.get()[-4:-1]

        # saving the currency to convert to
        currency_2 = convert_into.get()[-4:-1]

        URL = "https://openexchangerates.org/api/latest.json?app_id=3a7a1d3d1f97409ab8c24a9d8239808c"
        response = requests.get(URL).json()

        # fetch required values from API rates
        val_c1, val_c2 = response["rates"][currency_1], response["rates"][currency_2]

        # display converted currency
        converted.config(text=f"1 {currency_1} = {round(val_c2 / val_c1, 4)} {currency_2}\n\n{amount:,.2f} {currency_1}"
        f" = {round(val_c2 / val_c1 * amount, 2):,.2f} {currency_2}")
        converted.grid(column=2, row=8)
    except:
        pass


# convert currency button
convert_button = Button(text="Convert", width=10,  font=("Times New Roman", 16,), bg="brown", command=convert)
convert_button.grid(column=2, row=9, pady=25)


# reset button function
def reset():
    # reset all the states
    currency_select.delete(0, "end")
    convert_into.delete(0, "end")
    amount_to_convert.delete(0, "end")
    converted.destroy()


# reset button
reset_button = Button(text="Reset", width=10, font=("Times New Roman", 16,), command=reset, bg="yellow", border=0)
reset_button.grid(column=2, row=10, pady=20)

# tkinter window loop
window.mainloop()