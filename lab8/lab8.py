import sys
import datetime

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi


t2000 = datetime.datetime(2000,1,1)

def since_2000(t_now):
	delta = (t_now - t2000).total_seconds()
	seconds = int(delta % 60)
	minutes = int((delta // 60) % 60)
	hours = int((delta // 3600) % 24)
	days = int(delta // (3600*24))

	return {"seconds": seconds, "minutes": minutes, "hours": hours, "days": days }


class Window(QMainWindow):
	def fill_in(self):
		t_now = datetime.datetime.now()
		result = since_2000(t_now)
		self.le_cts.setText(t_now.strftime("%m/%d/%Y %H:%M:%S"))
		self.le_s.setText(str(result["seconds"]))
		self.le_m.setText(str(result["minutes"]))
		self.le_h.setText(str(result["hours"]))
		self.le_d.setText(str(result["days"]))

	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('mainwindow.ui',self)
		self.fill_in()

	@pyqtSlot()
	def on_btn_run_clicked(self):
		print("btn_run_clicked!")
		self.fill_in()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())