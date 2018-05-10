import sys
import math

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
		self.le_a.setText("2")
		self.le_b.setText("13")
		self.le_c.setText("0.8")

	@pyqtSlot()
	def on_btn_run_clicked(self):
		print("btn_lab3_clicked!")
		self.le_y.setText("{0:.12f}".format(y(float(self.le_a.text()),float(self.le_b.text()),float(self.le_c.text()))))


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())