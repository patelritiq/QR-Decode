import cv2
import pyzbar.pyzbar as pyzbar
import time

def scan_qr_code(image_path):
    try:
        start_time = time.time()

        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not open or read image file: {image_path}")
            return None

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        decoded_objects = pyzbar.decode(gray)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(f"QR code scanning took: {elapsed_time:.2f} ms")

        return decoded_objects

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def main():
    image_file = "qrc.jpg"

    decoded_data = scan_qr_code(image_file)

    if decoded_data:
        for obj in decoded_data:
            print("Type:", obj.type)
            print("Data:", obj.data.decode("utf-8"))
    else:
        print("No QR codes found in the image.")

if __name__ == "__main__":
    main()
