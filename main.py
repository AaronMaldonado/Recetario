#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
from ventanaprincipal import Ui_Ventana

class main(QtGui.QWidget):

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_Ventana()
        self.ui.setupUi(self)
        self.cargar_categoria()
	self.show()
  
    def cargar_categoria(self):
  
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(10,2)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Categoria"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Cantidad"))


        self.ui.table_categoria.setModel(self.model)

        self.ui.table_categoria.setColumnWidth(0,148)
        self.ui.table_categoria.setColumnWidth(1,110)
       

  
	
def run():
    app = QtGui.QApplication(sys.argv)
    ma = main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
