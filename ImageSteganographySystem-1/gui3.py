from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

class HomeInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create canvas
        self.canvas = Canvas(
            self.window,
            bg="#093545",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
        # Place canvas
        self.canvas.place(x=0, y=0)
        
        # Add background image
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            438.0,
            474.0,
            image=self.image_image_1
        )
        
        # Add welcome text
        self.canvas.create_text(
            310.0,
            28.0,
            anchor="nw",
            text="Welcome to StegaX!",
            fill="#FFFFFF",
            font=("LexendDeca Regular", 24 * -1)
        )
        
        # Add encode button
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_encoding_interface,
            relief="flat"
        )
        self.button_1.place(
            x=336.0,
            y=201.0,
            width=191.0,
            height=69.0
        )
        
        # Add decode button
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_decoding_interface,
            relief="flat"
        )
        self.button_2.place(
            x=336.0,
            y=287.0,
            width=191.0,
            height=69.0
        )
        
        # Add logout button
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_login_interface,
            relief="flat"
        )
        self.button_3.place(
            x=739.0,
            y=30.0,
            width=91.0,
            height=34.0
        )
        
        # Add detection button
        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_detection_interface,
            relief="flat"
        )
        self.button_4.place(
            x=336.0,
            y=373.0,
            width=191.0,
            height=69.0
        )
        
        # Add description text
        self.canvas.create_text(
            256.0,
            64.0,
            anchor="nw",
            text="StegaX is An Image Steganography System that enables you",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            292.0,
            82.0,
            anchor="nw",
            text="to hide secret messages within digital images.",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            298.0,
            158.0,
            anchor="nw",
            text="  Please choose one of the following features",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            298.0,
            340.0,
            anchor="nw",
            text="  Or analyze images for hidden content",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
    
    def open_login_interface(self):
        """Open the login interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui.py"])
        self.window.destroy()
    
    def open_encoding_interface(self):
        """Open the encoding interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui4.py"])
        self.window.destroy()
    
    def open_decoding_interface(self):
        """Open the decoding interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui5.py"])
        self.window.destroy()
    
    def open_detection_interface(self):
        """Open the detection interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui7.py"])
        self.window.destroy()
    
    def relative_to_assets(self, path: str) -> Path:
        """Get the path to an asset file"""
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets" / "frame3"
        return ASSETS_PATH / Path(path)
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

def show_home_interface():
    """Show the home interface"""
    app = HomeInterface()
    app.run()

if __name__ == "__main__":
    show_home_interface()
