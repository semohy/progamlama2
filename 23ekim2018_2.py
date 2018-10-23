from PyQt4.QtGui import *
from PyQt4.QtCore import*

class yaziTipiDlg(QDialog):
    def __init__(self,parent=None):
        super(yaziTipiDlg,self).__init__(parent)

        #Grid olustur
        grid=QGridLayout()

        grid.addWidget(QLabel("Yazı Tipi"), 0, 0)

        self.yaziTipiListe=QComboBox()
        self.yaziTipiListe.addItems(['Arial','Verdana','Comic Sans'])

        grid.addWidget(self.yaziTipiListe, 0, 1)

        button_ok = QPushButton("Tamam")
        button_cancel = QPushButton("Vazgeç")

        button_box = QHBoxLayout()

        button_box.addWidget(button_ok)
        button_box.addWidget(button_cancel)

        self.connect(button_ok,SIGNAL('pressed()'),self.accept)
        self.connect(button_cancel,SIGNAL('pressed()'),self.reject)

        grid.addLayout(button_box,1,0,1,2)

        self.setLayout(grid)
        self.setWindowTitle("Yazı Tipi Değiştir")

class yaziTipi(QDialog):
    def __init__(self,parent=None):
        super(yaziTipi,self).__init__(parent)

        self.yaziTipi = 'Verdana'
        self.metin='<font face="%s" size="+3">Merhaba Cerennn</font>'
        self.etiket = QLabel(self.metin%self.yaziTipi)

        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)

        ytDugme = QPushButton('Yazı Tipini Değiştir')

        kutu.addWidget(ytDugme)

        self.connect(ytDugme,SIGNAL('pressed()'),self.yaziTipi_cmd)

        self.setLayout(kutu)

        self.setWindowTitle("Yazı Tİpi Dialog Penceresi")

    def yaziTipi_cmd(self):
        diyalog = yaziTipiDlg()
        yaziTipiIndex = diyalog.yaziTipiListe.findText(self.yaziTipi)
        diyalog.yaziTipiListe.setCurrentIndex(yaziTipiIndex)

        if diyalog.exec_():
            self.yaziTipi = diyalog.yaziTipiListe.currentText()
            self.etiket.setText(self.metin%self.yaziTipi)
        
app =  QApplication([])
frame= yaziTipi()
frame.show()
app.exec_
