from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import subprocess
from PIL import Image
from steganography_functions import decode_lsb
import os
import tempfile

class DecodeInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX - Decode")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        self.selected = None
        self.temp_file = None
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
        
        # Add title with a background
        self.canvas.create_rectangle(
            200, 10, 662, 60,
            fill="#224957",
            outline=""
        )
        self.canvas.create_text(
            431.0,
            35.0,
            anchor="center",
            text="Decoding with StegaX!",
            fill="#FFFFFF",
            font=("Arial", 24, "bold")
        )
        
        # Add instructions box
        self.canvas.create_rectangle(
            250, 70, 612, 130,
            fill="#224957",
            outline=""
        )
        self.canvas.create_text(
            431.0,
            85.0,
            anchor="center",
            text="1. Choose the Encrypted image",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        self.canvas.create_text(
            431.0,
            110.0,
            anchor="center",
            text="2. Enter the encryption key and decode",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add file selection box
        self.canvas.create_rectangle(
            250, 140, 612, 200,
            fill="#224957",
            outline=""
        )
        self.canvas.create_text(
            280.0,
            155.0,
            anchor="nw",
            text="Image Path:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add file path entry
        self.entry_1 = Entry(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000000",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_1.place(
            x=280.0,
            y=175.0,
            width=250.0,
            height=30.0
        )
        
        # Add locate button
        self.button_locate = Button(
            text="Browse",
            font=("Arial", 12),
            bg="#20B2AA",
            fg="#FFFFFF",
            command=self.open_file_dialog,
            relief="flat",
            width=10,
            height=1
        )
        self.button_locate.place(x=540.0, y=175.0)
        
        # Add encryption key box
        self.canvas.create_rectangle(
            250, 210, 612, 270,
            fill="#224957",
            outline=""
        )
        self.canvas.create_text(
            280.0,
            225.0,
            anchor="nw",
            text="Encryption Key:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add encryption key entry
        self.entry_2 = Entry(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000000",
            font=("Arial", 12),
            highlightthickness=0
        )
        self.entry_2.place(
            x=280.0,
            y=245.0,
            width=250.0,
            height=30.0
        )
        
        # Add decode button
        self.button_decode = Button(
            text="Decode Message",
            font=("Arial", 12, "bold"),
            bg="#20B2AA",
            fg="#FFFFFF",
            command=self.decode_photo,
            relief="flat",
            width=15,
            height=1
        )
        self.button_decode.place(x=540.0, y=245.0)
        
        # Add results box
        self.canvas.create_rectangle(
            250, 280, 612, 400,
            fill="#224957",
            outline=""
        )
        self.canvas.create_text(
            280.0,
            295.0,
            anchor="nw",
            text="Decoded Message:",
            fill="#FFFFFF",
            font=("Arial", 12, "bold")
        )
        
        # Add decoded message text
        self.final_text = self.canvas.create_text(
            431.0,
            340.0,
            anchor="center",
            fill="#FFFFFF",
            font=("Arial", 12),
            width=300
        )
        
        # Add status bar
        self.canvas.create_rectangle(
            0, 480, 862, 519,
            fill="#224957",
            outline=""
        )
        
        # Add home button
        self.button_home = Button(
            text="Home",
            font=("Arial", 12),
            bg="#20B2AA",
            fg="#FFFFFF",
            command=self.open_home_interface,
            relief="flat",
            width=10,
            height=1
        )
        self.button_home.place(x=739.0, y=490.0)
        
        # Add version text
        self.canvas.create_text(
            20.0,
            490.0,
            anchor="nw",
            text="StegaX v1.0",
            fill="#FFFFFF",
            font=("Arial", 10)
        )
        
        # Add a frame for the decoded message
        self.message_frame = tk.Frame(
            self.window,
            bg="#224957",
            highlightthickness=0
        )
        self.message_frame.place(x=280, y=320, width=300, height=60)
        
        # Add a text widget for the decoded message
        self.message_text = tk.Text(
            self.message_frame,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            wrap=tk.WORD,
            width=30,
            height=3,
            relief="flat",
            highlightthickness=0
        )
        self.message_text.pack(expand=True, fill="both")
        self.message_text.config(state="disabled")
    
    def convert_to_png(self, image_path):
        """Convert JPG/JPEG image to PNG format"""
        try:
            # Create a temporary file for the PNG
            temp_dir = tempfile.gettempdir()
            temp_png = os.path.join(temp_dir, "temp_decode.png")
            
            # Open and convert the image
            img = Image.open(image_path)
            img.save(temp_png, "PNG")
            
            # Store the temp file path for cleanup
            self.temp_file = temp_png
            
            return temp_png
        except Exception as e:
            messagebox.showerror("Error", f"Error converting image: {str(e)}")
            return None
    
    def open_file_dialog(self):
        """Handle file selection"""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Convert JPG/JPEG to PNG if needed
            if file_path.lower().endswith(('.jpg', '.jpeg')):
                png_path = self.convert_to_png(file_path)
                if png_path:
                    self.selected = Image.open(png_path)
                    self.entry_1.delete(0, tk.END)
                    self.entry_1.insert(0, f"{file_path} (converted to PNG)")
            else:
                self.selected = Image.open(file_path)
                self.entry_1.delete(0, tk.END)
                self.entry_1.insert(0, file_path)
    
    def decrypt(self, encrypted_message, key):
        """Decrypt the message using the key"""
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - int(''.join(filter(str.isdigit, key)))) % 26 + ord('A'))
                else:
                    decrypted_char = chr((ord(char) - ord('a') - int(''.join(filter(str.isdigit, key)))) % 26 + ord('a'))
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message
    
    def decode_photo(self):
        """Decode the hidden message from the image"""
        if self.selected is None:
            messagebox.showwarning("Warning", "Please select an image first")
            return
            
        if not self.entry_2.get():
            messagebox.showwarning("Warning", "Please enter the encryption key")
            return
            
        try:
            # Perform decoding using the selected photo
            decoded_message = decode_lsb(self.selected)
            if not decoded_message:
                messagebox.showwarning("Warning", "No hidden message found in the image")
                return
                
            # Decrypt the message
            key = self.entry_2.get()
            final = self.decrypt(decoded_message, key)
            
            # Display the decoded message in the text widget
            self.message_text.config(state="normal")
            self.message_text.delete(1.0, tk.END)
            self.message_text.insert(tk.END, final)
            self.message_text.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during decoding: {str(e)}")
    
    def open_home_interface(self):
        """Open the home interface"""
        # Clean up temporary file if it exists
        if self.temp_file and os.path.exists(self.temp_file):
            try:
                os.remove(self.temp_file)
            except:
                pass
        
        self.window.withdraw()
        subprocess.Popen(["python", "gui3.py"])
        self.window.destroy()
    
    def relative_to_assets(self, path: str) -> Path:
        """Get the path to an asset file"""
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets" / "frame5"
        return ASSETS_PATH / Path(path)
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

def show_decoding_interface():
    """Show the decoding interface"""
    app = DecodeInterface()
    app.run()

if __name__ == "__main__":
    show_decoding_interface()
