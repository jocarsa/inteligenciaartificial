from PIL import Image
import numpy as np
import cv2

def angulo(imagen):
    image = imagen  # Replace with your image file name
    gray_image = image.convert("L")
    image_array = np.array(gray_image)
    edges = cv2.Canny(image_array, threshold1=30, threshold2=100)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    x1, y1, x2, y2 = cv2.boundingRect(largest_contour)
    delta_x = x2 - x1
    delta_y = y2 - y1
    angle_rad = np.arctan2(delta_y, delta_x)
    angle_deg = np.degrees(angle_rad)
    return angle_deg

print(angulo(Image.open("prueba.jpg")))
