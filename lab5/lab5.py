import time
import numpy as np
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

def f(n):
	return 1./((2*n-1)**2)

def lab3(eps):
	start_time = time.time()
	n, f_prev, f_curr, my_pi = 1, f(1), 0, 0
	while True:
		n += 1
		my_pi += f_prev
		f_curr = f(n)
		if (f_prev - f_curr <= eps): break
		f_prev = f_curr

	return {"pi": (my_pi*8)**.5, "num_iter": n, "time": time.time() - start_time}

def lab4(n):
	result = " "
	X = np.random.rand(n)
	result += "Массив случайных чисел:\n{}\n".format(X)
	X_max, X_min = np.max(X), np.min(X)
	result += "X_max: ~{0:.4f},\tX_min: ~{0:.4f}\n".format(X_max, X_min)
	result += "Итоговый массив:\n {}".format( X / (X_max - X_min))
	return result

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('mainwindow.ui',self)
		self.le_eps.setText("1e-18")
		self.le_lab4.setText("6")

	@pyqtSlot()
	def on_btn_lab3_clicked(self):
		print("btn_lab3_clicked!")
		result = lab3(float(self.le_eps.text()))
		self.le_pi.setText("{0:.12f}".format(result["pi"]))
		self.le_numiter.setText("{}".format(result["num_iter"]))
		self.le_time.setText("{0:.12f}".format(result["time"]))

	@pyqtSlot()
	def on_btn_lab4_clicked(self):
		print("btn_lab4_clicked!")
		self.te_lab4.setText(lab4(int(self.le_lab4.text())))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())