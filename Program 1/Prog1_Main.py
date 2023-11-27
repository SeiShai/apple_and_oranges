import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# functions
def confirm():
    name = name_entry.get()
    address = address_entry.get()

    if not all(char.isalpha() or char.isspace() for char in name):
        messagebox.showerror('Invalid', 'Please enter a valid name')
        return

    if not address:
        messagebox.showerror('Error', 'Address field should not be blank')
        return

    if confirmation_var.get() == 'not certified':
        messagebox.showwarning("Confirmation error", "Please certify that the details provided are accurate ")
        return

    if name and address and confirmation_var:

        root.destroy()

        def calculate_amount(price_per_item, quantity):
            try:
                quantity = int(quantity)
                if quantity < 0:
                    raise ValueError("Quantity should be a non-negative integer.")

                amount = price_per_item * quantity
                return amount
            except ValueError as e:
                return str(e)

        # Purchase function
        def purchase():
            apple_quantity = apple_quantity_entry.get()
            orange_quantity = orange_quantity_entry.get()

            apple_price = calculate_amount(20, apple_quantity)
            orange_price = calculate_amount(25, orange_quantity)

            if any(not entry for entry in (apple_quantity, orange_quantity)):
                messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
                return

            if not (apple_quantity.isdigit() and orange_quantity.isdigit()):
                messagebox.showerror('Invalid', 'Please enter valid amounts')
                return

            total_cost = apple_price + orange_price

            receipt_text = (
                f"-----Purchase Confirmed-----\n\n"
                f"Customer Information\n"
                f"Name: {name}\n"
                f"Address: {address}\n\n"
                f"Items Purchased\n\n"
                f"Apple Quantity: ₱20 x {apple_quantity} = ₱{apple_price}\n"
                f"Orange Quantity: ₱25 x {orange_quantity} = ₱{orange_price}\n\n"
                f"Total Cost: ₱ {total_cost}"
            )

            shop_window.destroy()

            # Receipt_Window
            receipt_window = ctk.CTk()
            receipt_window.title("Ship Shop")
            receipt_window.geometry('700x400')
            receipt_window.resizable(0, 0)

            def close():
                receipt_window.destroy()

            # Images
            receipt_vector_data = Image.open("receipt_vector.png")
            receipt_vector = CTkImage(dark_image=receipt_vector_data,
                                      light_image=receipt_vector_data,
                                      size=(350, 400))

            CTkLabel(receipt_window, text="", image=receipt_vector).pack(expand=True, fill='both', side="right")

            # GUI_Components
            receipt_frame = CTkFrame(receipt_window, width=350, height=400, fg_color="#ffffff")
            receipt_frame.pack_propagate(0)
            receipt_frame.pack(expand=True, fill='both', side="left")

            receipt_text_label = CTkLabel(receipt_frame, text=receipt_text, text_color='#7E7E7E',
                                          anchor="w", justify="center", font=("Times new roman", 20))
            receipt_text_label.place(relx=0.5, rely=0.4, anchor='center')

            close_button = CTkButton(receipt_frame, text='Close', command=close)
            close_button.place(relx=0.5, rely=0.85, anchor='center')

            receipt_window.mainloop()


        # Shop_window
        shop_window = ctk.CTk()
        shop_window.title("Ship Shop")
        shop_window.geometry('700x400')
        shop_window.resizable(0, 0)

        # Images
        apple_vector_data = Image.open("apples.png")
        apple_vector = CTkImage(dark_image=apple_vector_data,
                                light_image=apple_vector_data,
                                size=(350, 370))

        orange_vector_data = Image.open("oranges.png")
        orange_vector = CTkImage(dark_image=orange_vector_data,
                                 light_image=orange_vector_data,
                                 size=(350, 370))

        # GUI
        products_frames = CTkFrame(shop_window, width=700, height=370)
        products_frames.pack()

        # Apple product
        apple_label = CTkLabel(products_frames, text='', image=apple_vector, width=350, height=370)
        apple_label.pack(side='left', fill='both', expand=True)

        apple_price = CTkLabel(apple_label, justify='center', bg_color='#FFF0DE', text='₱20 per Apple',
                               font=("Times new roman", 20), text_color='#992e2e')
        apple_price.place(relx=0.25, rely=0.93, anchor='center')

        apple_quantity_entry = CTkEntry(apple_label, width=135, corner_radius=10, border_width=1, bg_color='#FFF0DE',
                                        placeholder_text='Amount of apples', justify='center')
        apple_quantity_entry.place(relx=0.67, rely=0.93, anchor='center')

        # Orange Product
        orange_label = CTkLabel(products_frames, text='', image=orange_vector, width=350, height=370)
        orange_label.pack(side='right', fill='both', expand=True)

        orange_price = CTkLabel(orange_label, justify='center', bg_color='#FFF0DE', text='₱25 per Orange',
                                font=("Times new roman", 20), text_color='#992e2e')
        orange_price.place(relx=0.25, rely=0.93, anchor='center')

        orange_quantity_entry = CTkEntry(orange_label, width=135, corner_radius=10, border_width=1, bg_color='#FFF0DE',
                                         placeholder_text='Amount of oranges', justify='center')
        orange_quantity_entry.place(relx=0.67, rely=0.93, anchor='center')

        # Buttons
        purchase_button = CTkButton(shop_window, text='Purchase', command=purchase, width=700)
        purchase_button.pack(side='bottom', fill='both', expand=True)

        shop_window.mainloop()

# main_window
root = ctk.CTk()
root.title("Ship Ship")
root.geometry('700x400')
root.resizable(0, 0)

# GUI_components
side_vector_data = Image.open("side-vector.png")
side_vector = CTkImage(dark_image=side_vector_data,
                       light_image=side_vector_data,
                       size=(350, 400))

name_icon_data = Image.open('Name.png')
name_icon = CTkImage(dark_image=name_icon_data,
                      light_image=name_icon_data,
                      size=(20, 20))

address_icon_data = Image.open("Address.png")
address_icon = CTkImage(dark_image=address_icon_data,
                         light_image=address_icon_data,
                         size=(20, 20))

CTkLabel(root, text="", image=side_vector).pack(expand=True, side="left")

# Frame
login_frame = CTkFrame(root, width=350, height=400, fg_color="#ffffff")
login_frame.pack_propagate(0)
login_frame.pack(expand=True, side="right")

# Labels and Entries
welcome_label = CTkLabel(login_frame,
         text="Welcome to ShipShop!",
         text_color="#4ab5bd",
         anchor="w",
         justify="left",
         font=("Arial Bold", 27))
welcome_label.pack(anchor="w", pady=(20, 5), padx=(12, 0))

sign_label = CTkLabel(login_frame,
         text="Please provide your name and address",
         text_color="#7E7E7E",
         anchor="w",
         justify="left",
         font=("Arial Bold", 12))
sign_label.pack(anchor="w", padx=(12, 0))

name_label = CTkLabel(login_frame,
         text="  Name:",
         text_color="#1e8881",
         anchor="w",
         justify="left",
         font=("Arial Bold", 14),
         image=name_icon, compound="left")
name_label.pack(anchor="w", pady=(25, 0), padx=(25, 0))

name_entry = CTkEntry(login_frame,
         width=300,
         placeholder_text='Enter Full Name',
         fg_color="#EEEEEE",
         border_color="#1e8881",
         border_width=1,
         text_color="#000000")
name_entry.pack(anchor="w", padx=(25, 0))

address_label = CTkLabel(login_frame,
         text="  Address:",
         text_color="#1e8881",
         anchor="w",
         justify="left",
         font=("Arial Bold", 14),
         image=address_icon,
         compound="left")
address_label.pack(anchor="w", pady=(21, 0), padx=(25, 0))

address_entry = CTkEntry(login_frame,
         placeholder_text='Enter Address',
         width=300,
         fg_color="#EEEEEE",
         border_color="#1e8881",
         border_width=1,
         text_color="#000000")
address_entry.pack(anchor="w", padx=(25, 0))

confirmation_var = customtkinter.StringVar(value="not certified")
confirmation_checkbox = CTkCheckBox(login_frame,
                                    border_color='#1e8881',
                                    checkbox_width=15,
                                    checkbox_height=15,
                                    corner_radius=2,
                                    variable=confirmation_var,
                                    text='I certify that the details provided are accurate.',
                                    font=("Arial Bold", 12),
                                    text_color="#1e8881")
confirmation_checkbox.pack(anchor="w", pady=(21, 0), padx=(25, 0))

Confirm_button = CTkButton(login_frame,
                         command=confirm,
                         text="Confirm",
                         fg_color="#1e8881",
                         hover_color="#E44982",
                         font=("Arial Bold", 12),
                         text_color="#ffffff",
                         width=300)
Confirm_button.pack(anchor="w", pady=(30, 0), padx=(25, 0))

root.mainloop()
