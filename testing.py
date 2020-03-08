import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sys


# Small function for printing/formatting reasons
def print_statements():
    print("-----" * 11)


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.image = Image.open("football-pitch-png-2.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self.resize)

        self.background.image = self.image

    def resize(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def show(self):
        self.lift


class ConverterScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # First Calculation
        label = tk.Label(root, text="Converter Page")
        label.pack(side="top", fill="both", expand=False)
        label.place(x=145, y=1)
        label1 = tk.Label(root, text="Enter a number ")
        label1.place(x=30, y=50)
        self.entry1 = tk.Entry(root)
        self.entry1.place(x=150, y=50)
        b1 = tk.Button(text="Start Calculating", command=self.calc_loss)
        b1.place(x=145, y=95)

        # Second Calculation
        label2 = tk.Label(root, text="Bought Price")
        label2.place(x=30, y=175)
        self.entry2 = tk.Entry(root)
        self.entry2.place(x=150, y=175)
        label3 = tk.Label(root, text="Sell Price")
        label3.place(x=30, y=220)
        self.entry3 = tk.Entry(root)
        self.entry3.place(x=150, y=220)
        b2 = tk.Button(text="Start Calculating", command=self.profit_and_loss)
        b2.place(x=145, y=270)

        # Exit button to leave GUI
        buttonExit = tk.Button(text='EXIT', command=lambda: sys.exit())
        buttonExit.place(x=360, y=0)


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
                label1 = Label(root, text=round(result, 2))
                label1.place(x=175, y=130)
                print("After taking 5% off your number you are left with {}".format(round(result, 2)))
                break

    # Function which determines if you have made a profit or loss depending on your buy and sale price
    def profit_and_loss(self):
        tax = 5
        percentage = 100
        x2 = int(self.entry2.get())
        x3 = int(self.entry3.get())

        while True:
            try:
                print("You have entered {} as how much you paid".format(x2))
                print_statements()
                print_statements()
                print("You have entered {} as how much you are selling for".format(x3))
                tax_calc = x3 / percentage * tax
                amount_after_tax = x3 - tax_calc
                print_statements()
                print("The amount of tax for {} is {}".format(x3, tax_calc))
                print_statements()
                print("After the sale and tax you have {}".format(amount_after_tax))
                final_result = amount_after_tax - x2
                print_statements()
                label1 = Label(root, text=round(final_result, 2))
                label1.place(x=175, y=310)
            except ValueError as e:
                print(e)
                continue

            else:
                if amount_after_tax > x2:
                    print("Profit: You made {} profit".format(abs(final_result)))
                elif amount_after_tax < x2:
                    print("Loss: You lost {}".format(abs(final_result)))
                else:
                    print("Broke even")
                break


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        page = ConverterScreen(self)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    main = Page(root)
    main1 = MainView(root)
    root.wm_title("FUT Converter")
    root.wm_geometry("400x400")
    main.pack(fill=BOTH, expand=True)
    main1.pack(fill=BOTH, expand=True)

    root.mainloop()
