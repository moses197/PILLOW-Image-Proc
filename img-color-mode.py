from PIL import Image
filename = "images/cute.png"

with Image.open(filename) as img:
    img = img.convert('RGB') # this is done to avert OSError err cause of JPG doesn't support transparency
    img.load()


cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")
# cmyk_img.show()
# gray_img.show()

x = img.getbands()
y = cmyk_img.getbands()
z = gray_img.getbands()

# print(f"img band is: {x}\ncmyk_img band is: {y}\ngray_img band  is: {z} ")

red, green, blue = img.split()
# print(red.mode)

zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))

green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))

blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

red_merge.show()
# green_merge.show()
# blue_merge.show()