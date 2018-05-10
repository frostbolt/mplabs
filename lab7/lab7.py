import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

def y(a,b,c):
	return (2+(2+(2+(2+a)**1/2)**1/2)**1/2)**1/2+math.sin((13-b)/c**5)

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('mainwindow.ui',self)
		self.le_1.setText("1")
		self.le_2.setText("2")
		self.le_3.setText("3")
		self.le_4.setText("4")
		self.le_5.setText("5")

	@pyqtSlot()
	def on_btn_run_clicked(self):
		print("btn_run_clicked!")
		self.te_o.setText(self.le_1.text()+self.le_2.text()+self.le_3.text()+self.le_4.text()+self.le_5.text())


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())