import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import * 

def signal_red():
    metin.setText('<center><font color="red">YBS</font></center>')

#pyqt Grid mantığı Dersi 10.09.2018

uyg = QApplication(sys.argv)
frame = QWidget()
izgara = QGridLayout()

metin=QLabel('<center><font color="orange">YBS</font></center>')
button_red =QPushButton("Kırmızı")

frame.connect(button_red,SIGNAL('pressed()'),signal_red)

izgara.addWidget(metin,0,1,2,1) # satır,sütun,satır genişlik,sütun genişlik
izgara.addWidget(button_red,0,2)

frame.setLayout(izgara)


frame.show()
uyg.exec_()
