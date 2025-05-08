# global_variables.py
"""Module for storing global variables shared between GUI files"""
import os

# Store the selected image
selected_image = None

# Store the encoded image
encoded_image = None

# Store the encryption key
encryption_key = None

# Store the encrypted message
encrypted_message = None

# Store the storage path for encoded images
storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encoded_images")
if not os.path.exists(storage_path):
    os.makedirs(storage_path)