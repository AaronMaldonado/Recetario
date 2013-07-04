# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui

class Ui_Ventana(object):

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(490, 400)
        
        self.table_categoria= QtGui.QTableView(Window)
        self.table_categoria.setGeometry(QtCore.QRect(60,80,250,300))
        self.table_categoria.setObjectName("table_producto")
        self.table_categoria.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_categoria.setAlternatingRowColors(True)
        self.table_categoria.setSortingEnabled(True)
	
	self.button1= QtGui.QPushButton(Window)
        self.button1.setGeometry(QtCore.QRect(300,40,100,25))
        self.button1.setObjectName("button1")
       
        self.search_box = QtGui.QLineEdit(Window)
        self.search_box.setGeometry(QtCore.QRect(30, 40, 200, 25))
        self.search_box.setObjectName("search_box")
	
	#self.button2 = QtGui.QPushButton(Window)
        #self.button2.setGeometry(QtCore.QRect(330,180,200,70))
        #self.button2.setObjectName("button2")
        
        
        self.label = QtGui.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(20,20,200,16))
        self.label.setObjectName("label")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Ventana", None, QtGui.QApplication.UnicodeUTF8))
        self.button1.setText(QtGui.QApplication.translate("Window", "Mostrar", None, QtGui.QApplication.UnicodeUTF8))
	#self.button2.setText(QtGui.QApplication.translate("Window", "Mostrar Categoria", None, QtGui.QApplication.UnicodeUTF8))
	self.label.setText(QtGui.QApplication.translate("Window", "Recetas", None, QtGui.QApplication.UnicodeUTF8))
	self.search_box.setPlaceholderText(QtGui.QApplication.translate("Window", "Busque recetas aquí", None, QtGui.QApplication.UnicodeUTF8))
