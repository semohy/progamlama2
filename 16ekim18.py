from PyQt4.QtGui import *
from PyQt4.QtCore import *

class maliyetHesaplama(QDialog):
    def __init__(self,parent=None):
        super(maliyetHesaplama,self).__init__(parent) # super fonk. python için diğer fonk. peşpeşe çalışmasını sağlar....

        izgara = QGridLayout()

        line1_t=QLabel('Sabit maliyet')
        line2_t=QLabel('Değişken maliyet')
        line3_t=QLabel('Yatırımın Ekonomik Ömrü')
        line4_t=QLabel('Toplam Gelir')
        durumKriter_t = QLabel("Karlılık Kriteri")
        self.line42_t=QLabel('0 Tl') #gelir tl
        line5_t=QLabel('Durum')
        self.line52_t=QLabel('?') # rapor

        self.sm = QLineEdit()
        self.dm = QLineEdit()
        self.durumKriter_e = QLineEdit()

        self.durumKriter_e.setText("20000")

        self.yeo =QSpinBox()
        self.yeo.setRange(1,10)
        self.yeo.setValue(1)

        self.button = QPushButton("Hesapla")
        
       
        

        izgara.addWidget(line1_t, 0, 0) # satır,sütun,satır genişlik,sütun genişlik
        izgara.addWidget(self.sm, 0, 1)
        izgara.addWidget(line2_t, 1, 0)
        izgara.addWidget(self.dm, 1, 1)
        izgara.addWidget(line3_t, 2, 0)
        izgara.addWidget(self.yeo, 2, 1)
        izgara.addWidget(line4_t, 3, 0)
        izgara.addWidget(self.line42_t, 3, 1)
        
        izgara.addWidget(durumKriter_t, 4, 0)
        izgara.addWidget(self.durumKriter_e, 4, 1)
        
        izgara.addWidget(line5_t, 5, 0)
        izgara.addWidget(self.line52_t, 5, 1)
        izgara.addWidget(self.button, 6, 1)

        self.setLayout(izgara)
        self.setWindowTitle("Maliyet Hesaplama")
        self.resize(250,150)

        self.signals() #connectler buraya aktardım

    def signals(self):
        QDialog.connect(self.button,SIGNAL('pressed()'),self.hesapla)
        
    def hesapla(self):
        toplamGelir = float(self.sm.text()) + ( float(self.dm.text()) * int(self.yeo.text()) )
        self.line42_t.setText('<font color="blue"><b>'+str(toplamGelir)+' TL</b></font>')

        if (toplamGelir > float(self.durumKriter_e.text())):
            self.line52_t.setText('<font color="blue"><b>Karlı</b></font>')
        else:
            self.line52_t.setText('<font color="red"><b>Zarar</b></font>')
        

uyg = QApplication([])                          
frame = maliyetHesaplama()
frame.show()
uyg.exec_()
