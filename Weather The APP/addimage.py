from PIL import Image
from IPython.display import display  # For Jupyter notebooks

# Open an image file
image_path = "D:\Coding\Python\Weather The APP\Images\Layer 7.png"  # Replace with the actual path to your image
img = Image.open(image_path)

# Display the image
img.show()

# If you are using a Jupyter notebook or IPython, you can use the following instead of img.show():
# display(img)
