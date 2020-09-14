# Name: University Admission - Tracking Table
# Description: Allows the editing and modifying of the status of university admissions
# Auhthor: Vo Trung Son
# Date: 13/02/19

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator
import webbrowser

# Basics - creating the main tkinter window
root = Tk()
root.title('University Admissions Table')
root.geometry("800x600")

# Create a frame inside of the window for the output table
frame = Frame(root, borderwidth=1, relief="solid")          # Borderwidth and relief gives the frame a solid border
frame.grid(row=10, column=0, columnspan=10, sticky="NSEW", pady=5, padx=10)

#Creating an Introduction label
intro = Label(root, text="University Admissions Table", font=(None, 15, "bold underline"))
intro.grid(row=0, column=0, sticky="W", padx=10, pady=10)

#Creating the lists to store the entries
list_name = []
list_status = []
list_date = []
list_website = []

def entry_root():
    """Function to create a second window for entering entries"""
    global website_entry

    # Creating a second window
    entry_root = Tk()
    entry_root.title('Entries')
    entry_root.geometry("300x300")

    def add():
        """Function to add new entries into the list"""
        list_name.append(name_entry.get())  # Add new entries into the list
        list_status.append(status_value.get())
        list_date.append(date_entry.get())
        list_website.append(website_entry.get())

    def remove():
        """Function to remove an entry when the name is typed"""
        for remove_name, remove_status, remove_date, remove_website in zip(list_name, list_status, list_date, list_website):      # Run through the lists
            if remove_name == name_entry.get():
                index = list_name.index(name_entry.get())       # Get the index of the specific name to be deleted in the list
                del list_name[index]                            # Deleting takes into account of index in list, not solely the variable
                del list_status[index]
                del list_date[index]
                del list_website[index]

    # Name section
    name_label = Label(entry_root, text="Name:")  # Create name label
    name_label.grid(row=0, column=0, pady=1, sticky="W")
    name_entry = ttk.Entry(entry_root)  # Create an entry box to enter the names
    name_entry.grid(row=1, column=0, sticky="W")  # Place that box into the window

    # Status section
    status_label = Label(entry_root, text="Status:")  # Create status label
    status_label.grid(row=2, column=0, pady=1, sticky="W")
    status_choices = ["Choose a status", "Incomplete", "Awaiting decision", "Accepted!", "Rejected"]  # Create a list of choices for drop down menu
    status_value = StringVar(entry_root)  # Create a value variable to store the choice that has been chosen
    status_value.set(status_choices[0])  # Set the default value for the drop down menu to the first position in the list

    status_dropdownlist = ttk.OptionMenu(entry_root, status_value, *status_choices)  # Create the drop down menu inside root, storing choice in value, using information in the choice list
    status_dropdownlist.grid(row=3, column=0, sticky="W")  # Output the drop down menu onto the window

    # Date section
    date_label = Label(entry_root, text="Deadline:")
    date_label.grid(row=4, column=0, pady=1, sticky="W")
    date_entry = ttk.Entry(entry_root)
    date_entry.grid(row=5, column=0, pady=1, sticky="W")

    # Website section
    website_label = Label(entry_root, text="Website:")
    website_label.grid(row=6, column=0, pady=1, sticky="W")
    website_entry = ttk.Entry(entry_root)
    website_entry.grid(row=7, column=0, pady=1, sticky="W")

    #Creating buttons inside the entry window
    add_button = ttk.Button(entry_root, text="Add", command=add, width=10)  # Create a button for the add function
    add_button.grid(row=8, column=0, sticky="w", pady=5)

    remove_button = ttk.Button(entry_root, text="Remove", command=remove, width=10)
    remove_button.grid(row=9, column=0, sticky="W", pady=5)

def save():
    """Function to save the tables into text files"""
    with open("saved_name.txt", "w+") as saved_name:
        for n in list_name:
            saved_name.write(n + "\n")

    with open("saved_status.txt", "w+") as saved_status:
        for s in list_status:
            saved_status.write(s + "\n")

    with open("saved_date.txt", "w+") as saved_date:
        for d in list_date:
            saved_date.write(d + "\n")

    with open("saved_website.txt", "w+") as saved_website:
        for w in list_website:
            saved_website.write(w + "\n")

def load():
    """Function to load a saved list"""
    with open("saved_name.txt", "r") as saved_name:
        for n in saved_name:
            list_name.append(n.rstrip("\n"))

    with open("saved_status.txt", "r") as saved_status:
        for s in saved_status:
            list_status.append(s.rstrip("\n"))

    with open("saved_date.txt", "r") as saved_date:
        for d in saved_date:
            list_date.append(d.rstrip("\n"))

    with open("saved_website.txt", "r") as saved_website:
        for w in saved_website:
            list_website.append(w.strip("\n"))

def update():
    """Function to clear the last frame and output an updated frame"""
    global item_website
    i = 0

    grid_slave = frame.grid_slaves()  # Creating a list of the labels inside thee frame
    for g in grid_slave:  # Run through the list, deleting all the labels inside the frame
        g.destroy()

    for item_name, item_status, item_date, item_website in zip(list_name, list_status, list_date, list_website):  # Run through the entries in the list

        Name = Label(frame, text="Name", font=(None, 13, "underline"))
        Name.grid(row=8, column=0, padx=5, pady=3)

        Status = Label(frame, text="Status", font=(None, 13, "underline"))
        Status.grid(row=8, column=2, padx=5, pady=3)

        Date = Label(frame, text="Deadline", font=(None, 13, "underline"))
        Date.grid(row=8, column=4, padx=5, pady=3)

        Website = Label(frame, text="Website", font=(None, 13, "underline"))
        Website.grid(row=8, column=6, padx=5, pady=3)

        sep_linelabel = Separator(frame, orient="horizontal")
        sep_linelabel.grid(row=9, column=0, sticky="we", columnspan=10)

        name_slot = StringVar()  # Create a slot and set it to the entries
        name_slot.set(item_name)
        name_details = Label(frame, textvariable=name_slot, font=(None, 13))  # Create a label to output the entries
        name_details.grid(row=10 + i, column=0, padx=5, pady=5)  # Place the label into the frame

        draw_hyphen = Label(frame, text="-")  # Create a hyphen between entries' lists
        draw_hyphen.grid(row=10 + i, column=1)

        status_slot = StringVar()
        status_slot.set(item_status)
        status_details = Label(frame, textvariable=status_slot, font=(None, 13))
        status_details.grid(row=10 + i, column=2, padx=5, pady=5)

        draw_hyphen = Label(frame, text="-")
        draw_hyphen.grid(row=10 + i, column=3)

        date_slot = StringVar()
        date_slot.set(item_date)
        date_details = Label(frame, textvariable=date_slot, font=(None, 13))
        date_details.grid(row=10 + i, column=4, padx=5, pady=5)

        draw_hyphen = Label(frame, text="-")
        draw_hyphen.grid(row=10 + i, column=5)

        website_slot = StringVar()
        website_slot.set(item_website)
        website_details = Label(frame, textvariable=website_slot, font=(None, 13))
        website_details.grid(row=10 + i, column=6, padx=5, pady=5)
        website_details.bind("<Button-1>", callback)       # Bind the label to the callback function

        sep_line = Separator(frame, orient="horizontal")
        sep_line.grid(row=11 + i, column=0, sticky="we", columnspan=10)

        i += 2  # This prints the next entry onto the next line

def callback(event):            # Can't open each website individually when pressed, so it opened all websites
    """Save and open a text file to access the admissions' websites"""
    # Creating a text file to save the admissions' websites
    with open("access_websites.txt", "w+") as access_website:  # Saving the admissions' websites
        access_website.write("Below are the links to the universities admissions' websites: " + "\n")
        for a in list_website:
            access_website.write("\n" + a + "\n")

    webbrowser.open_new(r"file://D:\Python Workspace\University Admission Tracking Table\dist\access_websites.txt") # Opening the admissions' text file


save_button = ttk.Button(root, text="Save", command=save, width=10)
save_button.grid(row=5, column=0, sticky="W", pady=5)

load_button = ttk.Button(root, text="Load", command=load, width=10)
load_button.grid(row=6, column=0, sticky="w", pady=5)

update_button = ttk.Button(root, text="Update", command=update, width=10)  # Create a button for the update function
update_button.grid(row=4, column=0, sticky="W", pady=5)

edit_button = ttk.Button(root, text="Edit", command=entry_root, width=10)
edit_button.grid(row=3, column=0, sticky="W", pady=5)


# Run the entire thing
root.mainloop()
