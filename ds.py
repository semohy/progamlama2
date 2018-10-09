import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#pyqt Grid mantığı Dersi 2 10.09.2018

uyg = QApplication(sys.argv)
frame = QWidget()
izgara = QGridLayout()

line1_l = QLabel("Gidilen Yol")
line1_e = QLineEdit()

line2_l = QLabel("Yakıt Lt")
line2_e = QLineEdit()

line3_l = QLabel("100km Tüketim")
line3_e = QLineEdit()

line4_l = QLabel("Topla Tutar")
line4_r = QLabel("0.00")

line5 = QPushButton("Hesapla")

izgara.addWidget(line1_l,0,0)
izgara.addWidget(line1_e,0,1)

izgara.addWidget(line2_l,1,0)
izgara.addWidget(line2_e,1,1)

izgara.addWidget(line3_l,2,0)
izgara.addWidget(line3_e,2,1)

izgara.addWidget(line4_l,3,0)
izgara.addWidget(line4_r,3,1)

izgara.addWidget(line5,4,0,2,3)

frame.setLayout(izgara)


frame.show()
uyg.exec_()
