from pathlib import Path
from tkinter import Frame, Tk, Canvas, Button, PhotoImage
from controller import get_day_cleaners, get_group_leader
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dashboard():
    Dashboard()

class Dashboard(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=420,
            width=706,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            119.0,
            58.0,
            376.0,
            337.0,
            fill="#9AB3DA",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.refresh_btn = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_refresh,
            relief="flat"
        )
        self.refresh_btn.place(
            x=641.0,
            y=15.0,
            width=51.0,
            height=43.0
        )

        # Get the current day of the week
        self.current_day = datetime.now().strftime("%A")

        self.day_text = self.canvas.create_text(
            190.0,
            96.0,
            anchor="nw",
            text=self.current_day,
            fill="#000000",
            font=("InriaSerif Bold", 32 * -1)
        )

        self.canvas.create_text(
            123.0,
            316.0,
            anchor="nw",
            text="Group Leader:",
            fill="#000000",
            font=("InriaSerif Bold", 15 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            301.0,
            322.0,
            image=self.image_image_1
        )

        self.text_object_Daycleaners = self.canvas.create_text(
            223.0,
            160.0,
            anchor="nw",
            text=str(get_day_cleaners(self.current_day)),
            fill="#000000",
            font=("MontserratRoman SemiBold", 60 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            522.0,
            189.0,
            image=self.image_image_2
        )

        self.group_leader_text = self.canvas.create_text(
            223.0,
            317.0,
            anchor="nw",
            text="", 
            fill="#000000",
            font=("InriaSerif Bold", 15 * -1)
        )

        self.update_text_from_database()

    def update_text_from_database(self):
        try:
            # Update the count of day cleaners
            day_cleaners_count = get_day_cleaners(self.current_day)
            self.canvas.itemconfigure(self.text_object_Daycleaners, text=str(day_cleaners_count))

            # Update the group leader text
            group_leader = get_group_leader(self.current_day)
            group_leader_text = ", ".join(group_leader) if group_leader else "No group leader found"
            self.canvas.itemconfigure(self.group_leader_text, text=group_leader_text)

        except Exception as e:
            print(f"Error: {e}")

    def handle_refresh(self):
        try:
            # Update the current day text
            self.current_day = datetime.now().strftime("%A")
            self.canvas.itemconfigure(self.day_text, text=self.current_day)
            # Refresh the data from the database
            self.update_text_from_database()
        except Exception as e:
            print(f"Error: {e}")

    def update_schedule(self, new_schedule_day):
        # Update the current day to the new schedule day
        self.current_day = new_schedule_day
        # Refresh the text from the database
        self.update_text_from_database()
