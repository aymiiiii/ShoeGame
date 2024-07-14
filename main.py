import subprocess
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import json
import os

def open_customer_login():
    customer_login_window = Toplevel()
    customer_login_window.title("Customer Login")
    customer_login_window.geometry("1000x600")
    customer_login_window.config(bg="black")
    customer_login_window.resizable(False, False)
    app.withdraw()

    image_path_logo = "IMAGES/LOGO.png"
    img = Image.open(image_path_logo)
    img = img.resize((500, 500), Image.LANCZOS)
    img_logo = ImageTk.PhotoImage(img)

    label_logo = Label(customer_login_window, image=img_logo, bg="black")
    label_logo.image = img_logo
    label_logo.place(x=10, y=30)

    frames = Frame(customer_login_window, width=700, height=900, bg="white")
    frames.place(x=550, y=0)

    login_Lbl1 = Label(frames, text="Log In", font=("Sans-serif", 30, "bold"), fg="black", bg="white")
    login_Lbl1.place(x=170, y=70)

    username_Lbl1 = Label(frames, text="Username", font=("Sans-serif", 10), fg="black", bg="white")
    username_Lbl1.place(x=70, y=210)

    global username_Entry1
    username_Entry1 = Entry(frames, width=30, relief="ridge")
    username_Entry1.place(x=160, y=212)

    password_Lbl1 = Label(frames, text="Password", font=("Sans-serif", 10), fg="black", bg="white")
    password_Lbl1.place(x=70, y=290)

    global password_Entry1
    password_Entry1 = Entry(frames, width=30, show="*", relief="ridge")
    password_Entry1.place(x=160, y=292)

    def show_password():
        if password_Entry1.cget('show') == '*':
            password_Entry1.config(show='')
        else:
            password_Entry1.config(show='*') 

    show_Pass = Checkbutton(frames, text="Show Password", font=("sans-serif", 7), bg="white", command=show_password)
    show_Pass.place(x=160, y=320)

    def login_user():
        username = username_Entry1.get()
        password = password_Entry1.get()

        if username and password:
            if check_credentials(username, password):
                customer_login_window.destroy()
                start_shop(username)  # Call function to start shop with username
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "Username and password are required.")

    login_Btn1 = Button(frames, text="Log In", font=("Sans-serif", 9, "bold"), bg="black", fg="white", width=25, relief="flat", command=login_user)
    login_Btn1.place(x=160, y=390)

    not_Register = Label(frames, text="Don't have Account ?", font=("Sans-serif", 7), fg="black", bg="white")
    not_Register.place(x=170, y=430)

    register_Btn1 = Button(frames, text="Create Account", font=("Sans-serif", 7), fg="black", bg="white", relief="flat", command=open_create_account_window)
    register_Btn1.place(x=264, y=429)

    customer_login_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(customer_login_window))

def on_closing(window):
    app.deiconify()
    window.destroy()

def check_credentials(username, password):
    filename = 'login_details_customer.json'

    if os.path.exists(filename):
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
            users = data.get('login_details')

            for user in users:
                if user['username'] == username and user['password'] == password:
                    return True
    return False

def write_to_json_customer(username, password):
    login_details = {
        'username': username,
        'password': password
    }
    
    filename = 'login_details_customer.json'
    if os.path.exists(filename):
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
            if 'login_details' not in data:
                data['login_details'] = []
    else:
        data = {'login_details': []}

    data['login_details'].append(login_details)

    with open(filename, 'w') as create_file:
        json.dump(data, create_file, indent=4)

# CREATE ACCOUNT WINDOW
def open_create_account_window():
    create_account_window = Toplevel()
    create_account_window.title("Create Account")
    create_account_window.geometry("600x400")
    create_account_window.config(bg="black")
    create_account_window.resizable(False, False)

    register_label = Label(create_account_window, text="Create Account", font=("Sans-serif", 20, "bold"), fg="#38B6FF", bg="black")
    register_label.pack(pady=30)

    username_label1 = Label(create_account_window, text="Username", font=("Sans-serif", 10), fg="#38B6FF", bg="black")
    username_label1.place(x=90, y=130)

    global username_entry1
    username_entry1 = Entry(create_account_window, width=30, relief="flat")
    username_entry1.place(x=220, y=132)

    password_label1 = Label(create_account_window, text="Password", font=("Sans-serif", 10), fg="#38B6FF", bg="black")
    password_label1.place(x=90, y=190)

    global password_entry1
    password_entry1 = Entry(create_account_window, width=30, relief="flat", show="*")
    password_entry1.place(x=220, y=192)

    def register_customer():
        username = username_entry1.get()
        password = password_entry1.get()

        if username and password:
            write_to_json_customer(username, password)
            messagebox.showinfo("Success", "Account created successfully!")
            create_account_window.destroy()
        else:
            messagebox.showerror("Error", "Username and password are required.")

    register_button1 = Button(create_account_window, text="Register", font=("Sans-serif", 8, "bold"), bg="#38B6FF", fg="black", width=25, relief="flat", command=register_customer)
    register_button1.place(x=220, y=280)


# ADMIN LOG IN WINDOW
def open_admin_login():
    admin_login_window = Toplevel()
    admin_login_window.title("Admin Login")
    admin_login_window.geometry("1000x600")
    admin_login_window.config(bg="black")
    app.withdraw()

    image_path_logo = "IMAGES/LOGO.png"
    img = Image.open(image_path_logo)
    img = img.resize((500, 500), Image.LANCZOS)
    img_logo = ImageTk.PhotoImage(img)

    label_logo = Label(admin_login_window, image=img_logo, bg="black")
    label_logo.image = img_logo
    label_logo.place(x=10, y=30)

    frame2 = Frame(admin_login_window, width=700, height=900, bg="white")
    frame2.place(x=550, y=0)

    login_Lbl = Label(frame2, text="Log In", font=("Sans-serif", 30, "bold"), fg="black", bg="white")
    login_Lbl.place(x=170, y=70)

    username_Lbl = Label(frame2, text="Username", font=("Sans-serif", 10), fg="black", bg="white")
    username_Lbl.place(x=70, y=210)

    global username_Entry2
    username_Entry2 = Entry(frame2, width=30, relief="ridge")
    username_Entry2.place(x=160, y=212)

    password_Lbl2 = Label(frame2, text="Password", font=("Sans-serif", 10), fg="black", bg="white")
    password_Lbl2.place(x=70, y=290)

    global password_Entry2
    password_Entry2 = Entry(frame2, width=30, show="*", relief="ridge")
    password_Entry2.place(x=160, y=292)

    def show_password():
        if password_Entry2.cget('show') == '*':
            password_Entry2.config(show='')
        else:
            password_Entry2.config(show='*') 

    show_Pass = Checkbutton(frame2, text="Show Password", font=("sans-serif", 7), bg="white", command=show_password)
    show_Pass.place(x=160, y=320)

    def login_admin():
        username = username_Entry2.get()
        password = password_Entry2.get()

        if username and password:
            if credentials_check(username, password):
                admin_login_window.destroy()
                start_admin(username)  # Call function to start shop with username
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "Username and password are required.")

    login_Btn2 = Button(frame2, text="Log In", font=("Sans-serif", 9, "bold"), bg="black", fg="white", width=25, relief="flat", command=login_admin)
    login_Btn2.place(x=160, y=390)

    not_Register = Label(frame2, text="Don't have Account ?", font=("Sans-serif", 7), fg="black", bg="white")
    not_Register.place(x=170, y=430)

    register_Btn2 = Button(frame2, text="Create Account", font=("Sans-serif", 7), fg="black", bg="white", relief="flat", command=open_create_account_window2)
    register_Btn2.place(x=264, y=429)

    admin_login_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(admin_login_window))

def credentials_check(username, password):
    filename = 'login_details_admin.json'

    if os.path.exists(filename):
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
            users = data.get('login_details_admin')

            for user in users:
                if user['username'] == username and user['password'] == password:
                    return True
    return False

def write_to_json_admin(username, password):
    login_details_admin = {
        'username': username,
        'password': password
    }
    filename = 'login_details_admin.json'

    if os.path.exists(filename):
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
            if 'login_details_admin' not in data:
                data['login_details_admin'] = []
    else:
        data = {'login_details_admin': []}

    data['login_details_admin'].append(login_details_admin)

    with open(filename, 'w') as create_file:
        json.dump(data, create_file, indent=4)

def open_create_account_window2():
    create_account_window2= Toplevel()
    create_account_window2.title("Create Account")
    create_account_window2.geometry("600x400")
    create_account_window2.config(bg="black")
    create_account_window2.resizable(False, False)

    register_label = Label(create_account_window2, text="Create Account", font=("Sans-serif", 20, "bold"), fg="#38B6FF", bg="black")
    register_label.pack(pady=30)

    username_label2 = Label(create_account_window2, text="Username", font=("Sans-serif", 10), fg="#38B6FF", bg="black")
    username_label2.place(x=90, y=130)

    global username_entry2
    username_entry2 = Entry(create_account_window2, width=30, relief="flat")
    username_entry2.place(x=220, y=132)

    password_label2 = Label(create_account_window2, text="Password", font=("Sans-serif", 10), fg="#38B6FF", bg="black")
    password_label2.place(x=90, y=190)

    global password_entry2
    password_entry2 = Entry(create_account_window2, width=30, relief="flat", show="*")
    password_entry2.place(x=220, y=192)

    
    def register_admin():
        username = username_entry2.get()
        password = password_entry2.get()

        if username and password:
            write_to_json_admin(username, password)
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Username and password are required.")

    register_button2 = Button(create_account_window2, text="Register", font=("Sans-serif", 8, "bold"), bg="#38B6FF", fg="black", width=25, relief="flat", command=register_admin)
    register_button2.place(x=220, y=280)

# MAIN WINDOW
app = Tk()
app.title("Main")
app.geometry("800x500")
app.config(bg="black")
app.resizable(False, False)

# IMAGES BUTTON
image_path_client = "IMAGES/CLIENT.png"
photo_client = PhotoImage(file=image_path_client)

image_path_admin = "IMAGES/ADMIN.png"
photo_admin = PhotoImage(file=image_path_admin)

# BUTTONS for CLIENT and ADMIN
button_client = Button(app, image=photo_client, borderwidth=0, highlightthickness=0, command=open_customer_login)
button_client.place(x=220, y=160)

button_admin = Button(app, image=photo_admin, borderwidth=0, highlightthickness=0, command=open_admin_login)
button_admin.place(x=470, y=160)

# LABELS for CLIENT and ADMIN
label_client = Label(app, text="CUSTOMER", font=("Sans-serif", 13, "bold"), fg="#38B6FF", bg="black")
label_client.place(x=220, y=270)

label_admin = Label(app, text="ADMIN", font=("Sans-serif", 13, "bold"), fg="#38B6FF", bg="black")
label_admin.place(x=480, y=270)

def start_shop(username):
    try:
        subprocess.Popen(['python', 'shop.py', username])
    except Exception as e:
        print(f"Error starting shop.py: {e}")

def start_admin(username):
    try:
        subprocess.Popen(['python', 'admin.py', username])
    except Exception as e:
        print(f"Error starting admin.py: {e}")

# MAIN TKINTER EVENT LOOP
app.mainloop()

