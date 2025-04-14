from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw
import os

def os_path_join(asset_path, string_name):
    return os.path.join(asset_path, string_name)

### open an image using the context manager
def image_editor():
    # B:\CODES\Python-Related\PYQT-PROJECT\Image-Editing-App
    assets_path = os.path.join(os.getcwd(), "assets")

    # print(os.listdir(assets_path)) # returns a list

    # B:\CODES\Python-Related\PYQT-PROJECT\Image-Editing-App\assets\woodland_path.jpg
    woodland_jpg = os.path.join(assets_path, "woodland_path.jpg")

    with Image.open(woodland_jpg) as picture:
        # picture.show()

        black_and_white = picture.convert("L")
        # black_and_white.show()
        
        # to save this use the save method
        # NOTE: Remember that you need to save the extension the same as the original one.
        black_and_white.save(os_path_join(assets_path, "greyed_woodland.jpg"))

        # using the ImageOps to flip a picture
        mirror = ImageOps.flip(picture)
        mirror.save(os_path_join(assets_path, "mirror.jpg"))
        
        # Blurry
        blur = picture.filter(ImageFilter.BLUR)
        # blur.save(os_path_join(assets_path, "blurred.jpg"))
        
        # Image Enhancement
        constrast = ImageEnhance.Contrast(picture)
        constrast = constrast.enhance(2.5)
        # constrast.save(os_path_join(assets_path, "contrast.jpg"))


        # Color
        color = ImageEnhance.Color(picture).enhance(2.5)
        color.save(os_path_join(assets_path, "color.jpg"))

        # rotate
        left = picture.transpose(Image.ROTATE_90)
        left.show()

# image_editor() 


# creating an image from nothing using ImageDraw and .new method from the Image class
def image_creation():
    assets_path = os.path.join(os.getcwd(), "assets")

    im = Image.new("RGB", (500, 300), (128, 128, 128))
    draw = ImageDraw.Draw(im)

    draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

    im.save(
        os.path.join(assets_path, "pillow_imagedraw.jpg")
    )

# image_creation()