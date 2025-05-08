from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import subprocess
from PIL import Image, ImageTk
from steg_detector import SteganographyDetector
from malware_detector import MalwareDetector

class DetectionInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("StegaX - Detection")
        self.window.geometry("862x519")
        self.window.configure(bg="#093545")
        
        # Initialize detectors
        self.steg_detector = SteganographyDetector()
        self.malware_detector = MalwareDetector()
        
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
            text="Steganography & Malware Detection",
            fill="#FFFFFF",
            font=("Arial", 24)
        )
        
        # Add file selection button
        self.button_select = Button(
            text="Select File",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.select_file,
            relief="flat",
            width=20,
            height=2
        )
        self.button_select.place(
            x=336.0,
            y=100.0
        )
        
        # Add encode button
        self.button_encode = Button(
            text="Encode",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.encode,
            relief="flat",
            width=20,
            height=2
        )
        self.button_encode.place(
            x=336.0,
            y=150.0
        )
        
        # Add detection button
        self.button_detect = Button(
            text="Detect",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.detect,
            relief="flat",
            width=20,
            height=2
        )
        self.button_detect.place(
            x=336.0,
            y=200.0
        )
        
        # Add home button
        self.button_home = Button(
            text="Home",
            font=("Arial", 12),
            bg="#224957",
            fg="#FFFFFF",
            command=self.open_home_interface,
            relief="flat",
            width=10,
            height=2
        )
        self.button_home.place(
            x=739.0,
            y=30.0
        )
        
        # Add results text area
        self.results_text = Text(
            self.window,
            bg="#224957",
            fg="#FFFFFF",
            font=("Arial", 12),
            wrap=tk.WORD,
            width=60,
            height=15
        )
        self.results_text.place(x=250, y=250)
        
        # Initialize selected file
        self.selected_file = None
    
    def select_file(self):
        """Handle file selection"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.selected_file = file_path
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Selected file: {file_path}\n")
    
    def encode(self):
        """Handle encoding functionality"""
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first")
            return
            
        try:
            # Open the encode interface
            self.window.withdraw()
            subprocess.Popen(["python", "gui4.py"])
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error opening encode interface: {str(e)}")
    
    def detect(self):
        """Perform detection on selected file"""
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first")
            return
        
        try:
            # Clear previous results
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Analyzing file...\n\n")
            
            # Perform steganography detection
            steg_results = self.steg_detector.detect_steganography(self.selected_file)
            
            # Perform malware detection
            malware_results = self.malware_detector.detect_malware(self.selected_file)
            
            # Display results
            self.display_results(steg_results, malware_results)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during detection: {str(e)}")
    
    def display_results(self, steg_results, malware_results):
        """Display detection results"""
        self.results_text.delete(1.0, tk.END)
        
        # Display steganography results
        self.results_text.insert(tk.END, "=== Steganography Detection Results ===\n\n")
        self.results_text.insert(tk.END, f"Probability of hidden content: {steg_results['steganography_probability']:.2%}\n")
        self.results_text.insert(tk.END, f"Noise level: {steg_results['noise_level']:.4f}\n")
        self.results_text.insert(tk.END, f"Entropy: {steg_results['entropy']:.4f}\n")
        self.results_text.insert(tk.END, f"Contains steganographic content: {'Yes' if steg_results['is_steganographic'] else 'No'}\n\n")
        
        # Display malware results
        self.results_text.insert(tk.END, "=== Malware Detection Results ===\n\n")
        self.results_text.insert(tk.END, f"Malware detected: {'Yes' if malware_results['is_malware'] else 'No'}\n")
        self.results_text.insert(tk.END, f"Confidence: {malware_results['confidence']:.2%}\n")
        self.results_text.insert(tk.END, f"Threat level: {malware_results['threat_level']}\n")
        
        if malware_results['detection_methods']:
            self.results_text.insert(tk.END, "\nDetection methods:\n")
            for method in malware_results['detection_methods']:
                self.results_text.insert(tk.END, f"- {method}\n")
        
        if malware_results['details']:
            self.results_text.insert(tk.END, "\nDetails:\n")
            for key, value in malware_results['details'].items():
                self.results_text.insert(tk.END, f"- {key}: {value}\n")
    
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
    app = DetectionInterface()
    app.run() 