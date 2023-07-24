from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Adobe Photoshop 2077')
main_window.resize(700,400)

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


main_window.setLayout(H)
main_window.show()
app.exec_()