import os
import fitz
import base64

def convert_pdf_to_images(pdf_path, output_folder):
    image_name = f"{os.path.basename(pdf_path)}.png"
    image_path = os.path.join(output_folder, image_name)
    image_base64 = []
    with fitz.open(pdf_path) as doc:
        page = doc[0]
        pix = page.get_pixmap()
        pix.save(image_path)
    image_base64.append(base64.b64encode(open(image_path, "rb").read()).decode('utf-8'))
    os.remove(image_path)
    return image_base64