# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui

class Ui_Ventanafinal(object):

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(600, 450)
        

	self.table_categoria2= QtGui.QTableView(Window)
        self.table_categoria2.setGeometry(QtCore.QRect(30,15,250,50))
        self.table_categoria2.setObjectName("table_producto2")
        self.table_categoria2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_categoria2.setAlternatingRowColors(True)
        self.table_categoria2.setSortingEnabled(True)
	
	self.TextEdit1 = QtGui.QTextEdit(Window)
        self.TextEdit1.setGeometry(QtCore.QRect(30,240,300,150))
        self.TextEdit1.setReadOnly(True)
	self.TextEdit2 = QtGui.QTextEdit(Window)
        self.TextEdit2.setGeometry(QtCore.QRect(30,110,300,100))
        self.TextEdit2.setReadOnly(True)
             
	self.button1= QtGui.QPushButton(Window)
        self.button1.setGeometry(QtCore.QRect(400,250,60,50))
        self.button1.setObjectName("button1")
        
	self.label = QtGui.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(350,0,300,300))
        self.label.setObjectName("label")
	
	self.button2 = QtGui.QPushButton(Window)
        self.button2.setGeometry(QtCore.QRect(400,300,60,50))
        self.button2.setObjectName("button2")
        
	self.label2 = QtGui.QLabel(Window)
	self.label2.setGeometry(QtCore.QRect(30,90,200,16))
	self.label2.setObjectName("label2")

	self.label3 = QtGui.QLabel(Window)
	self.label3.setGeometry(QtCore.QRect(30,220,200,16))
	self.label3.setObjectName("label3")
     
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Receta", None, QtGui.QApplication.UnicodeUTF8))
	self.button2.setText(QtGui.QApplication.translate("Window", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
	self.button1.setText(QtGui.QApplication.translate("Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Window", "Ingredientes: ", None, QtGui.QApplication.UnicodeUTF8))
	self.label3.setText(QtGui.QApplication.translate("Window", "Preparación: ", None, QtGui.QApplication.UnicodeUTF8))
