import cv2
import numpy as np
import os

def process_image(filepath, filename, output_folder):
    img = cv2.imread(filepath)
    processed_files = []

    # GrayScale
    gray_file = f"gray_{filename}"
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(output_folder, gray_file), gray)
    processed_files.append(gray_file)

    # Gaussian Blur
    blur_file = f"blur_{filename}"
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite(os.path.join(output_folder, blur_file), blur)
    processed_files.append(blur_file)

    # Sepia
    sepia_file = f"sepia_{filename}"
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, sepia_filter)
    sepia = np.clip(sepia, 0, 255)
    cv2.imwrite(os.path.join(output_folder, sepia_file), sepia)
    processed_files.append(sepia_file)

    # Edge Detection
    edges_file = f"edges_{filename}"
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(os.path.join(output_folder, edges_file), edges)
    processed_files.append(edges_file)

    return processed_files