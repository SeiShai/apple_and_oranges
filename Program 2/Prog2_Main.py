import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# Main Window
root = ctk.CTk()
root.title("Ship Ship")
root.geometry('350x400')
root.resizable(0, 0)

# Images
main_bg_data = Image.open("main_bg.png")
main_bg = CTkImage(dark_image=main_bg_data,
                       light_image=main_bg_data,
                       size=(350, 400))

#GUI
window_frame = CTkFrame(root, width=700, height=400)
window_frame.pack()

window_label = CTkLabel(window_frame, text='', image=main_bg, width=700, height=400)
window_label.pack(fill='both', expand=True)

# Apples
apple_price_entry = CTkEntry(window_label, width=135, border_width=0, fg_color='#a8324a', bg_color='#a8324a',
                             placeholder_text='Apple Price', placeholder_text_color='white', justify=CENTER,
                             font=("times new roman", 15))
apple_price_entry.place(relx=0.26, rely=0.1, anchor='center')

apple_amount_entry = CTkEntry(window_label, width=135, border_width=0, fg_color='#a8324a', bg_color='#a8324a',
                             placeholder_text='Apple Amount', placeholder_text_color='white', justify=CENTER,
                             font=("times new roman", 15))
apple_amount_entry.place(relx=0.73, rely=0.1, anchor='center')

# Oranges
orange_price_entry = CTkEntry(window_label, width=135, border_width=0, fg_color='#a8324a', bg_color='#a8324a',
                             placeholder_text='Orange Price', placeholder_text_color='white', justify=CENTER,
                             font=("times new roman", 15))
orange_price_entry.place(relx=0.26, rely=0.2, anchor='center')

orange_amount_entry = CTkEntry(window_label, width=135, border_width=0, fg_color='#a8324a', bg_color='#a8324a',
                             placeholder_text='Orange Amount', placeholder_text_color='white', justify=CENTER,
                             font=("times new roman", 15))
orange_amount_entry.place(relx=0.73, rely=0.2, anchor='center')

# Cash
cash_amount_entry = CTkEntry(window_label, width=300, border_width=0, fg_color='#a8324a', bg_color='#a8324a',
                             placeholder_text='Enter Cash Amount', placeholder_text_color='white', justify=CENTER,
                             font=("times new roman", 15))
cash_amount_entry.place(relx=0.5, rely=0.3, anchor='center')

results_frame = CTkFrame(window_label, width= 300, height=200)
results_frame.place(relx=0.5, rely=0.705, anchor='center')

# Buttons
def confirm():
    try:
        apple_price = float(apple_price_entry.get())
        apple_amount = float(apple_amount_entry.get())
        orange_price = float(orange_price_entry.get())
        orange_amount = float(orange_amount_entry.get())
        cash_amount = float(cash_amount_entry.get())

        total_cost = (apple_price * apple_amount) + (orange_price * orange_amount)
        remaining_cash = cash_amount - total_cost

        # Display results
        results_text = (
            f"Price of Apples: ₱{apple_price}\n"
            f"Amount of Apples: {apple_amount}\n"
            f"Price of Oranges: ₱{orange_price}\n"
            f"Amount of Oranges: {orange_amount}\n"
            f"Amount of Cash: {cash_amount}\n"
            f"------------------------\n"
            f"Total Cost: ₱{total_cost}\n"
            f"Remaining Cash: ₱{remaining_cash}"
        )

        results_label = CTkLabel(results_frame, text=results_text, text_color='white',
                                 anchor="w", justify="left", font=("Times new roman", 15))
        results_label.place(relx=0.05, rely=0.4, anchor='w')

    except ValueError:
        messagebox.showerror('Invalid Input', 'Please enter valid numeric values for prices, amounts, and cash.')

confirm_button = CTkButton(window_label,
                         command=confirm,
                         text="Confirm",
                         fg_color="#1e8881",
                         bg_color='#1e8881',
                         hover_color="#E44982",
                         font=("times new roman", 15),
                         text_color="#ffffff",
                         width=300)
confirm_button.place(relx=0.5, rely=0.4, anchor='center')

root.mainloop()