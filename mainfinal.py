#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controllerfinal
from ventanafinal import Ui_Ventanafinal


class mainfinal(QtGui.QWidget):
	
	def __init__(self):
		super(mainfinal, self).__init__()
		self.ui = Ui_Ventanafinal()
		self.ui.setupUi(self)
		self.cargar_receta()
		self.cargar_nombre()
		self.cargar_preparacion()
		#self.set_signal()
		self.show()	
		nombre2="imagen1.jpeg"
		filename = "./" + nombre2
        	image = QtGui.QImage(filename)
        	pp = QtGui.QPixmap.fromImage(image)
        	self.ui.label.setPixmap(pp)
		
		
	def cargar_receta(self,ingredientes=None):
		
		if ingredientes is None:
			ingredientes = controllerfinal.get_ingredientes()
         
        	for ingrediente in ingredientes:
			   ingredientes[0]
		lista = str(ingrediente[0])
		#casa = lista.split(',')
		self.ui.TextEdit2.setText(lista)
		
	def cargar_nombre(self,nombre=None):
		
		if nombre is None:
			 nombre = controllerfinal.get_nombre() 
			 
		self.model = QtGui.QStandardItemModel(1,1)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
		r=0
		
		for row in nombre:
			 index=self.model.index(r,0,QtCore.QModelIndex())
			 self.model.setData(index,row['Nombre'])
			 r=r+1			
		self.ui.table_categoria2.setModel(self.model)	
		self.ui.table_categoria2.setColumnWidth(0,250)
	def set_signal(self):
		m=self.ui.TextEdit1.setReadOnly(True)
		self.ui.button1.clicked.connect(m)

	def cargar_preparacion(self, preparacion=None):
		if preparacion is None:
			preparacion=controllerfinal.get_preparacion()
			for i in preparacion:
				i[0]
		lista = str(i[0])
				
		self.ui.TextEdit1.setText(lista) 

		 
def run():
    app = QtGui.QApplication(sys.argv)
    ma = mainfinal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
