import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory


# prompt user for folders
Tk().withdraw()
jpeg_folder = askdirectory(title='Select folder with jpeg images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exists, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the jpeg folder
for file_name in os.listdir(jpeg_folder):
    if file_name.endswith('.jpeg') or file_name.endswith('.JPEG'):
        # open jpeg image and convert to RGB
        jpeg_image = Image.open(os.path.join(jpeg_folder, file_name))
        jpeg_image = jpeg_image.convert('RGB')

        # create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # save jpg image with maximum quality
        jpeg_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All jpeg images in {jpeg_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug