from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import subprocess
from PIL import ImageTk, Image
import global_variables
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame6"


def open_login_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def open_encoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui4.py"])
    window.destroy()  # Close the current interface

def open_decoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui5.py"])
    window.destroy()  # Close the current interface

def save_image():
    if global_variables.encoded_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            global_variables.encoded_image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
    else:
        messagebox.showerror("Error", "No encoded image to save!")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ResultsInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX - Results")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        # Initialize storage path if not set
        if not hasattr(global_variables, 'storage_path'):
            global_variables.storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encoded_images")
            if not os.path.exists(global_variables.storage_path):
                os.makedirs(global_variables.storage_path)
        
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
        
        # Add success message
        self.canvas.create_text(
            343.0,
            74.0,
            anchor="nw",
            text="Image Successfully encoded!",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Create frames for images
        self.original_frame = tk.Frame(self.window, width=270, height=178, bg="#D9D9D9")
        self.original_frame.place(x=114, y=148)
        
        self.encoded_frame = tk.Frame(self.window, width=270, height=178, bg="#D9D9D9")
        self.encoded_frame.place(x=479, y=148)
        
        # Display original image
        if global_variables.selected_image:
            # Resize image to fit the frame
            original_img = global_variables.selected_image.copy()
            original_img.thumbnail((270, 178))
            self.original_photo = ImageTk.PhotoImage(original_img)
            
            original_label = tk.Label(self.original_frame, image=self.original_photo, bg="#D9D9D9")
            original_label.image = self.original_photo
            original_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Display encoded image
        if global_variables.encoded_image:
            # Resize image to fit the frame
            encoded_img = global_variables.encoded_image.copy()
            encoded_img.thumbnail((270, 178))
            self.encoded_photo = ImageTk.PhotoImage(encoded_img)
            
            encoded_label = tk.Label(self.encoded_frame, image=self.encoded_photo, bg="#D9D9D9")
            encoded_label.image = self.encoded_photo
            encoded_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Add image labels
        self.canvas.create_text(
            196.0,
            331.0,
            anchor="nw",
            text="Original Image",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        self.canvas.create_text(
            561.0,
            331.0,
            anchor="nw",
            text="Encoded Image",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add storage location label
        self.canvas.create_text(
            114.0,
            360.0,
            anchor="nw",
            text="Storage Location:",
            fill="#FFFFFF",
            font=("Arial", 12)
        )
        
        # Add storage location display
        self.storage_label = tk.Label(
            self.window,
            text=getattr(global_variables, 'storage_path', 'Not set'),
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            anchor="w",
            padx=5
        )
        self.storage_label.place(
            x=114.0,
            y=380.0,
            width=635.0,
            height=25.0
        )
        
        # Add buttons
        self.button_save = Button(
            text="Save",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.save_image,
            relief="flat",
            width=10,
            height=1
        )
        self.button_save.place(x=320.0, y=420.0)
        
        self.button_decode = Button(
            text="Decode",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.open_decoding_interface,
            relief="flat",
            width=10,
            height=1
        )
        self.button_decode.place(x=396.0, y=420.0)
        
        self.button_encode = Button(
            text="New Encode",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.open_encoding_interface,
            relief="flat",
            width=10,
            height=1
        )
        self.button_encode.place(x=472.0, y=420.0)
        
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
        self.button_home.place(x=748.0, y=29.0)
        
        # Auto-save the encoded image
        if global_variables.encoded_image:
            self.auto_save_image()
    
    def auto_save_image(self):
        """Automatically save the encoded image"""
        try:
            # Create filename with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"encoded_image_{timestamp}.png"
            
            # Save to the selected storage location
            save_path = os.path.join(global_variables.storage_path, filename)
            global_variables.encoded_image.save(save_path)
            
            # Update storage label
            self.storage_label.config(text=save_path)
            
            messagebox.showinfo("Success", f"Image automatically saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to auto-save image: {str(e)}")
    
    def save_image(self):
        """Handle manual save image"""
        if global_variables.encoded_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Files", "*.png")],
                initialdir=getattr(global_variables, 'storage_path', os.path.dirname(os.path.abspath(__file__))),
                initialfile="encoded_image.png"
            )
            if file_path:
                try:
                    global_variables.encoded_image.save(file_path)
                    self.storage_label.config(text=file_path)
                    messagebox.showinfo("Success", f"Image saved successfully to:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {str(e)}")
        else:
            messagebox.showerror("Error", "No encoded image to save!")
    
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
    
    def open_home_interface(self):
        """Open the home interface"""
        self.window.withdraw()
        subprocess.Popen(["python", "gui3.py"])
        self.window.destroy()
    
    def run(self):
        """Run the interface"""
        self.window.resizable(False, False)
        self.window.mainloop()

if __name__ == "__main__":
    app = ResultsInterface()
    app.run()
