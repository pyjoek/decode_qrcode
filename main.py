import cv2 as c
from pyzbar.pyzbar import decode

def read_img(path_image):
    image = c.imread(path_image)
    object = decode(image)

    for obj in object:
        data = obj.data.decode('utf-8')
        print(f"Decoded Data: {data}")

if __name__ == "__main__":
    path_image = input("Enter the path: ")
    read_img(path_image)
