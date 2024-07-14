from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk
from location import regions, province_select, municipality_select, brgy_select
import os
import json
import random

shop_window = Tk()
shop_window.title("ShoeGame")
shop_window.geometry("1300x850")
shop_window.resizable(False, False)
icon_path = "IMAGES/ICON.ico"  # Replace with your icon file path
shop_window.iconbitmap(icon_path)

cart_items = []

# Function to raise a frame
def show_frame(frame):
    frame.tkraise()

# Function to clear all widgets in frame5 (Cart display)
def clear_cart_widgets():
    for widget in frame5.winfo_children():
        widget.destroy()
    cart_items.clear()
    update_cart_display()

# Function to update cart display
def update_cart_display():
    total_price = sum(item['price'] for item in cart_items)
    total_items = len(cart_items)

    # Clear previous items in the cart display
    for widget in frame5.winfo_children():
        if isinstance(widget, Label) and widget != shopping_Lbl and widget != line and widget != total_items_label:
            widget.destroy()

    y_offset = 140
    for item in cart_items:
        item_label = Label(frame5, text=f"{item['name']}  Size: {item['size']}  Price: ₱{item['price']}", font=("sans-serif", 12), bg="white", fg="black")
        item_label.place(x=80, y=y_offset)
        y_offset += 30
    
    # Display total price
    total_label = Label(frame5, text=f"Total: ₱{total_price}", font=("sans-serif", 14, "bold"), bg="white", fg="black")
    total_label.place(x=80, y=y_offset + 30)

    # Display total items count
    total_items_label.config(text=f"Total Items: {total_items}")

    # Save cart items to JSON file with only 'name' and 'size'
    simplified_cart_items = [{'name': item['name'], 'size': item['size'], 'price': item['price']} for item in cart_items]
    with open('cart_items.json', 'w') as file:
        json.dump(simplified_cart_items, file, indent=4)

# Function to calculate the total cost
def calculate_total():
    total = sum(item['price'] for item in cart_items)
    return total

# Function to create Buy Window with Combobox and Add to Cart button
# Sample refactored function to create a buy window
def open_buy_window(item_name, sizes, prices):
    def add_to_cart():
        selected_size = size_combo.get()
        selected_price = prices[sizes.index(selected_size)]

        cart_items.append({'name': item_name, 'size': selected_size, 'price': selected_price})
        update_cart_display()
        buy_window.destroy()

    buy_window = Toplevel(shop_window)
    buy_window.title(f"Select Size for {item_name}")
    buy_window.geometry("500x350")
    buy_window.config(bg="black")
    buy_window.resizable(False, False)
    
    label = Label(buy_window, text=f"Select Size for {item_name}", font=("sans-serif", 12, "bold"), fg="#38B6FF", bg="black")
    label.pack(pady=10)
    
    size_combo = Combobox(buy_window, values=sizes, state="readonly", font=("sans-serif", 10), width=5)
    size_combo.pack(pady=10)
    size_combo.current(0)  # Set default selection

    for idx, size in enumerate(sizes):
        price_label = Label(buy_window, text=f"{size}: ₱{prices[idx]}", font=("sans-serif", 10), bg="black", fg="#38B6FF")
        price_label.pack()

    add_order = Button(buy_window, text="Add to Cart", font=("sans-serif", 10, "bold"), width=15, height=1, bg="#38B6FF", fg="black", relief="flat", command=add_to_cart)
    add_order.pack(pady=20)



# FRAME1
frame1 = Frame(shop_window, width=1300, height=80, bg="black")
frame1.place(x=0, y=0)

# BUTTONS IN FRAME1 WHICH IS THE NAV BAR
button1 = Button(frame1, 
                 text="HOME", 
                 font=("sans-serif", 12, "bold"), 
                 width=10, 
                 activebackground="black", 
                 bd=0 , 
                 bg="black", 
                 cursor="hand2", 
                 fg="white", 
                 relief="flat", 
                 command=lambda: show_frame(frame2))
button1.place(x=380, y=20)

button2 = Button(frame1, 
                 text="SHOES", 
                 font=("sans-serif", 12, "bold"), 
                 width=10, 
                 activebackground="black", 
                 bd=0, 
                 bg="black", 
                 cursor="hand2", 
                 fg="white", 
                 relief="flat", 
                 command=lambda: show_frame(frame3))
button2.place(x=580, y=20)

button3 = Button(frame1, 
                 text="CLOTHES", 
                 font=("sans-serif", 12, "bold"), 
                 width=10, 
                 activebackground="black", 
                 bd=0, 
                 bg="black", 
                 cursor="hand2", 
                 fg="white", 
                 relief="flat", 
                 command=lambda: show_frame(frame4))
button3.place(x=780, y=20)

image_path_cart = "IMAGES/CART.png"
photo_cart = PhotoImage(file=image_path_cart)
button_cart = Button(frame1, image=photo_cart, relief="flat", width=25, activebackground="whitesmoke", bd=0, height=25, cursor="hand2", command=lambda: show_frame(frame5))
button_cart.place(x=1100, y=24)

image_path_logo = "IMAGES/LOGOUT.png"
photo_logo = PhotoImage(file=image_path_logo)
photo_logo_resized = photo_logo.subsample(1, 1)

def logout():
    shop_window.destroy()  # Destroy the shop window
    import main

button_logout = Button(frame1, 
                       image=photo_logo_resized, relief="flat", width=95, height=40, command=logout, activebackground="whitesmoke", bd=0, cursor="hand2")
button_logout.place(x=1160, y=15)

# HOME FRAME (frame2)
frame2 = Frame(shop_window, width=1300, height=770)
frame2.place(x=0, y=80)

home_image = PhotoImage(file="IMAGES/SHOES.png")
image_label = Label(frame2, image=home_image)
image_label.pack()

# SHOES FRAME (frame3)
frame3 = Frame(shop_window, width=1300, height=770, bg="white")
frame3.place(x=0, y=80)

# ================ AirJordanFlightMVP1Low ================
AirJordanFlightMVP1Low = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1Low.place(x=60, y=70)
AirJordanFlightMVP1Low_image = PhotoImage(file="IMAGES/SHOE1.png")
image1 = Label(AirJordanFlightMVP1Low, image=AirJordanFlightMVP1Low_image)
image1.place(x=0, y=0)

# Prices for AirJordanFlightMVP1Low
AirJordanFlightMVP1Low_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1Low_prices = [1195, 2195, 3195, 4195, 5195, 6195, 7195]

# Function call with arguments
buy1 = Button(AirJordanFlightMVP1Low, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Low", AirJordanFlightMVP1Low_sizes, AirJordanFlightMVP1Low_prices))
buy1.place(x=70, y=240)

# ================ AirJordanFlightMVP1LowSe ================
AirJordanFlightMVP1LowSe = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1LowSe.place(x=360, y=70)
AirJordanFlightMVP1LowSe_image = PhotoImage(file="IMAGES/SHOE2.png")
image2 = Label(AirJordanFlightMVP1LowSe, image=AirJordanFlightMVP1LowSe_image)
image2.place(x=0, y=0)

# Prices for AirJordanFlightMVP1LowSe
AirJordanFlightMVP1LowSe_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1LowSe_prices = [1519, 2519, 3519, 4519, 5519, 6519, 7519]

# Function call with arguments
buy2 = Button(AirJordanFlightMVP1LowSe, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Low Se", AirJordanFlightMVP1LowSe_sizes, AirJordanFlightMVP1LowSe_prices))
buy2.place(x=70, y=240)

# =============== AirJordanFlightMVP1ElevateLow ================
AirJordanFlightMVP1ElevateLow = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1ElevateLow.place(x=660, y=70)
AirJordanFlightMVP1ElevateLow_image = PhotoImage(file="IMAGES/SHOE3.png")
image3 = Label(AirJordanFlightMVP1ElevateLow, image=AirJordanFlightMVP1ElevateLow_image)
image3.place(x=0, y=0)

# Prices for AirJordanFlightMVP1ElevateLow
AirJordanFlightMVP1ElevateLow_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1ElevateLow_prices = [1095, 2095, 3095, 4095, 5095, 6095, 7095]

# Function call with arguments
buy3 = Button(AirJordanFlightMVP1ElevateLow, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Elevate Low", AirJordanFlightMVP1ElevateLow_sizes, AirJordanFlightMVP1ElevateLow_prices))
buy3.place(x=70, y=240)

# ================ AirJordanFlightMVP1LowBlue ==============
AirJordanFlightMVP1LowBlue = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1LowBlue.place(x=970, y=70)
AirJordanFlightMVP1LowBlue_image = PhotoImage(file="IMAGES/SHOE4.png")
image4 = Label(AirJordanFlightMVP1LowBlue, image=AirJordanFlightMVP1LowBlue_image)
image4.place(x=0, y=0)

# Prices for AirJordanFlightMVP1LowBlue
AirJordanFlightMVP1LowBlue_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1LowBlue_prices = [1095, 2095, 3095, 4095, 5095, 6095, 7095]

# Function call with arguments
buy4 = Button(AirJordanFlightMVP1LowBlue, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Low Blue", AirJordanFlightMVP1LowBlue_sizes, AirJordanFlightMVP1LowBlue_prices))
buy4.place(x=70, y=240)

# =============== JordanFlightMVPSpizikeyLow ===============
JordanFlightMVPSpizikeyLow = Frame(frame3, width=250, height=280, bg="white")
JordanFlightMVPSpizikeyLow.place(x=60, y=420)
JordanFlightMVPSpizikeyLow_image = PhotoImage(file="IMAGES/SHOE5.png")
image5 = Label(JordanFlightMVPSpizikeyLow, image=JordanFlightMVPSpizikeyLow_image)
image5.place(x=0, y=0)

# Prices for JordanFlightMVPSpizikeyLow
JordanFlightMVPSpizikeyLow_sizes = ["39", "40", "41", "42", "43", "44", "45"]
JordanFlightMVPSpizikeyLow_prices = [1096, 2096, 3096, 4096, 5096, 6096, 7096]

# Function call with arguments
buy5 = Button(JordanFlightMVPSpizikeyLow, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Flight MVP Spizikey Low", JordanFlightMVPSpizikeyLow_sizes, JordanFlightMVPSpizikeyLow_prices))
buy5.place(x=70, y=240)

# =============== AirJordanFlightMVP1RetroHihghOGLatte ===============
AirJordanFlightMVP1RetroHihghOGLatte = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1RetroHihghOGLatte.place(x=360, y=420)
AirJordanFlightMVP1RetroHihghOGLatte_image = PhotoImage(file="IMAGES/SHOE6.png")
image6 = Label(AirJordanFlightMVP1RetroHihghOGLatte, image=AirJordanFlightMVP1RetroHihghOGLatte_image)
image6.place(x=0, y=0)

# Prices for AirJordanFlightMVP1RetroHihghOGLatte
AirJordanFlightMVP1RetroHihghOGLatte_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1RetroHihghOGLatte_prices = [1519, 2519, 3519, 4519, 5519, 6519, 7519]

# Function call with arguments
buy6 = Button(AirJordanFlightMVP1RetroHihghOGLatte, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Retro HihghOG Latte", AirJordanFlightMVP1RetroHihghOGLatte_sizes, AirJordanFlightMVP1RetroHihghOGLatte_prices))
buy6.place(x=70, y=240)

# =============== Tatum2PF ===============
Tatum2PF = Frame(frame3, width=250, height=280, bg="white")
Tatum2PF.place(x=660, y=420)
Tatum2PF_image = PhotoImage(file="IMAGES/SHOE7.png")
image7 = Label(Tatum2PF, image=Tatum2PF_image)
image7.place(x=0, y=0)

# Prices for Tatum2PF
Tatum2PF_sizes = ["39", "40", "41", "42", "43", "44", "45"]
Tatum2PF_prices = [1095, 2095, 3095, 4095, 5095, 6095, 7095]

# Function call with arguments
buy7 = Button(Tatum2PF, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Tatum 2 PF", Tatum2PF_sizes, Tatum2PF_prices))
buy7.place(x=70, y=240)

# =============== AirJordanFlightMVP1RetroHighOG ===============
AirJordanFlightMVP1RetroHighOG = Frame(frame3, width=250, height=280, bg="white")
AirJordanFlightMVP1RetroHighOG.place(x=970, y=420)
AirJordanFlightMVP1RetroHighOG_image = PhotoImage(file="IMAGES/SHOE8.png")
image8 = Label(AirJordanFlightMVP1RetroHighOG, image=AirJordanFlightMVP1RetroHighOG_image)
image8.place(x=0, y=0)

# Prices for AirJordanFlightMVP1RetroHighOG
AirJordanFlightMVP1RetroHighOG_sizes = ["39", "40", "41", "42", "43", "44", "45"]
AirJordanFlightMVP1RetroHighOG_prices = [1195, 2195, 3195, 4195, 5195, 6195, 7195]

# Function call with arguments
buy8 = Button(AirJordanFlightMVP1RetroHighOG, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Air Jordan Flight MVP1 Retro High OG", AirJordanFlightMVP1RetroHighOG_sizes, AirJordanFlightMVP1RetroHighOG_prices))
buy8.place(x=70, y=240)

# CLOTHES FRAME (frame4)
frame4 = Frame(shop_window, width=1300, height=770, bg="white")
frame4.place(x=0, y=80)

# ================ JordanFlightMVP ================
JordanFlightMVP = Frame(frame4, width=250, height=280, bg="white")
JordanFlightMVP.place(x=60, y=70)
JordanFlightMVP_image = PhotoImage(file="IMAGES/CLOTHE1.png")
image1 = Label(JordanFlightMVP, image=JordanFlightMVP_image)
image1.place(x=0, y=0)

# Sizes and prices for JordanFlightMVP
JordanFlightMVP_sizes = ["S", "M", "L", "XL"]
JordanFlightMVP_prices = [999, 1099, 1199, 3495]

# Function call with arguments
buy1 = Button(JordanFlightMVP, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Flight MVP", JordanFlightMVP_sizes, JordanFlightMVP_prices))
buy1.place(x=70, y=240)

# ================ Jordan ================
Jordan = Frame(frame4, width=250, height=280, bg="white")
Jordan.place(x=360, y=70)
Jordan_image = PhotoImage(file="IMAGES/CLOTHE2.png")
image2 = Label(Jordan, image=Jordan_image)
image2.place(x=0, y=0)

# Sizes and prices for Jordan
Jordan_sizes = ["S", "M", "L", "XL"]
Jordan_prices = [799, 899, 999, 1185]

# Function call with arguments
buy2 = Button(Jordan, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan", Jordan_sizes, Jordan_prices))
buy2.place(x=70, y=240)

# =============== JordanFlightEssentials ================
JordanFlightEssentials = Frame(frame4, width=250, height=280, bg="white")
JordanFlightEssentials.place(x=660, y=70)
JordanFlightEssentials_image = PhotoImage(file="IMAGES/CLOTHE3.png")
image3 = Label(JordanFlightEssentials, image=JordanFlightEssentials_image)
image3.place(x=0, y=0)

# Sizes and prices for JordanFlightEssentials
JordanFlightEssentials_sizes = ["S", "M", "L", "XL"]
JordanFlightEssentials_prices = [899, 999, 1099, 1195]

# Function call with arguments
buy3 = Button(JordanFlightEssentials, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Flight Essentials", JordanFlightEssentials_sizes, JordanFlightEssentials_prices))
buy3.place(x=70, y=240)

# ================ JordanSportJam ==============
JordanSportJam = Frame(frame4, width=250, height=280, bg="white")
JordanSportJam.place(x=970, y=70)
JordanSportJam_image = PhotoImage(file="IMAGES/CLOTHE4.png")
image4 = Label(JordanSportJam, image=JordanSportJam_image)
image4.place(x=0, y=0)

# Sizes and prices for JordanSportJam
JordanSportJam_sizes = ["S", "M", "L", "XL"]
JordanSportJam_prices = [1099, 1199, 2299, 4795]

# Function call with arguments
buy4 = Button(JordanSportJam, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Sport Jam", JordanSportJam_sizes, JordanSportJam_prices))
buy4.place(x=70, y=240)

# =============== JordanGolf ===============
JordanGolf = Frame(frame4, width=250, height=280, bg="white")
JordanGolf.place(x=60, y=420)
JordanGolf_image = PhotoImage(file="IMAGES/CLOTHE5.png")
image5 = Label(JordanGolf, image=JordanGolf_image)
image5.place(x=0, y=0)

# Sizes and prices for JordanGolf
JordanGolf_sizes = ["S", "M", "L", "XL"]
JordanGolf_prices = [2999, 4099, 6199, 8898]

# Function call with arguments
buy5 = Button(JordanGolf, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Golf", JordanGolf_sizes, JordanGolf_prices))
buy5.place(x=70, y=240)

# =============== Nocta ===============
Nocta = Frame(frame4, width=250, height=280, bg="white")
Nocta.place(x=360, y=420)
Nocta_image = PhotoImage(file="IMAGES/CLOTHE6.png")
image6 = Label(Nocta, image=Nocta_image)
image6.place(x=0, y=0)

# Sizes and prices for Nocta
Nocta_sizes = ["S", "M", "L", "XL"]
Nocta_prices = [1199, 2299, 3399, 4495]

# Function call with arguments
buy6 = Button(Nocta, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Nocta", Nocta_sizes, Nocta_prices))
buy6.place(x=70, y=240)

# =============== JordanBrooklynFleece ===============
JordanBrooklynFleece = Frame(frame4, width=250, height=280, bg="white")
JordanBrooklynFleece.place(x=660, y=420)
JordanBrooklynFleece_image = PhotoImage(file="IMAGES/CLOTHE7.png")
image7 = Label(JordanBrooklynFleece, image=JordanBrooklynFleece_image)
image7.place(x=0, y=0)

# Sizes and prices for JordanBrooklynFleece
JordanBrooklynFleece_sizes = ["S", "M", "L", "XL"]
JordanBrooklynFleece_prices = [899, 999, 1099, 2285]

# Function call with arguments
buy7 = Button(JordanBrooklynFleece, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Brooklyn Fleece", JordanBrooklynFleece_sizes, JordanBrooklynFleece_prices))
buy7.place(x=70, y=240)

# =============== JordanGolfBlack ===============
JordanGolfBlack = Frame(frame4, width=250, height=280, bg="white")
JordanGolfBlack.place(x=970, y=420)
JordanGolfBlack_image = PhotoImage(file="IMAGES/CLOTHE8.png")
image8 = Label(JordanGolfBlack, image=JordanGolfBlack_image)
image8.place(x=0, y=0)

# Sizes and prices for JordanGolfBlack
JordanGolfBlack_sizes = ["S", "M", "L", "XL"]
JordanGolfBlack_prices = [1099, 2199, 4299, 7898]

# Function call with arguments
buy8 = Button(JordanGolfBlack, text="BUY NOW", font=("sans-serif", 8, "bold"),activebackground="black", bd=0, width=15, height=1, bg="black", fg="white", relief="flat", command=lambda: open_buy_window("Jordan Golf Black", JordanGolfBlack_sizes, JordanGolfBlack_prices))
buy8.place(x=70, y=240)

frame5 = Frame(shop_window, width=1300, height=770, bg="white")
frame5.place(x=0, y=80)

shopping_Lbl = Label(frame5, text="Shopping Cart", font=("sans-serif", 20, "bold"), bg="white", fg="black")
shopping_Lbl.place(x=80, y=50)

line = Label(frame5, text="___________________________________________________________________________________________________________________________________________________________________________________________________________________", bg="white", fg="black")
line.place(x=80, y=90)

total_items_label = Label(frame5, text="Total Items: 0", font=("sans-serif", 20, "bold"), bg="white", fg="black")
total_items_label.place(x=920, y=58)


# =================== CHECKOUT ===========================

frame6 = Frame(shop_window, width=1300, height=770, bg="white")
frame6.place(x=0, y=80)

checkout_logo = "IMAGES/CHECKOUT.png"
check_Out = PhotoImage(file=checkout_logo)
check_Out = check_Out.subsample(1, 1)
checkout_Btn = Button(frame5, image=check_Out, relief="flat", width=90,bd=0, height=40, command=lambda: show_frame(frame6))
checkout_Btn.place(x=1005, y=620)

delivert_Info = Label(frame6, text="Delivery Information", font=("sans-serif", 25, "bold"), bg="white")
delivert_Info.place(x=470, y=60)

full_name = Label(frame6, text="Full Name:", font=("sans-serif", 12), bg="white")
full_name.place(x=100, y=180)
full_name_ent = Entry(frame6, font=("sans-serif", 12), relief="ridge", width=33)
full_name_ent.place(x=200, y=180)

phone_Number = Label(frame6, text="Phone Number:", font=("sans-serif", 12), bg="white")
phone_Number.place(x=100, y=280)
phone_Number_Ent = Entry(frame6, font=("sans-serif", 12), relief="ridge", width=28)
phone_Number_Ent.place(x=240, y=280)

email_Lbl = Label(frame6, text="Email:", font=("sans-serif", 12), bg="white")
email_Lbl.place(x=100, y=370)
email_Lbl_ent = Entry(frame6, font=("sans-serif", 12), relief="ridge", width=32)
email_Lbl_ent.place(x=200, y=370)

address_Lbl = Label(frame6, text="Address:", font=("sans-serif", 12), bg="white")
address_Lbl.place(x=100, y=470)
address_Lbl_ent = Entry(frame6, font=("sans-serif", 12), relief="ridge", width=32)
address_Lbl_ent.place(x=200, y=470)
    
region_Lbl = Label(frame6, text="Region:", font=("sans-serif", 12), bg="white")
region_Lbl.place(x=720, y=180)
region_combobox = ttk.Combobox(frame6)
region_combobox['values'] = regions
region_combobox.current(0)  
region_combobox.place(x=820, y=180, width=300, height=22)
region_combobox.set("Select Region")

def on_region_select(event):
        selected_region = region_combobox.get()
        province_values = province_select(selected_region)
        province_combobox.config(values=province_values)
        province_combobox.current(0)

region_combobox.bind("<<ComboboxSelected>>", on_region_select)

province_Lbl = Label(frame6, text="Province:", font=("sans-serif", 12), bg="white")
province_Lbl.place(x=720, y=280)

province_combobox = ttk.Combobox(frame6)
province_combobox.place(x=820, y=280, width=300, height=22)
province_combobox.set("Select Province")

def on_province_select(event):
        selected_region = region_combobox.get()
        selected_province = province_combobox.get()
        municipality_values = municipality_select(selected_region, selected_province)
        municipality_combobox.config(values=municipality_values)
        municipality_combobox.current(0)

province_combobox.bind("<<ComboboxSelected>>", on_province_select)

municipal_Lbl = Label(frame6, text="Municipal:", font=("sans-serif", 12), bg="white")
municipal_Lbl.place(x=720, y=370)

municipality_combobox = ttk.Combobox(frame6)
municipality_combobox.place(x=820, y=370, width=300, height=22)
municipality_combobox.set("Select Municipality")

def on_municipality_select(event):
        selected_region = region_combobox.get()
        selected_province = province_combobox.get()
        selected_municipality = municipality_combobox.get()
        barangay_values = brgy_select(selected_region, selected_province, selected_municipality)
        barangay_combobox.config(values=barangay_values)
        barangay_combobox.current(0)

municipality_combobox.bind("<<ComboboxSelected>>", on_municipality_select)

barangay_Lbl = Label(frame6, text="Barangay:", font=("sans-serif", 12), bg="white")
barangay_Lbl.place(x=720, y=470)

barangay_combobox = ttk.Combobox(frame6)
barangay_combobox.place(x=820, y=470, width=300, height=22)
barangay_combobox.set("Select Barangay")

Label(frame6, text="Payment Method:", font=("sans-serif", 12), bg="white").place(x=440, y=570)
payment_method_combo = Combobox(frame6, values=["Credit Card", "Debit Card", "Cash on Delivery"], state="readonly", font=("sans-serif", 12), width=25, height=20)
payment_method_combo.current(0)
payment_method_combo.place(x=580, y=570)

class OrderItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def proceed_checkout():
    full_name = full_name_ent.get()
    contact_number = phone_Number_Ent.get()
    email = email_Lbl_ent.get()
    address = address_Lbl_ent.get()
    region = region_combobox.get()
    province = province_combobox.get()
    municipality = municipality_combobox.get()
    barangay = barangay_combobox.get()
    payment = payment_method_combo.get()

    items = []
    for item in cart_items:
        items.append(OrderItem(item['name'], item['price']))

    total_cost = sum(item['price'] for item in cart_items)

    status = []  # Add a new variable for the order status

    # Generate a unique order number
    order_number = random.randint(10000000, 99999999)  # Generate a random 8-digit order number

    order_details = {
        "Order Number": order_number, 
        "Full Name": full_name,
        "Contact Number": contact_number,
        "Email": email,
        "Address": address,
        "Region": region,
        "Province": province,
        "Municipality": municipality,
        "Barangay": barangay,
        "Payment": payment,
        "Items": cart_items,
        "Total Cost": total_cost,
        "Status": status
    }

    filename = "order_details.json"
    if os.path.exists(filename):
        with open(filename, "r") as rwad_file:
            orders = json.load(rwad_file)
    else:
        orders = {"order_details":[]}
        with open(filename, "w") as write_file:
            json.dump(orders, write_file, indent=4)

    if 'order_details' not in orders:
        orders['order_details'] = []

    orders["order_details"].append(order_details)

    with open(filename, 'w') as update_file:
        json.dump(orders, update_file, indent=4)

    messagebox.showinfo("Order Confirmed", "Thank you for purchasing!")

    cart_items.clear()
    update_cart_display()
    reset_widgets()
    
checkout_button = Button(frame6, text="Proceed to Checkout", font=("sans-serif", 12, "bold"), width=25, height=2, bg="black", fg="white",relief="flat" , command=proceed_checkout)
checkout_button.place(x=550, y=650)



def reset_widgets():
    full_name_ent.delete(0, END)
    phone_Number_Ent.delete(0, END)
    email_Lbl_ent.delete(0, END)
    address_Lbl_ent.delete(0, END)
    region_combobox.set("Select Region")
    province_combobox.set("Select Province")
    municipality_combobox.set("Select Municipality")
    barangay_combobox.set("Select Barangay")
    payment_method_combo.current(0)


    cart_items.clear()
    update_cart_display()

show_frame(frame2)  # Display the home frame initially
shop_window.mainloop()