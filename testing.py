# import Tkinter as tk
# from Tkinter import *
#
#
# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#
#     def show(self):
#         self.lift
#
#
# class MenuScreen(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="Hey there")
#         label.pack(side="top", fill="both", expand=True)
#
#
# class ConverterScreen(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="Converter Page")
#         label.pack(side="top", fill="both", expand=True)
#
#
# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         first_page = MenuScreen(self)
#         second_page = ConverterScreen(self)
#
#         button_frame = tk.Frame(self)
#         container = tk.Frame(self)
#         button_frame.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)
#
#         first_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         second_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#
#         b1 = tk.Button(button_frame, text="Start Calculating", command=second_page.lift)
#
#         b1.pack(side="top")
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_title("FUT Converter")
#     root.wm_geometry("400x400")
#     root.mainloop()

# Small function for printing/formatting reasons
def print_statements():
    print("-----" * 11)


# Function which is used to calculate how much money you lose with a tax of 5%
def calc_loss():
    tax = 5
    percentage = 100

    while True:
        try:
            input_number = int(raw_input("Enter a number to calculate tax loss "))
            print_statements()
            print("You have entered {} to be calculated".format(input_number))
            print_statements()
            calculation = input_number / percentage * tax
            result = input_number - calculation
        except ValueError as e:
            print(e)
            continue
        else:
            print("After taking 5% off your number you are left with {}".format(result))
            break


#F Function which determines if you have made a profit or loss depending on your buy and sale price
def profit_and_loss():
    tax = 5
    percentage = 100

    while True:
        try:
            paid_number = int(raw_input("Enter how much you paid "))
            print("You have entered {} as how much you paid".format(paid_number))
            print_statements()
            sale_amount = int(raw_input("Enter the amount you will sell for "))
            print_statements()
            print("You have entered {} as how much you are selling for".format(sale_amount))
            tax_calc = sale_amount / percentage * tax
            amount_after_tax = sale_amount - tax_calc
            print_statements()
            print("The amount of tax for {} is {}".format(sale_amount, tax_calc))
            print_statements()
            print("After the sale and tax you have {}").format(amount_after_tax)
            final_result = amount_after_tax - paid_number
            print_statements()

        except ValueError as e:
            print(e)
            continue

        else:
            if amount_after_tax > paid_number:
                print("Profit: You made {} profit").format(abs(final_result))
            elif amount_after_tax < paid_number:
                print("Loss: You lost {}").format(abs(final_result))
            else:
                print("Broke even")
            break

# Main method
if __name__ in '__main__':

    user_input = ''
    print("FUT Calc:")
    print_statements()
    print("There is two options to choose from, these are:")
    print("Options are A: To Calculate Profit or Loss and B: Calculate tax ")
    while not (user_input == 'A' or user_input == 'B'):
        user_input = raw_input("Enter either A or B ").upper()
    if user_input == 'A':
        profit_and_loss()
    elif user_input == 'B':
        calc_loss()
    else:
        print("Exit")




