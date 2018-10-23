from PyQt4.QtGui import *
from PyQt4.QtCore import*

class ornekTablo(QDialog):
    def __init__(self,parent=None):
        super(ornekTablo,self).__init__(parent)

        #Grid olustur
        grid=QGridLayout()

        #tablo Oluşturma

        self.tablo=QTableWidget()
        self.tablo.resize(400,250)
        self.tabloRowSize = 0
        self.tabloColSize = 0
        self.tablo.setRowCount(self.tabloRowSize)
        self.tablo.setColumnCount(self.tabloColSize)

        grid.addWidget(self.tablo)

        #tabloya int veri ekleme
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, 1500)
        self.tablo.setItem(0, 0,QTableWidgetItem(item))

    


class tabloListeOrnegi(QDialog):
    def __init__(self,parent=None):
        super(tabloListeOrnegi,self).__init__(parent)

        diyalog = ornekTablo()

        data={'col':['1','2','3'],'col2':['4','5','6'],'col3':['7','8','9']}
        
        diyalog.tabloRowSize = len(data)

        for x in data:
            columSize = len(data[x])
        
        diyalog.tabloColSize = len(data)

        
        
       
app =  QApplication([])
frame= tabloListeOrnegi()
frame.show()
app.exec_
