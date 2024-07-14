from tkinter import *
import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog
import os
import json
import fpdf
from reportlab.lib.pagesizes import TABLOID, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle 
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from io import BytesIO

def generate_bar_graph():
    size_counts = {}

    filename = 'order_details.json'
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)

        for order in orders["order_details"]:
            for item in order["Items"]:
                if item["size"] in size_counts:
                    size_counts[item["size"]] += 1
                else:
                    size_counts[item["size"]] = 1

    # Create a new figure and set the size
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(size_counts.keys(), size_counts.values(), color=[
           '#3498DB', '#E74C3C', '#2ECC71', '#F1C40F', '#E67E22', '#9B59B6'])
    ax.set_xlabel('Sizes')
    ax.set_ylabel('Number of Items')
    ax.set_title('Item Sizes')
    ax.grid(axis='y', linestyle='--', linewidth=0.5, color='lightgray', alpha=0.7)

    # Remove the spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))

    # Save the figure as an image
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    buffer.seek(0)

    # Convert the image to a PhotoImage
    image = Image.open(buffer)
    photo_image = ImageTk.PhotoImage(image)

    # Create a label with the image
    graph_label = Label(dash_frame, image=photo_image, bg='white')
    graph_label.image = photo_image
    graph_label.place(x=60, y=330)

def generate_pie_chart():
    # Clear previous pie chart if it exists
    for widget in dash_frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    status_counts = {"Delivered": 0, "To Ship": 0, "Pending": 0}

    filename = 'order_details.json'
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)

        for order in orders["order_details"]:
            if "Status" in order and len(order["Status"]) > 0:
                if order["Status"].lower() == "delivered":
                    status_counts["Delivered"] += 1
                elif order["Status"].lower() == "to ship":
                    status_counts["To Ship"] += 1
                elif order["Status"].lower() == "pending":
                    status_counts["Pending"] += 1

        labels = list(status_counts.keys())
        sizes = list(status_counts.values())

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=dash_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=530, y=330)
    else:
        print("File does not exist or is empty.")
    
def update_time():
    current_date = datetime.now().strftime('%B %d, %Y')
    current_time = datetime.now().strftime('%I:%M:%S %p')
    date_label.config(text=current_date)
    time_label.config(text=current_time)
    admin.after(1000, update_time)

def show_dashboard():
    dash_frame.tkraise()

def show_manage():
    manage_frame.tkraise()


admin = Tk()
admin.title("Admin")
admin.geometry("1300x850")
admin.config(bg="whitesmoke")
admin.resizable(False, False)

sidebar = Frame(width=350, height=850, bg="#F5F5F5")
sidebar.place(x=0, y=0)

image_path_sidebar = "IMAGES/PROFILE.png" 
image_sidebar = Image.open(image_path_sidebar)
image_sidebar_resized = image_sidebar.resize((230, 230), Image.LANCZOS)
photo_sidebar_resized = ImageTk.PhotoImage(image_sidebar_resized)
label_sidebar = Label(sidebar, image=photo_sidebar_resized, width=150, height=150)
label_sidebar.place(x=90, y=130)

admin_Lbl = Label(sidebar, text="Admin", font=("sans-serif", 15, "bold"), bg="whitesmoke")
admin_Lbl.place(x=130, y=290)

# Date and Time Labels
date_label = Label(sidebar, font=("sans-serif", 10, "bold"), bg="#F5F5F5")
date_label.place(x=130, y=20)
time_label = Label(sidebar, font=("sans-serif", 10, "bold"), bg="#F5F5F5")
time_label.place(x=130, y=50)
update_time()

icon_path = "IMAGES/DASHBOARD.png"  # Update the path to your icon image
icon_image = Image.open(icon_path)
icon_image_resized = icon_image.resize((40, 40), Image.LANCZOS)
icon_photo_resized = ImageTk.PhotoImage(icon_image_resized)
icon_label = Label(sidebar, image=icon_photo_resized, bg="#F5F5F5")
icon_label.place(x=50, y=430)

dash_Btn = Button(sidebar, text="Dashboard", font=("sans-serif", 15, "bold"), bg="whitesmoke", fg="black", activebackground="whitesmoke", bd=0, relief="flat", width=10, command=show_dashboard)
dash_Btn.place(x=120, y=435)

icon_path2 = "IMAGES/MANAGE.png"  # Update the path to your second icon image
icon_image2 = Image.open(icon_path2)
icon_image2_resized = icon_image2.resize((50, 50), Image.LANCZOS)
icon_photo2_resized = ImageTk.PhotoImage(icon_image2_resized)
icon_label2 = Label(sidebar, image=icon_photo2_resized, bg="#F5F5F5")
icon_label2.place(x=50, y=520)

manage_Btn = Button(sidebar, text="Manage", font=("sans-serif", 15, "bold"), bg="whitesmoke", fg="black", activebackground="whitesmoke", bd=0, relief="flat", width=10, command=show_manage)
manage_Btn.place(x=120, y=527)

icon_path3 = "IMAGES/EXIT.png"  # Update the path to your second icon image
icon_image3 = Image.open(icon_path3)
icon_image3_resized = icon_image3.resize((50, 50), Image.LANCZOS)
icon_photo3_resized = ImageTk.PhotoImage(icon_image3_resized)
icon_label3 = Label(sidebar, image=icon_photo3_resized, bg="#F5F5F5")
icon_label3.place(x=50, y=610)

def back_login():
    admin.destroy()
    import main
    
exit_Btn = Button(sidebar, text="Exit", font=("sans-serif", 15, "bold"), bg="whitesmoke", fg="black", activebackground="whitesmoke", bd=0, relief="flat", width=10, command=back_login)
exit_Btn.place(x=120, y=615)

up_frame = Frame(admin, width=950, height=80, bg="#3498DB")
up_frame.place(x=350, y=0)

def update_total_data():
    filename = 'order_details.json'
    total_orders_count = 0
    total_delivered_count = 0
    total_revenue_amount = 0.0

    shoes_count = 0
    clothes_count = 0

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
        
        total_orders_count = len(orders["order_details"])
        total_revenue_amount = sum(float(item["Total Cost"]) for item in orders["order_details"])
        
        # Calculate total orders for each product category
        for order in orders["order_details"]:
            for item in order["Items"]:
                if item["name"].lower() == "shoes":
                    shoes_count += 1
                elif item["name"].lower() == "clothes":
                    clothes_count += 1

        # Calculate total delivered orders
        for item in orders["order_details"]:
            if isinstance(item["Status"], str) and item["Status"].lower() == "delivered":
                total_delivered_count += 1

        # Update the labels and graph
        orders_total.config(text=str(total_orders_count))
        delivery.config(text=str(total_delivered_count))
        revenue.config(text=f"₱{total_revenue_amount:.2f}")

        # Generate and display the bar graph
        generate_bar_graph()
    else:
        orders_total.config(text="0")
        delivery.config(text="0")
        revenue.config(text="₱0.00")


# Function to add a new order
def add_order(order_data):
    filename = 'order_details.json'
    orders = {"order_details": []}
    
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
    
    orders["order_details"].append(order_data)
    
    with open(filename, 'w') as outfile:
        json.dump(orders, outfile, indent=4)
    
    # Update total orders and revenue after adding order
    update_total_data()

# Function to delete an order
def delete_order(order_id):
    filename = 'order_details.json'
    orders = {"order_details": []}
    
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
    
    if order_id < len(orders["order_details"]):
        del orders["order_details"][order_id]
    
        with open(filename, 'w') as outfile:
            json.dump(orders, outfile, indent=4)
    
    # Update total orders and revenue after deleting order
    update_total_data()

# Function to update an order
def update_order(order_id, updated_data):
    filename = 'order_details.json'
    orders = {"order_details": []}
    
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
    
    if order_id < len(orders["order_details"]):
        orders["order_details"][order_id] = updated_data
    
        with open(filename, 'w') as outfile:
            json.dump(orders, outfile, indent=4)
    
    # Update total orders and revenue after updating order
    update_total_data()

#========== DASHBOARD FRAME ==========
dash_frame = Frame(admin, width=950, height=770, bg="white")
dash_frame.place(x=350, y=80)
down_frame = Frame(dash_frame, width=950, height=80, bg="#3498DB")
down_frame.place(x=0, y=690)

dashboard_Label = Label(dash_frame, text="Dashboard", font=("sans-serif", 25, "bold"), bg="white")
dashboard_Label.place(x=50, y=30)

total_orders = Frame(dash_frame, width=220, height=170, bg="#3498DB", highlightthickness=3, highlightbackground="black")
total_orders.place(x=80, y=120)

label_orders = Label(total_orders, text="Total Orders", font=("sans-serif", 14, "bold"), bg="#3498DB", fg="black")
label_orders.place(x=70, y=28)

orders_total = Label(total_orders, text="", font=("sans-serif", 20, "bold"), bg="#3498DB", fg="white")
orders_total.place(x=100, y=80)

icon_path_orders = "IMAGES/ORDER.png" 
icon_image_orders = Image.open(icon_path_orders)
icon_image_orders_resized = icon_image_orders.resize((40, 40), Image.LANCZOS)
icon_photo_orders_resized = ImageTk.PhotoImage(icon_image_orders_resized)
icon_label_orders = Label(total_orders, image=icon_photo_orders_resized, bg="#3498DB")
icon_label_orders.place(x=20, y=20)

total_deliver = Frame(dash_frame, width=220, height=170, bg="#3498DB", highlightthickness=3, highlightbackground="black")
total_deliver.place(x=360, y=120)

label_deliver = Label(total_deliver, text="Delivered", font=("sans-serif", 14, "bold"), bg="#3498DB", fg="black")
label_deliver.place(x=70, y=28)

delivery = Label(total_deliver, text="", font=("sans-serif", 20, "bold"), bg="#3498DB", fg="white")
delivery.place(x=100, y=80)

icon_path_deliver = "IMAGES/SHIP.png"  
icon_image_deliver = Image.open(icon_path_deliver)
icon_image_deliver_resized = icon_image_deliver.resize((40, 40), Image.LANCZOS)
icon_photo_deliver_resized = ImageTk.PhotoImage(icon_image_deliver_resized)
icon_label_deliver = Label(total_deliver, image=icon_photo_deliver_resized, bg="#3498DB")
icon_label_deliver.place(x=20, y=20)

total_revenue = Frame(dash_frame, width=220, height=170, bg="#3498DB", highlightthickness=3, highlightbackground="black")
total_revenue.place(x=650, y=120)

label_revenue = Label(total_revenue, text="Revenue", font=("sans-serif", 14, "bold"), bg="#3498DB", fg="black")
label_revenue.place(x=70, y=28)

revenue = Label(total_revenue, text="", font=("sans-serif", 17, "bold"), bg="#3498DB", fg="white")
revenue.place(x=50, y=80)

icon_path_revenue = "IMAGES/REVENUE.png" 
icon_image_revenue = Image.open(icon_path_revenue)
icon_image_revenue_resized = icon_image_revenue.resize((40, 40), Image.LANCZOS)
icon_photo_revenue_resized = ImageTk.PhotoImage(icon_image_revenue_resized)
icon_label_revenue = Label(total_revenue, image=icon_photo_revenue_resized, bg="#3498DB")
icon_label_revenue.place(x=20, y=20)


#========== MANAGE FRAME ===============
manage_frame = Frame(admin, width=950, height=770, bg="white")  
manage_frame.place(x=350, y=80)

edit_frame = Frame(admin, width=950, height=770, bg="white")  
edit_frame.place(x=350, y=80)

order_frame = Frame(manage_frame, width=900, height=630, bg="#3498DB")
order_frame.place(x=25, y=25)

style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 12), rowheight=30)
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
style.configure("Treeview", 
                background="#FBFCFC", 
                foreground="black", 
                rowheight=25, 
                fieldbackground="#3498DB")

style.map("Treeview", 
          background=[('selected', "#EBF5FB")], 
          foreground=[('selected', "black")])

tree_frame = Frame(order_frame)
tree_frame.place(x=20, y=80, width=855, height=530)

tree = ttk.Treeview(tree_frame, columns=("Order Number", "Full Name", "Contact Number", "Email", "Address", "Region", "Province", "Municipality", "Barangay", "Payment", "Items", "Total Cost", "Status"),
                    show="headings", height=30)

# Center the text in each column
for col in tree["columns"]:
    tree.column(col, anchor="center")

# Center the text in the headings
for col in tree["columns"]:
    tree.heading(col, text=col, anchor="center")

tree_yscroll = Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree_xscroll = Scrollbar(tree_frame, orient="horizontal", command=tree.xview)

tree.place(x=1, y=1, width=837, height=513)
tree_yscroll.place(x=837, y=1, height=513)
tree_xscroll.place(x=1, y=513, width=837)

tree.configure(yscrollcommand=tree_yscroll.set, xscrollcommand=tree_xscroll.set)
tree_yscroll.configure(command=tree.yview)
tree_xscroll.configure(command=tree.xview)

tree.column("Order Number", stretch=False, width=100)
tree.column("Full Name", stretch=False, width=230)
tree.column("Contact Number", stretch=False, width=150)
tree.column("Email", stretch=False, width=200)
tree.column("Address", stretch=False, width=200)
tree.column("Region", stretch=False, width=150)
tree.column("Province", stretch=False, width=150)
tree.column("Municipality", stretch=False, width=150)
tree.column("Barangay", stretch=False, width=200)
tree.column("Payment", stretch=False, width=150)
tree.column("Items", stretch=False, width=100)
tree.column("Total Cost", stretch=False, width=100)
tree.column("Status", stretch=False, width=100)


tree.heading("Order Number", text="Order #")
tree.heading("Full Name", text="Name" )
tree.heading("Contact Number", text="Phone" )
tree.heading("Email", text="Email" )
tree.heading("Address", text="Address" )
tree.heading("Region", text="Region" )
tree.heading("Province", text="Province" )
tree.heading("Municipality", text="Municipal" )
tree.heading("Barangay", text="Barangay" )
tree.heading("Payment", text="Payment" )
tree.heading("Items", text="Item" )
tree.heading("Total Cost", text="Total Cost" )
tree.heading("Status", text="Status")

search_Ent = Entry(manage_frame, relief="ridge")
search_Ent.place(x=50, y=50, width=600, height=30)

def search_treeview():
    search_term = search_Ent.get().lower()
    for item in tree.get_children():
        tree.delete(item)

    filename = 'order_details.json'
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
            for order in orders["order_details"]:
                items_str = ', '.join([f"{item['name']} {item['size']} - ₱{item['price']:.2f}" for item in order["Items"]])
                if (search_term in str(order["Order Number"]).lower() or
                    search_term in order["Full Name"].lower() or
                    search_term in order["Contact Number"].lower() or
                    search_term in order["Email"].lower() or
                    search_term in order["Address"].lower() or
                    search_term in order["Region"].lower() or
                    search_term in order["Province"].lower() or
                    search_term in order["Municipality"].lower() or
                    search_term in order["Barangay"].lower() or
                    search_term in order["Payment"].lower() or
                    search_term in items_str.lower() or
                    search_term in str(order["Total Cost"]).lower() or
                    search_term in order["Status"].lower()):
                        tree.insert('', 'end', values=(order["Order Number"], 
                                                        order["Full Name"], 
                                                        order["Contact Number"], 
                                                        order["Email"], 
                                                        order["Address"], 
                                                        order["Region"], 
                                                        order["Province"], 
                                                        order["Municipality"], 
                                                        order["Barangay"], 
                                                        order["Payment"], 
                                                        items_str, 
                                                        f"₱{order['Total Cost']:.2f}", order["Status"]))

search_Btn = Button(manage_frame, text="Search", font=("sans-serif", 13), activebackground="black", bd=0, bg="black", fg="white", relief="flat", command=search_treeview)
search_Btn.place(x=680, y=50, width=100)

# Function to refresh Treeview and update total orders and revenue
def refresh_data():
    filename = 'order_details.json'
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as readfile:
            orders = json.load(readfile)
            
        tree.delete(*tree.get_children())
        for item in orders["order_details"]:
            items_str = ', '.join([f"{item['name']} {item['size']} - ₱{item['price']:.2f}" for item in item["Items"]])
            tree.insert('', 'end', values=(item["Order Number"], 
                                                    item["Full Name"], 
                                                    item["Contact Number"], 
                                                    item["Email"], 
                                                    item["Address"], 
                                                    item["Region"], 
                                                    item["Province"], 
                                                    item["Municipality"], 
                                                    item["Barangay"], 
                                                    item["Payment"], 
                                                    items_str, 
                                                    f"₱{item['Total Cost']:.2f}", item["Status"]))

    else:
        messagebox.showwarning("No Data Found", "No data found to refresh.")

refresh_Btn = Button(manage_frame, text="Refresh", font=("sans-serif", 13), activebackground="black", bd=0, bg="black", fg="white", relief="flat", command=refresh_data)
refresh_Btn.place(x=800, y=50, width=100)


buttons_frame = Frame(manage_frame, width=900, height=70, bg="#3498DB")
buttons_frame.place(x=25, y=680)

# Function to edit the status of an order
def edit_order():
    # Get the selected item from the Treeview
    selected_item = tree.focus()
    if selected_item:
        item_details = tree.item(selected_item)['values']
        
        edit_window = Toplevel(admin)
        edit_window.title("Edit Status")
        edit_window.geometry("400x200")
        edit_window.resizable(False, False)
        edit_window.config(bg="#3498DB")
        
        Label(edit_window, text="New Status", font=("sans-serif", 11, "bold"), bg="#3498DB").place(x=150, y=30)
        new_status_entry = Entry(edit_window, relief="flat", width=35)
        new_status_entry.place(x=90, y=60)
        
        def save_changes():
            new_status = new_status_entry.get()
            
            # Update the status in the Treeview
            tree.item(selected_item, values=(
                item_details[0],  # Order Number
                item_details[1],  # Full Name
                item_details[2],  # Contact Number
                item_details[3],  # Email
                item_details[4],  # Address
                item_details[5],  # Region
                item_details[6],  # Province
                item_details[7],  # Municipality
                item_details[8],  # Barangay
                item_details[9],  # Payment
                item_details[10],  # Items
                item_details[11],  # Total Cost
                new_status  # Updated Status
            ))
            
            # Update the JSON file with the new status
            filename = 'order_details.json'
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, 'r') as readfile:
                    orders = json.load(readfile)
                
                for order in orders["order_details"]:
                    if order["Order Number"] == item_details[0]:
                        order["Status"] = new_status
                        break
            
                with open(filename, 'w') as outfile:
                    json.dump(orders, outfile, indent=4)
            
            # Refresh the dashboard data
            update_total_data()

            edit_window.destroy()
        
        update_btn = Button(edit_window, 
                            text="Update", 
                            relief="flat",
                            bg="black",
                            fg="white",
                            activebackground="#3498DB",
                            bd=0,
                            width=10,
                            font=("sans-serif", 11),
                            command=save_changes)
        update_btn.place(x=140, y=110)

editBtn = Button(buttons_frame, text="Edit", font=("sans-serif", 13), activebackground="black", bd=0 , bg="black", fg="white", relief="flat", command=edit_order)
editBtn.place(x=80, y=20, width=120)


# Function to delete an order from JSON and Treeview
def delete_order():
    # Get the selected item from the Treeview
    selected_item = tree.focus()
    if selected_item:
        item_details = tree.item(selected_item)['values']
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete order #{item_details[0]}?")
        
        if confirm:
            filename = 'order_details.json'
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, 'r') as readfile:
                    orders = json.load(readfile)
                
                # Find and remove the order from JSON data
                updated_orders = {"order_details": []}
                for order in orders["order_details"]:
                    if order["Order Number"] != item_details[0]:
                        updated_orders["order_details"].append(order)
                
                with open(filename, 'w') as outfile:
                    json.dump(updated_orders, outfile, indent=4)
                
                tree.delete(selected_item)
                update_total_data()
                
                messagebox.showinfo("Order Deleted", f"Order #{item_details[0]} has been deleted.")
            else:
                messagebox.showwarning("No Data Found", "No data found to delete.")

deleteBtn = Button(buttons_frame, text="Delete", font=("sans-serif", 13), activebackground="black", bd=0, bg="black", fg="white", relief="flat",command=delete_order)
deleteBtn.place(x=280, y=20, width=120)
           

# Function to print a receipt as PDF
def print_receipt():
    # Get the selected item from the Treeview
    selected_item = tree.focus()
    if selected_item:
        item_details = tree.item(selected_item)['values']
        
        # Create a receipt format
        receipt = f"Receipt for Order #{item_details[0]}\n"
        receipt += f"Name: {item_details[1]}\n"
        receipt += f"Contact Number: {item_details[2]}\n"
        receipt += f"Email: {item_details[3]}\n"
        receipt += f"Address: {item_details[4]}\n"
        receipt += f"Region: {item_details[5]}\n"
        receipt += f"Province: {item_details[6]}\n"
        receipt += f"Municipality: {item_details[7]}\n"
        receipt += f"Barangay: {item_details[8]}\n"
        receipt += f"Payment: {item_details[9]}\n"
        receipt += f"Items:\n"
        items_str = item_details[10].split(', ')
        for item in items_str:
            receipt += f"  - {item}\n"
        receipt += f"Total Cost: {item_details[11]}\n"
        
        # Prompt the user to choose a file name and location
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        
        if file_path:
            # Create a PDF file
            pdf = fpdf.FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Add content line by line
            for line in receipt.split('\n'):
                # Ensure proper encoding here
                pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1', 'replace'), ln=True, align="L")
                
            # Save the PDF
            pdf.output(file_path)
            
            messagebox.showinfo("Receipt Saved", f"Receipt for order #{item_details[0]} has been saved as PDF.")

receipt_Btn = Button(buttons_frame, text="Receipt", font=("sans-serif", 13), activebackground="black", bd=0, bg="black", fg="white", relief="flat", command=print_receipt)
receipt_Btn.place(x=480, y=20, width=120)

def export_to_pdf():
    filename = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")])
    if filename:
        try:
            root = tk.Tk()
            root.withdraw()

            # Create PDF in custom size and landscape orientation
            c = canvas.Canvas(filename, pagesize=landscape(TABLOID))
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, 700, "Order Details")

            # Adjust treeview dimensions
            tree = ttk.Treeview(root)
            tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
            tree.column("#0", width=10, minwidth=10, stretch=tk.NO)
            for col in tree["columns"]:
                tree.column(col, width=10, minwidth=10, stretch=tk.NO)
            tree.heading("#0", text="ID", anchor=tk.W)
            for col in tree["columns"]:
                tree.heading(col, text=col, anchor=tk.W)

            y_position = 280
            for child in tree.get_children():
                item = tree.item(child)['values']
                y_position -= 20
                c.drawString(10, y_position, f"Order Number: {item[0]}")
                y_position -= 20
                c.drawString(10, y_position, f"Full Name: {item[1]}")
                y_position -= 20
                c.drawString(10, y_position, f"Contact Number: {item[2]}")
                y_position -= 20
                c.drawString(10, y_position, f"Email: {item[3]}")
                y_position -= 20
                c.drawString(10, y_position, f"Address: {item[4]}")
                y_position -= 20
                c.drawString(10, y_position, f"Region: {item[5]}")
                y_position -= 20
                c.drawString(10, y_position, f"Province: {item[6]}")
                y_position -= 20
                c.drawString(10, y_position, f"Municipality: {item[7]}")
                y_position -= 20
                c.drawString(10, y_position, f"Barangay: {item[8]}")
                y_position -= 20
                c.drawString(10, y_position, f"Payment: {item[9]}")
                y_position -= 20
                c.drawString(10, y_position, f"Items: {item[10]}")
                y_position -= 20
                c.drawString(10, y_position, f"Total Cost: {item[11]}")

               
                

            c.showPage()
            c.save()

            messagebox.showinfo("Exported to PDF", f"Data exported to {filename}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")




def export_to_pdf():
    filename = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")])
    if filename:
        try:
            c = canvas.Canvas(filename, pagesize=landscape(TABLOID))
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 500, "Order Details")

            # Define table headers
            table_headers = ["Order Number", "Full Name", "Contact Number", "Email", "Address", "Region", "Province",
                             "Municipality", "Barangay", "Payment", "Items", "Total Cost", "Status"]

            # Define table data
            table_data = []
            for child in tree.get_children():
                item = tree.item(child)['values']
                table_data.append(item)

            # Create table style
            table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                     ('BOX', (0, 0), (-1, -1), 0.5, colors.black)])

            # Create table object
            order_table = Table([table_headers] + table_data)
            order_table.setStyle(table_style)

            # Add table to the PDF
            order_table.wrapOn(c, 200, 200)
            order_table.drawOn(c, 20, 350)

            c.showPage()
            c.save()

            messagebox.showinfo("PDF Export", "PDF file has been successfully generated.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


printBtn = Button(buttons_frame, text="Print", font=("sans-serif", 13), activebackground="black", bd=0, bg="black", fg="white", relief="flat", command=lambda:export_to_pdf())
printBtn.place(x=680, y=20, width=120)


update_total_data() 

generate_bar_graph()
generate_pie_chart() 

dash_frame.tkraise()

admin.mainloop()
