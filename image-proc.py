from PIL import Image
filename = "images/cute.png"

with Image.open(filename) as img:
    img = img.convert('RGB') # this is done to avert OSError err cause of JPG doesn't support transparency
    img.load()

# img.show() # - this show the image using the system image viewer
# img.format # - this shows the format of the image eg jpeg, png etc
# img.size # - this show the size of the image
# img.mode # - this shows the mode of the image eg 'RGB';
    
# To Crop image use .crop((left, upper, right, bottom))
cropped_img = img.crop((300, 150, 700, 1000))
# cropped_img.show()

low_res_img = cropped_img.resize(
    (cropped_img.width // 4, cropped_img.height // 4)
)

# low_res_img.show()
low_res_img = cropped_img.reduce(4)
img.thumbnail((200, 200))

# img.size
cropped_img.save("images/cropped_cute_image.jpg")
low_res_img.save("images/low_res_cute_image.png")