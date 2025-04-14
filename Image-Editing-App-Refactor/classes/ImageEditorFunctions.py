import os
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Slot
from PIL import ImageEnhance, ImageFilter, Image, ImageOps, ImageQt

class ImageEditorFunctions():
    def __init__(self, instance):
        self.instance = instance
    
    def select_folder_function(self):
        file_path = QFileDialog.getExistingDirectory()

        # .file_path is living inside the ImageEditorWidgets
        
        if file_path and isinstance(file_path, str):
            self.instance.file_path = file_path

            self.list_data_to_list_box(
                instance=self.instance,
                file_path=file_path
            )
    
    def list_data_to_list_box(self, instance, file_path):
        path = os.listdir(file_path)
        
        for file in path:
            if file.endswith(("png", "jpeg", "bmp", "jpg")):
                instance.file_list.addItem(file)
    
    @Slot(str) # <optional> a good practice if this method uses a Signal
    def on_file_select_emit(self, file_name):
        """
        This functions ties with the CustomListWidget class from the ImageEditorDesigns

        Args:
            file_name: this is auto-generated because it will be used as a variable that was return in the fileSelected emit method. Which is the name of the file that was selected. No need to supply this with arguments. Like a decorator? or just put a @Slot on top?
        """

        # create a Qpixmap opener here
        image_path = os.path.join(self.instance.file_path, file_name)

        # reassign variable to the ImageEditorWidget instance attribute image_exact_path
        self.instance.image_exact_path = image_path

        self.instance.pixmap.load(image_path)
        
        # get the main widget width and height
        width = self.instance.width()
        height = self.instance.height()

        # scaling the pixmap (custom)
        scaled_pixmap = self.instance.pixmap.scaled(
            (width - 300),
            (height - 100),
            Qt.KeepAspectRatio
        )

        self.instance.picture_box.setPixmap(scaled_pixmap)

        # create a pixmap opener
        # select_image_to_render(
        #     image_path=self.instance.file_path,
        #     filename=file_name,
        #     pix_map_instance=self.instance.pixmap,
        #     qLabel=self.instance.picture_box,
        #     container=self.instance
        # )
        

    # add functinalities for the combo box here
    def combo_box_function(self):
        current_text = self.instance.combo_box.currentText()
        map_functions = {
            "B/W": lambda image: image.convert("L"),
            "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
            "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2),
            "Blur": lambda image: image.filter(ImageFilter.BLUR),
            "Left": lambda image: image.transpose(Image.ROTATE_90),
            "Right": lambda image: image.transpose(Image.ROTATE_270),
            "Mirror":  lambda image: ImageOps.flip(image),
            "Sharpen":  lambda image: image.filter(ImageFilter.SHARPEN),
        }

        # create a qt image first
        if self.instance.image_exact_path: 
            with Image.open(self.instance.image_exact_path) as image:
                qt_image = ImageQt.ImageQt(image)
                pixmap = QPixmap.fromImage(qt_image)

                if current_text and current_text != "Original" and self.instance.image_exact_path:
                    filter_function = map_functions.get(current_text)

                    if filter_function:
                        # with Image.open(self.instance.image_exact_path) as image:
                        filtered_image = filter_function(image)
                    
                        # convert to Qt Image first
                        qt_image = ImageQt.ImageQt(filtered_image)
                        pixmap = QPixmap.fromImage(qt_image)

                        # display on the QLabel now
                        self.instance.picture_box.setPixmap(pixmap)
        
                elif current_text == "Original" and self.instance.image_exact_path:           
                    self.instance.picture_box.setPixmap(pixmap)

def select_image_to_render(image_path, filename, pix_map_instance, qLabel, container):
    path = os.path.join(image_path, filename)
    
    # reassign variable to the ImageEditorWidget instance attribute image_exact_path
    container.image_exact_path = path
    
    pix_map_instance.load(path)
    container_width = container.width() # 1080
    container_height = container.height() # 720

    scaled_pixmap = pix_map_instance.scaled(
        (container_width - 300),
        (container_height - 100),
        Qt.KeepAspectRatio
    )

    qLabel.setPixmap(scaled_pixmap)
    