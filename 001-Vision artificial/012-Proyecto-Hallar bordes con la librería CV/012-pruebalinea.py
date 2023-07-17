from PIL import Image
import numpy as np
import cv2

# Load the image
image = Image.open("prueba.jpg")  # Replace with your image file name

# Convert the image to grayscale
gray_image = image.convert("L")

# Convert the grayscale image to a NumPy array
image_array = np.array(gray_image)

# Apply Canny edge detection
edges = cv2.Canny(image_array, threshold1=30, threshold2=100)

# Find contours in the edges
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour (assuming it represents the line)
largest_contour = max(contours, key=cv2.contourArea)

# Get the line endpoints
x1, y1, x2, y2 = cv2.boundingRect(largest_contour)

# Calculate the angle of the line
delta_x = x2 - x1
delta_y = y2 - y1
angle_rad = np.arctan2(delta_y, delta_x)
angle_deg = np.degrees(angle_rad)

print("Line angle (in degrees):", angle_deg)
