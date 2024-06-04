
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Style, Treeview
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def viewCleaners():
    ViewCleaners()

class ViewCleaners(Frame):
     def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 420,
            width = 706,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            40.0,
            81.0,
            668.0,
            326.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            175.0,
            57.0,
            image= self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            154.5,
            57.5,
            image=self.entry_image_1
        )
        self.search_var = StringVar()
        entry_1 = Entry(
            self,
            textvariable=self.search_var,
            bd=0,
            bg="#3B6EF2",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=50.0,
            y=43.0,
            width=209.0,
            height=27.0
        )

        canvas.create_rectangle(
            264.0,
            43.0,
            265.0,
            72.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.search_btn = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_records,
            relief="flat"
        )
        self.search_btn.place(
            x=273.0,
            y=44.0,
            width=28.0,
            height=27.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_delete,
            relief="flat"
        )
        button_2.place(
            x=581.0,
            y=348.0,
            width=87.0,
            height=39.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_edit,
            relief="flat"
        )
        button_3.place(
            x=479.0,
            y=348.0,
            width=87.0,
            height=39.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("add"),
            relief="flat"
        )
        button_4.place(
            x=377.0,
            y=348.0,
            width=87.0,
            height=39.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.refresh_btn = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_refresh,
            relief="flat"
        )
        self.refresh_btn.place(
            x=40.0,
            y=348.0,
            width=36.0,
            height=36.0
        )

        self.columns = {
            "cleaner_id": ["Cleaners ID", 10],
             "group_leader": ["Group Leader", 40],
             "members": ["Members", 100],
             "schedule_day": ["Schedule", 40],
            "cleaning": ["Cleaning Materials", 30] 
        }
        
                # Create a style
        self.style = Style(self)
        self.style.configure("Custom.Treeview", background="#FFFFFF")
        self.style.map("Custom.Treeview",
                       background=[("selected", "#0E46A3")])

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            style="Custom.Treeview"
            # bg="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=40.0, y=81.0, width=630.0, height=250.0) #264.0,
          
           
        #self.treeview.place(x=40.0, y=101.0, width=700.0, height=229.0)

        # Insert data
        self.handle_refresh()   
# Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

     def filter_treeview_records(self, query):
        self.treeview.delete(*self.treeview.get_children())
        # Run for loop from original data
        for row in self.room_data:
            # Check if query exists in any value from data
            if query.lower() in str(row).lower():
                # Insert the data into the treeview
                self.treeview.insert("", "end", values=row)
        self.on_treeview_select()

     def on_treeview_select(self, event=None):
        try:
            self.treeview.selection()[0]
        except IndexError:
            self.parent.selected_rid = None
            return
        # Get the selected item
        item = self.treeview.selection()[0]
        # Get the room id
        self.parent.selected_rid = self.treeview.item(item, "values")[0]
        # Enable the buttons
        self.delete_btn.config(state="normal")
        self.edit_btn.config(state="normal")

     def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.room_data = db_controller.get_cleaners()
        print("self room data: ", self.room_data)
        for row in self.room_data:
            self.treeview.insert("", "end", values=row)

     #def handle_navigate_back(self):
        #self.parent.navigate("add")

     def handle_delete(self):
        if db_controller.delete_cleaners(self.parent.selected_rid): 
            messagebox.showinfo("Success","Successfully Deleted the room")
        else:
            messagebox.showerror("failed","Unable to delete room")

        self.handle_refresh()

     def handle_edit(self):
        self.parent.navigate("update")
        self.parent.windows["update"].initialize()
        self.handle_refresh()

     def search_records(self):
        # Get the search query
        query = self.search_var.get().strip()
        
        # Perform search
        if query:
            search_results = db_controller.search_cleaners(query)
            # Update the Treeview with search results
            self.update_treeview(search_results)
        else:
            # If query is empty, show all records
            self.handle_refresh()

     def update_treeview(self, records):
        # Clear existing data in Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Insert search results into Treeview
        for row in records:
            self.treeview.insert("", "end", values=row)



        