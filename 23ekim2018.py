from PyQt4.QtGui import *
from PyQt4.QtCore import*

class butunlesik(QDialog):
    def __init__(self,parent=None):
        super(butunlesik,self).__init__(parent)

        grid = QGridLayout()

        slider=QSlider()
        slider.setRange(0,100)
        slider.setOrientation(Qt.Horizontal)

        grid.addWidget(slider, 0, 0)

        spinbox = QSpinBox()
        spinbox.setRange(0,100)

        grid.addWidget(spinbox, 1, 0)

        self.connect(spinbox,SIGNAL('valueChanged(int)'),slider.setValue)
        self.connect(slider,SIGNAL('valueChanged(int)'),spinbox.setValue)

        self.setLayout(grid)
        self.setWindowTitle("Bütünleşik Uygulama")

app =  QApplication([])
frame= butunlesik()
frame.show()
uyg.exec__
