from pathlib import Path
import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3
import bcrypt
import re

class RegisterInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        # Initialize database connection
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        
        # Create users table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )''')
        
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
        
        # Add error and success text
        self.error_text = self.canvas.create_text(
            272.0,
            400.0,
            anchor="nw",
            fill="#FF0000",
            font=("Poppins Regular", 12 * -1)
        )
        self.success_text = self.canvas.create_text(
            272.0,
            400.0,
            anchor="nw",
            fill="#00FF00",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add register button
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.register,
            relief="flat"
        )
        self.button_1.place(
            x=303.0,
            y=328.0,
            width=256.0,
            height=34.0
        )
        
        # Add username entry
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            431.5,
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
            x=314.0,
            y=214.0,
            width=235.0,
            height=34.0
        )
        
        self.canvas.create_text(
            398.0,
            190.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add password entry
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            431.5,
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
            x=314.0,
            y=276.0,
            width=235.0,
            height=34.0
        )
        
        self.canvas.create_text(
            400.0,
            255.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        # Add welcome text
        self.canvas.create_text(
            272.0,
            136.0,
            anchor="nw",
            text="Welcome to StegaX, Register now and start your trial!",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            312.0,
            153.0,
            anchor="nw",
            text="or login if you already have an account!",
            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )
        
        self.canvas.create_text(
            302.0,
            72.0,
            anchor="nw",
            text="Register Now",
            fill="#FFFFFF",
            font=("Poppins Regular", 40 * -1)
        )
        
        # Add login button
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_login_interface,
            relief="flat"
        )
        self.button_2.place(
            x=745.0,
            y=30.0,
            width=91.0,
            height=34.0
        )
    
    def register(self):
        """Handle user registration"""
        username = self.entry_1.get()
        password = self.entry_2.get()
        
        self.canvas.itemconfig(self.error_text, text="")  # Clear previous error messages
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        
        # Encrypt the password
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        # Check if the username already exists
        self.cursor.execute("SELECT COUNT(*) FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()
        if result[0] > 0:
            self.canvas.itemconfig(self.error_text, text="Username already exists. Please choose a different username.")
            return
        
        # Check the length of the password
        if len(password) <= 8:
            self.canvas.itemconfig(self.error_text, text="Password should be more than 8 characters long.")
            return
        
        # Check if the password meets the requirements
        if not re.match(r"^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()_+=\-[\]{};':\"\\|,.<>/?])", password):
            self.canvas.itemconfig(self.error_text, text="Password should contain at least one letter, one digit, and one special symbol.")
            return
        
        # Insert the new user into the database
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.connection.commit()
        self.canvas.itemconfig(self.success_text, text="Registration successful.")
        
        self.open_login_interface()
    
    def open_login_interface(self):
        """Open the login interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui.py"])
        self.window.destroy()
    
    def relative_to_assets(self, path: str) -> Path:
        """Get the path to an asset file"""
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"
        return ASSETS_PATH / Path(path)
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

def show_register_interface():
    """Show the register interface"""
    app = RegisterInterface()
    app.run()

if __name__ == "__main__":
    show_register_interface()
