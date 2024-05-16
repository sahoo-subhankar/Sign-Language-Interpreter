import cv2
import os

def flip_images():
    gest_folder = "gestures"
    for g_id in os.listdir(gest_folder):
        for i in range(450):
            path = os.path.join(gest_folder, g_id, str(i+1) + ".jpg")
            new_path = os.path.join(gest_folder, g_id, str(i+1+433) + ".jpg")
            print("Processing:", path)  # Debug print statement
            if not os.path.isfile(path):
                print("Error: File not found -", path)  # Error handling
                continue
            img = cv2.imread(path, 0)
            if img is None:
                print("Error: Failed to read image -", path)  # Error handling
                continue
            img = cv2.flip(img, 1)
            cv2.imwrite(new_path, img)
            print("Flipped image saved to:", new_path)  # Debug print statement

flip_images()
