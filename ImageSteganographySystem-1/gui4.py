from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import subprocess
from PIL import Image
import global_variables
import os

class EncodeInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX - Encode")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        # Initialize storage path
        self.storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encoded_images")
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
        
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
        
        # Add title
        self.canvas.create_text(
            298.0,
            28.0,
            anchor="nw",
            text="Encoding with StegaX!",
            fill="#FFFFFF",
            font=("Arial", 24)
        )
        
        # Add instructions
        self.canvas.create_text(
            318.0,
            74.0,
            anchor="nw",
            text="1. Write the message you want to hide",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        self.canvas.create_text(
            351.0,
            92.0,
            anchor="nw",
            text="2. Add the encryption code",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        self.canvas.create_text(
            369.0,
            110.0,
            anchor="nw",
            text="3. Choose the image",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add message entry label
        self.canvas.create_text(
            308.0,
            145.0,
            anchor="nw",
            text="Secret Message:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add message entry
        self.entry_message = Entry(
            self.window,
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_message.place(
            x=308.0,
            y=167.0,
            width=246.0,
            height=40.0
        )
        
        # Add encryption key label
        self.canvas.create_text(
            308.0,
            246.0,
            anchor="nw",
            text="Encryption Key:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add encryption key entry
        self.entry_key = Entry(
            self.window,
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_key.place(
            x=308.0,
            y=268.0,
            width=246.0,
            height=31.0
        )
        
        # Add image path label
        self.canvas.create_text(
            308.0,
            306.0,
            anchor="nw",
            text="Input Image:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add image path entry
        self.entry_image = Entry(
            self.window,
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_image.place(
            x=308.0,
            y=328.0,
            width=246.0,
            height=29.0
        )
        
        # Add storage path label
        self.canvas.create_text(
            308.0,
            366.0,
            anchor="nw",
            text="Storage Location:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add storage path entry
        self.entry_storage = Entry(
            self.window,
            bd=0,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_storage.place(
            x=308.0,
            y=388.0,
            width=246.0,
            height=29.0
        )
        self.entry_storage.insert(0, self.storage_path)
        
        # Add buttons
        self.button_select = Button(
            text="Select Image",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.open_file_dialog,
            relief="flat",
            width=15,
            height=1
        )
        self.button_select.place(x=564.0, y=328.0)
        
        # Add storage location button
        self.button_storage = Button(
            text="Change Location",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.select_storage_location,
            relief="flat",
            width=15,
            height=1
        )
        self.button_storage.place(x=564.0, y=388.0)
        
        self.button_encode = Button(
            text="Encode",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.encode_photo,
            relief="flat",
            width=15,
            height=1
        )
        self.button_encode.place(x=336.0, y=440.0)
        
        self.button_home = Button(
            text="Home",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.open_home_interface,
            relief="flat",
            width=10,
            height=1
        )
        self.button_home.place(x=739.0, y=30.0)
    
    def open_file_dialog(self):
        """Handle file selection"""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            global_variables.selected_image = Image.open(file_path)
            self.entry_image.delete(0, tk.END)
            self.entry_image.insert(0, file_path)
    
    def select_storage_location(self):
        """Handle storage location selection"""
        folder_path = filedialog.askdirectory(title="Select Storage Location")
        if folder_path:
            self.storage_path = folder_path
            self.entry_storage.delete(0, tk.END)
            self.entry_storage.insert(0, folder_path)
    
    def encrypt(self, message, key):
        """Encrypt the message using the key"""
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + int(''.join(filter(str.isdigit, key)))) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) - ord('a') + int(''.join(filter(str.isdigit, key)))) % 26 + ord('a'))
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message
    
    def encode_photo(self):
        """Handle encoding functionality"""
        if not global_variables.selected_image:
            messagebox.showwarning("Warning", "Please select an image first")
            return
            
        if not self.entry_message.get():
            messagebox.showwarning("Warning", "Please enter a message to hide")
            return
            
        if not self.entry_key.get():
            messagebox.showwarning("Warning", "Please enter an encryption key")
            return
            
        try:
            # Encrypt the message
            message = self.entry_message.get()
            key = self.entry_key.get()
            encrypted_message = self.encrypt(message, key)
            
            # Save the current state
            global_variables.encrypted_message = encrypted_message
            global_variables.encryption_key = key
            global_variables.storage_path = self.storage_path
            
            # Open the after-encode interface
            self.window.withdraw()
            subprocess.Popen(["python", "gui6.py"])
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during encoding: {str(e)}")
    
    def open_home_interface(self):
        """Open the home interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui3.py"])
        self.window.destroy()
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

def show_encoding_interface():
    """Show the encoding interface"""
    app = EncodeInterface()
    app.run()

if __name__ == "__main__":
    show_encoding_interface()
