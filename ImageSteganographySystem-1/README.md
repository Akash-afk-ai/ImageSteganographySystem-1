# AI-Based Steganography & Hidden Malware Detector

## Project Overview
This project implements an AI-based system for detecting hidden messages and malware in images using steganography techniques. The system combines deep learning with traditional security analysis methods to provide comprehensive detection capabilities.

## Features
- Image steganography detection using CNN
- Hidden malware detection in steganographic content
- Multiple detection methods:
  - Deep learning-based pattern recognition
  - YARA rules scanning
  - Hash-based malware detection
  - PE file analysis
  - Suspicious pattern detection
- User-friendly GUI interface
- Secure user authentication
- Real-time analysis and reporting

## Tech Stack
- **Frontend**: Tkinter (Python GUI)
- **Backend**: Python
- **AI/ML**: TensorFlow, Keras
- **Image Processing**: OpenCV, PIL
- **Security Analysis**: YARA, PEfile, python-magic
- **Data Processing**: NumPy, scikit-learn

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/steganography-detector.git
cd steganography-detector
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the application:
```bash
python main.py
```

2. Login or register a new account
3. Choose between encoding or decoding images
4. For detection:
   - Select an image to analyze
   - The system will automatically detect:
     - Hidden steganographic content
     - Potential malware
     - Suspicious patterns
   - View detailed analysis results

## Project Structure
```
├── main.py                 # Main application entry point
├── gui.py                  # Login interface
├── gui2.py                 # Registration interface
├── gui3.py                 # Home interface
├── gui4.py                 # Encoding interface
├── gui5.py                 # Decoding interface
├── gui6.py                 # Results interface
├── steg_detector.py        # Steganography detection module
├── malware_detector.py     # Malware detection module
├── steganography_functions.py  # Core steganography functions
├── requirements.txt        # Project dependencies
└── assets/                 # GUI assets
    ├── frame0/            # Login interface assets
    ├── frame1/            # Registration interface assets
    ├── frame2/            # Home interface assets
    ├── frame3/            # Encoding interface assets
    ├── frame4/            # Decoding interface assets
    └── frame5/            # Results interface assets
```

## AI/ML Components
1. **Steganography Detection**
   - CNN-based model for detecting hidden content
   - Trained on StegExpose dataset
   - Features: noise analysis, entropy calculation

2. **Malware Detection**
   - Multiple detection methods:
     - Deep learning pattern recognition
     - YARA rules matching
     - Hash-based detection
     - PE file analysis
     - Suspicious pattern detection

## Security Features
- Secure password hashing using bcrypt
- SQLite database for user management
- Input validation and sanitization
- Secure file handling

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- StegExpose dataset for training data
- YARA project for malware detection rules
- TensorFlow and Keras communities
