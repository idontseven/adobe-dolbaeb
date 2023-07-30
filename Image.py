import os
import adbobe_psd as ap
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap

class ProccesImage():
    def __init__(self,name,image):
        self.name = name 
        self.image = image
    def loadimage(self,filename):
        self.filename = filename
        img = os.path.join(ap.work_folder,filename)
        self.image = Image.open(img)
    def showImage(self,path):
        ap.photo.hide()
        pixmapimage = QPixmap(path)
        
        ap.photo.show()