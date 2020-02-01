import Tkinter as tk
from Tkinter import *

# Small function for printing/formatting reasons
def print_statements():
    print("-----" * 11)


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift


class ConverterScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(root, text="Converter Page")
        label.pack(side="top", fill="both", expand=False)
        label.pack()
        label1 = Label(root, text="Enter a number ")
        label1.place(x=20, y=27)
        self.entry1 = tk.Entry(root)
        self.entry1.place(x=120, y=23)

  # Function which is used to calculate how much money you lose with a tax of 5%
    def calc_loss(self):
        tax = 0.95
        x1 = int(self.entry1.get())

        while True:
            try:
                print_statements()
                print("You have entered {} to be calculated".format(x1))
                print_statements()
                calculation = x1 * tax
                result = x1 - calculation
            except ValueError as e:
                print(e)
                continue
            else:
                label1 = Label(root, text=result)
                label1.pack()
                print("After taking 5% off your number you are left with {}".format(result))
                break


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        page = ConverterScreen(self)
        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(fill="none", expand=True)
        container.pack(side="bottom", fill="both", expand=True)

        b1 = tk.Button(button_frame, text="Start Calculating", command=page.calc_loss)

        b1.pack(side="top")
        page.place(in_=container, x=1, y=2, relwidth=1, relheight=1)


if __name__ == '__main__':
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_title("FUT Converter")
    root.wm_geometry("400x400")
    root.mainloop()


# Function which is used to calculate how much money you lose with a tax of 5%
# def calc_loss():
#     tax = 5
#     percentage = 100
#
#     while True:
#         try:
#             num1 = int(raw_input("Enter a number to calculate tax loss "))
#             print_statements()
#             print("You have entered {} to be calculated".format(num1))
#             print_statements()
#             calculation = num1 / percentage * tax
#             result = num1 - calculation
#         except ValueError as e:
#             print(e)
#             continue
#         else:
#             print("After taking 5% off your number you are left with {}".format(result))
#             break
#
# # Function which determines if you have made a profit or loss depending on your buy and sale price
# def profit_and_loss():
#     tax = 5
#     percentage = 100
#
#     while True:
#         try:
#             paid_number = int(raw_input("Enter how much you paid "))
#             print("You have entered {} as how much you paid".format(paid_number))
#             print_statements()
#             sale_amount = int(raw_input("Enter the amount you will sell for "))
#             print_statements()
#             print("You have entered {} as how much you are selling for".format(sale_amount))
#             tax_calc = sale_amount / percentage * tax
#             amount_after_tax = sale_amount - tax_calc
#             print_statements()
#             print("The amount of tax for {} is {}".format(sale_amount, tax_calc))
#             print_statements()
#             print("After the sale and tax you have {}").format(amount_after_tax)
#             final_result = amount_after_tax - paid_number
#             print_statements()
#
#         except ValueError as e:
#             print(e)
#             continue
#
#         else:
#             if amount_after_tax > paid_number:
#                 print("Profit: You made {} profit").format(abs(final_result))
#             elif amount_after_tax < paid_number:
#                 print("Loss: You lost {}").format(abs(final_result))
#             else:
#                 print("Broke even")
#             break
#
# # Main method
# if __name__ in '__main__':
#
#     user_input = ''
#     print("FUT Calc:")
#     print_statements()
#     print("There is two options to choose from, these are:")
#     print("Options are A: To Calculate Profit or Loss and B: Calculate tax ")
#     while not (user_input == 'A' or user_input == 'B'):
#         user_input = raw_input("Enter either A or B ").upper()
#     if user_input == 'A':
#         profit_and_loss()
#     elif user_input == 'B':
#         calc_loss()
#     else:
#         print("Exit")
#
#
#
#
