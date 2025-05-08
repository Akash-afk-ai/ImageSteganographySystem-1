from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3
import bcrypt

class LoginInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        # Initialize database connection
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        
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
        
        # Add error text
        self.error_text = self.canvas.create_text(
            320.0,
            380.0,
            anchor="nw",
            fill="#FF0000",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add login button
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.authenticate,
            relief="flat"
        )
        self.button_1.place(
            x=300.0,
            y=328.0,
            width=256.0,
            height=34.0
        )
        
        # Add register button
        self.button_image = PhotoImage(
            file=self.relative_to_assets("Button.png"))
        self.button = Button(
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_register_interface,
            relief="flat"
        )
        self.button.place(
            x=745.0,
            y=30.0,
            width=91.0,
            height=34.0
        )
        
        # Add username entry
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            428.5,
            232.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=311.0,
            y=214.0,
            width=235.0,
            height=34.0
        )
        
        self.canvas.create_text(
            407.0,
            190.0,
            anchor="nw",
            text="Login:",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add password entry
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            428.5,
            294.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            highlightthickness=0,
            show="*"
        )
        self.entry_2.place(
            x=311.0,
            y=276.0,
            width=235.0,
            height=34.0
        )
        
        self.canvas.create_text(
            397.0,
            255.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add welcome text
        self.canvas.create_text(
            250.0,
            164.0,
            anchor="nw",
            text="Welcome to StegaX, login to your account in order to access",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            364.0,
            101.0,
            anchor="nw",
            text="Sign in",
            fill="#FFFFFF",
            font=("Poppins Regular", 40 * -1)
        )
    
    def authenticate(self):
        """Handle user authentication"""
        username = self.entry_1.get()
        password = self.entry_2.get()
        
        self.canvas.itemconfig(self.error_text, text="")  # Clear previous error messages
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        
        # Query the database to check if the credentials are correct
        self.cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()
        
        if result:
            hashed_password = result[0]
            # Check if the entered password matches the stored hashed password
            if bcrypt.checkpw(password.encode(), hashed_password):
                # Authentication successful, open the home page
                self.open_home_interface()
            else:
                # Authentication failed, show an error message
                self.canvas.itemconfig(self.error_text, text="Incorrect username or password")
        else:
            # Authentication failed, show an error message
            self.canvas.itemconfig(self.error_text, text="Incorrect username or password")
    
    def open_home_interface(self):
        """Open the home interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui3.py"])
        self.window.destroy()
    
    def open_register_interface(self):
        """Open the register interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui2.py"])
        self.window.destroy()
    
    def relative_to_assets(self, path: str) -> Path:
        """Get the path to an asset file"""
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
        return ASSETS_PATH / Path(path)
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

def show_login_interface():
    """Show the login interface"""
    app = LoginInterface()
    app.run()

if __name__ == "__main__":
    show_login_interface()
