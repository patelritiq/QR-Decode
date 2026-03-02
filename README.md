# QR-Decode 📱

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![pyzbar](https://img.shields.io/badge/pyzbar-0.1.9+-orange.svg)](https://pypi.org/project/pyzbar/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python application that scans and decodes QR codes from images using OpenCV and pyzbar libraries.

---

## Project Statistics 📊

- **2 core libraries** (OpenCV, pyzbar)
- **3 processing steps** (Load → Grayscale → Decode)
- **Multiple QR code support** (scans all QR codes in one image)
- **Performance tracking** (millisecond-level timing)
- **Universal QR support** (URLs, text, contact info, WiFi, etc.)
- **Real-time processing** (near-instant decoding)

---

## Project Overview 🎯

QR-Decode is a learning project built while exploring computer vision, image processing, and QR code technology. It demonstrates practical application of OpenCV for image manipulation and pyzbar for QR code decoding.

### Development Context
- Built as a hands-on learning project for computer vision and image processing
- Explores QR code scanning and decoding techniques
- Demonstrates integration of OpenCV and pyzbar libraries
- Foundation for understanding barcode/QR code recognition systems

### What I Learned
- QR code structure and encoding
- Image preprocessing for better recognition
- Grayscale conversion for efficient processing
- Using pyzbar library for decoding
- Performance measurement and optimization
- Error handling in image processing

---

## How It Works 🔧

The QR code decoding process involves 3 key steps:

1. **Image Loading**
   - Reads image file using OpenCV
   - Validates image data
   - Handles file errors

2. **Grayscale Conversion**
   - Converts RGB/BGR to grayscale
   - Improves decoding accuracy
   - Reduces processing complexity

3. **QR Code Decoding**
   - Uses pyzbar to detect and decode QR codes
   - Extracts data and type information
   - Supports multiple QR codes in single image

---


## Installation & Setup 🛠️

### Prerequisites
- Python 3.8 or higher
- OpenCV library
- pyzbar library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/patelritiq/QR-Decode.git
   cd QR-Decode
   ```

2. **Install required libraries:**
   ```bash
   pip install opencv-python pyzbar
   ```

---

## Usage 📖

1. **Place your QR code image in the project folder**

2. **Update the image path in `QR.py`:**
   ```python
   image_file = "your_qr_image.jpg"
   ```

3. **Run the script:**
   ```bash
   python QR.py
   ```

4. **View the results:**
   - QR code type (QRCODE, etc.)
   - Decoded data (URL, text, etc.)
   - Processing time in milliseconds

---

## Supported QR Code Types 📋

The decoder works with all standard QR code formats:

- **URLs**: Website links
- **Text**: Plain text messages
- **Contact Info**: vCard format
- **WiFi Credentials**: SSID and password
- **Email**: Email addresses
- **Phone Numbers**: Tel links
- **SMS**: Text message links
- **Geo Coordinates**: Location data
- **Calendar Events**: iCal format

---

## Troubleshooting 🔧

### Issue: "Error: Could not open or read image file"

**Solution:**
- Ensure image file exists in the project directory
- Check image filename and extension
- Verify image format is supported

### Issue: "No QR codes found in the image"

**Solution:**
- Ensure QR code is clearly visible
- Check image quality and resolution
- Verify QR code is not damaged or distorted
- Try with better lighting in the image

### Issue: ImportError for pyzbar

**Solution:**
```bash
pip install pyzbar
```

For Windows, you may also need:
```bash
pip install pyzbar[scripts]
```

---

## Limitations ⚠️

- Requires manual image path configuration
- Processes one image at a time
- No real-time camera scanning
- No GUI interface
- Grayscale conversion only (no color QR codes)

---

## Future Enhancements 🔮

- [ ] Real-time webcam QR code scanning
- [ ] GUI for user-friendly operation
- [ ] Batch processing for multiple images
- [ ] Command-line arguments for flexibility
- [ ] QR code generation feature
- [ ] Support for other barcode formats
- [ ] Visual display of QR code location
- [ ] Export decoded data to file

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author 👨‍💻

**Ritik Pratap Singh Patel**

- Computer vision and QR code technology learner
- Image processing enthusiast

---

## Acknowledgments 🙏

This project was developed as a learning exercise in computer vision and QR code technology. It demonstrates practical application of OpenCV and pyzbar for QR code scanning and decoding.

---

## Quick Start 🚀

```bash
# Clone repository
git clone https://github.com/patelritiq/QR-Decode.git
cd QR-Decode

# Install dependencies
pip install opencv-python pyzbar

# Run the program
python QR.py
```

Scan and decode QR codes instantly! 📱✨
