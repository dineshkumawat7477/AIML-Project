import tkinter as tk
from tkinter.ttk import *
from backend import insert_data, get_data
from GET_path import path
font_data = "Arial 15" # For normal use

class APP(tk.Tk):
    # Window Initiator
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        icon_img = tk.PhotoImage(file = path()+"1.png")
        self.iconphoto(True, icon_img)
        self.geometry("1030x500")
        # Menu
        self.create_menu()
        # Frame for all elements in body
        self.body_frame = Frame()
        self.body_frame.pack(fill = "both")
        # Body
        self.Body(self.body_frame)

    # Menu
    def create_menu(self):
        # Creates main menubar variable using tk.menu
        menubar = tk.Menu(self, tearoff = 0)
        # Sets menubar in window
        self.config(menu=menubar)
        # Adds Option Settings in menu
        menubar.add_command(label="Settings", command=lambda: self.settings(frame = self.body_frame))
        menubar.add_command(label="Home", command=lambda: self.Home(frame = self.body_frame))
        menubar.add_command(label="View", command=lambda: self.View(frame = self.body_frame))
        
        '''# Creates an option
        file_menu = tk.Menu(menubar, tearoff=0)
        # Create submenu for this option
        file_menu.add_command(label="New", command=lambda: print("New file!"))
        file_menu.add_command(label="Exit", command=self.destroy)
        # Adds an option in the mneubar
        menubar.add_cascade(label="File", menu=file_menu)'''

    # Body of Window
    def Body(self, frame):
        self.Home(frame) # Defaukt Page set to Home
        
    # Home
    def Home(self, frame):
        self.clear_body(frame)
        self.create_category(frame)
        self.detail_box(frame)
        self.Price_box(frame)
        # Add/Submit Button
        font_style = Style().configure('button.TButton', font = font_data) # font for ttk button
        Button(frame, text = "Add", style = "button.TButton", command = self.Add).pack()

    # View Page
    def View(self, frame):
        self.clear_body(frame)
        self.content(frame)

    # Clearing Body
    def clear_body(self, frame):
        for elements in frame.winfo_children():
            elements.destroy()

    # Settings
    def settings(self, frame):
        self.clear_body(frame)

    # Creating catergory dropdown widget
    def create_category(self, frame):
        self.option_list = ["Food", "Laundary", "Person", "Other", "Credit"]
        self.selected_option = tk.StringVar(frame) # Show selected option and data store variable
        self.selected_option.set("Select an option") # Default value
        dropdown = Combobox(frame, 
                            textvariable=self.selected_option, # Stores selected option
                            values = self.option_list,
                            state = "readonly", # Prevent custom input
                            height = 10, # Set number of items in the dropdown list to be displayed. eg. for height = 1 with 3 items fit so normal but with more items say 8 or 9 then 3 items are displayed with scroll for otheritems
                            width = 18, # Set Chracter length to be displayed
                            font = font_data # Also determine character height
                            )
        dropdown.pack(padx = 30, pady = 40, anchor = "nw")

    # Detail Box
    def detail_box(self, frame):
        self.input_text = tk.StringVar(frame, value = "Add Detail")
        self.input_box = Entry(frame, textvariable = self.input_text, width = 20, font = font_data)
        self.input_box.pack(padx = 30, anchor = "nw")
    # Price Box
    def Price_box(self, frame):
        self.price_label = Label(frame, text = "Enter Amount(in Rs.) : ", font = font_data) # Text
        self.price_label.pack(side = "left", padx = 30, pady = 40, anchor = "nw")
        self.price_text = tk.StringVar(frame, value = "Enter Amount") #Data store var
        self.price_box = Entry(frame, textvariable = self.price_text, width = 20, font = font_data) #Intake Box
        self.price_box.pack(side = "left", pady = 40, anchor = "nw")
    
    def Add(self): # Calling Backend Process To store data
        insert = insert_data(self.selected_option.get(), self.input_box.get(), self.price_box.get())
        if insert == "Price Error":
            return insert
        
    def print_data(self, box, raw_data): 
        '''Data shown normally from list is printed in a list of curly brackets to make it look pretty it preine line by line'''
        
        months = ["January","February","March","April","May","June","July","August","September","October","November", "December"]
        for line in raw_data:
            for month in months:
                if month+":" in line:
                    box.insert(tk.END, "\n"+line+"\n")
                    break
                elif month == "December":
                    box.insert(tk.END, line+"\n")

    def content(self, frame): # Calling Backend Process To read Data
        yscroll_bar = Scrollbar(frame) # Y-axis Scroll Bar
        yscroll_bar.pack(side ="right", fill = "y")
        
        xscroll_bar = Scrollbar(frame, orient = tk.HORIZONTAL) # X-axis Scroll Bar
        xscroll_bar.pack(side ="bottom", fill = "x")
        
        # self.content_box = tk.Text(frame, wrap = "word", font = font_data) # Content Area
        self.content_box = tk.Text(frame, wrap = "none", font = font_data) # Content Area
        self.content_box.pack()
        # self.content_box.insert(tk.END, get_data())
        self.print_data(raw_data = get_data(), box = self.content_box)
        
        yscroll_bar.config(command = self.content_box.yview)
        xscroll_bar.config(command = self.content_box.xview)
        
        self.content_box.config(yscrollcommand = yscroll_bar.set, xscrollcommand=xscroll_bar.set)

        
if __name__ == "__main__":
    app = APP()
    app.mainloop()
    