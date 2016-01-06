#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore, uic
import serial
SERIALPORT =  '/dev/ttyACM0'

class MyWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui =uic.loadUi('carica_link_00.ui', self)
		self.ui.show()
		self.connect(self.ui.B_file, QtCore.SIGNAL("clicked()"), creahtml)
		self.connect(self.ui.B_quit, QtCore.SIGNAL("clicked()"), quit_gui)

def creahtml():
	#Apre file txt
	path = QtGui.QFileDialog.getOpenFileName(window.ui, 'Scegli un file link','.',"TXT (*.txt)")
	window.ui.T_file.setText(path)
	file=open(path, 'r')
	#Test
	path_no_ext=path[:-3]
	#window.ui.T_log.appendPlainText(path_no_ext)
	path_htm=path_no_ext+"htm"
	# Apre file htm
	fow = open(path_htm, "wb")
	fow.write("<HTML>\n<HEAD><TITLE>ELENCO SITI</TITLE></HEAD>\n<BODY>\n")
	fow.write("<H1 ALIGN=CENTER><P><B>Elenco siti</B></H1><H3 ALIGN=LEFT><P>\n")
	for line in file.xreadlines():
		http_find=line.find('http')
		google_find=line.find('google')
		uguale_find=line.find('=')
		num_caratteri=len(line)
		#window.ui.T_log.appendPlainText(str(google_find))
		if http_find == 0 :
			fow.write("<A target=\"_blank\" HREF=\"")
			fow.write(line)
			fow.write("\">")
			if google_find > 0 :
				fow.write("Google link")
			elif num_caratteri > 100 :
				fow.write(line[:90] + " --- link")
			else :
				window.ui.T_log.appendPlainText("Trovato link " + line)
				fow.write(line)
			fow.write("</A><P>\n")
		elif uguale_find == 0:
			fow.write("<hr>")
		else :
			fow.write(line)
			fow.write("<P>\n")
	# Close opend files
	file.close()
	fow.write("</BODY>\n</HTML>\n")
	fow.close()
	window.ui.T_log.appendPlainText("\nFile convertito\n")



def quit_gui():
	quit()

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	window.move(200, 200)
	sys.exit(app.exec_())
