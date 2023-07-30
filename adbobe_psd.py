from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
from img_filt import *

right_expansion = []
work_folder = ''

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Adobe Photoshop 2077')
main_window.resize(900,600)

H = QHBoxLayout()
main_layout_v1 = QVBoxLayout()
main_layout_v2 = QVBoxLayout()
layout_h_btn = QHBoxLayout()

btn_folder = QPushButton('Папка')
list_photoes = QListWidget()
photo = QLabel('картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_rezkozt = QPushButton('Резкость')
btn_b_or_w = QPushButton('Ч/Б')

main_layout_v1.addWidget(btn_folder)
main_layout_v1.addWidget(list_photoes)

main_layout_v2.addWidget(photo)

main_layout_v2.addLayout(layout_h_btn)
layout_h_btn.setSpacing(25)
layout_h_btn.addWidget(btn_left)
layout_h_btn.addWidget(btn_right)
layout_h_btn.addWidget(btn_mirror)
layout_h_btn.addWidget(btn_rezkozt)
layout_h_btn.addWidget(btn_b_or_w)

H.addLayout(main_layout_v1)
H.addLayout(main_layout_v2)

def chooseWorkDIR():
    global work_folder
    work_folder = QFileDialog.getExistingDirectory()


def filter(files,right_expansion):
    result = []
    for file in files:
        for re in right_expansion:
            if file.endswith(re):
                result.append(file)
            else:
                pass        
    return result

def showFilesName():
    right_expansion = ['.png','.jpeg','.jpg','.svg','.gif','.psd']
    chooseWorkDIR()
    files = filter(os.listdir(work_folder),right_expansion)
    list_photoes.clear()
    for file in files:
        list_photoes.addItem(file)

class Image():
    def __init__(self,name,image):
        self.name = name 
        self.image = image
    def loadimage(self,filename):
        self.filename = filename
        img = os.path.join(work_folder,filename)
        self.image = Image.open(img)
    def showImage(self,path):
        photo.hide()
        
        photo.show()

btn_folder.clicked.connect(showFilesName)
main_window.setLayout(H)
main_window.show()
app.exec_()