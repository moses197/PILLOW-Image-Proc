from PIL import Image
filename = "images/cute.png"

with Image.open(filename) as img:
    img = img.convert('RGB') # this is done to avert OSError err cause of JPG doesn't support transparency
    img.load()


convert_img =  img.transpose(Image.FLIP_TOP_BOTTOM)
# convert_img.show()

rotate_img = img.rotate(45)
# rotate_img.show()

rotate_img = img.rotate(45, expand=True)
# rotate_img.show()

