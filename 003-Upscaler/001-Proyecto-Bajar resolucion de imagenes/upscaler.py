from PIL import Image
import os

def lower_resolution(input_folder, output_folder, new_width, new_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = os.listdir(input_folder)

    for file_name in files:
        input_path = os.path.join(input_folder, file_name)
        with Image.open(input_path) as img:
            img = img.resize((new_width, new_height), Image.LANCZOS)
            _, ext = os.path.splitext(file_name)
            output_path = os.path.join(output_folder, f"lowered_{file_name}")
            img.save(output_path)

if __name__ == "__main__":
    input_folder = "../carasaltaresolucion"  
    output_folder = "../carasbajaresolucion"  
    new_width = 128  
    new_height = 128  

    lower_resolution(input_folder, output_folder, new_width, new_height)
