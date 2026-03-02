import cv2
import pyzbar.pyzbar as pyzbar
import time

def scan_qr_code(image_path):
    """
    Scans and decodes QR codes from an image file.
    
    Args:
        image_path: Path to the image file containing QR code(s)
        
    Returns:
        List of decoded QR code objects or None if error occurs
    """
    try:
        start_time = time.time()

        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not open or read image file: {image_path}")
            print("Please ensure the image file exists and is in a supported format.")
            return None

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        decoded_objects = pyzbar.decode(gray)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(f"QR code scanning took: {elapsed_time:.2f} ms")

        return decoded_objects

    except cv2.error as e:
        print(f"OpenCV error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def main():
    image_file = "qrc.jpg"

    print(f"Scanning QR code from: {image_file}")
    decoded_data = scan_qr_code(image_file)

    if decoded_data:
        print(f"\nFound {len(decoded_data)} QR code(s):\n")
        for i, obj in enumerate(decoded_data, 1):
            print(f"QR Code #{i}:")
            print(f"  Type: {obj.type}")
            print(f"  Data: {obj.data.decode('utf-8')}")
            print()
    else:
        print("No QR codes found in the image.")

if __name__ == "__main__":
    main()
