from rembg import remove    #pip install rembg onnxruntime

from PIL import Image

# Path img input
input_path = '../data/images/img3.jpg'

# Path img output
output_path = 'img3_sans_fond.png'

input_img = Image.open(input_path) # load img input

output_img = remove(input_img) #suppression du fond de l'img

output_img.save(output_path)
