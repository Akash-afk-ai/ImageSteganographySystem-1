import numpy as np
from PIL import Image
import cv2
import os

class SteganographyDetector:
    def __init__(self):
        pass
        
    def calculate_noise_level(self, image_path):
        """Calculate noise level in the image"""
        try:
            img = cv2.imread(image_path)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Calculate noise using Laplacian
            noise = cv2.Laplacian(gray, cv2.CV_64F).var()
            return noise
        except Exception as e:
            print(f"Error calculating noise level: {e}")
            return 0.0
    
    def calculate_entropy(self, image_path):
        """Calculate image entropy"""
        try:
            img = cv2.imread(image_path)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Calculate histogram
            hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
            hist = hist.ravel() / hist.sum()
            # Calculate entropy
            entropy = -np.sum(hist * np.log2(hist + 1e-7))
            return entropy
        except Exception as e:
            print(f"Error calculating entropy: {e}")
            return 0.0
    
    def detect_steganography(self, image_path):
        """Detect steganographic content in image using heuristic approach"""
        results = {
            'steganography_probability': 0.0,
            'noise_level': 0.0,
            'entropy': 0.0,
            'is_steganographic': False
        }
        
        try:
            # Calculate noise level and entropy
            results['noise_level'] = self.calculate_noise_level(image_path)
            results['entropy'] = self.calculate_entropy(image_path)
            
            # Use heuristic approach based on noise and entropy levels
            noise_threshold = 100.0
            entropy_threshold = 7.0
            
            if results['noise_level'] > noise_threshold or results['entropy'] > entropy_threshold:
                results['steganography_probability'] = 0.7
                results['is_steganographic'] = True
            else:
                results['steganography_probability'] = 0.3
                results['is_steganographic'] = False
            
            return results
            
        except Exception as e:
            print(f"Error detecting steganography: {e}")
            return results 