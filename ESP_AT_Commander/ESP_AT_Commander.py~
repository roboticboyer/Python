#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore, uic
import serial
import time

#---Form Principale----------------------------------------------------
class Principale(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui =uic.loadUi('py_ESP_AT_Commander_01.ui', self) #Carica form.
		#Posizione e dimensione della finestra.
		#self.ui.setGeometry(200, 200, 800, 800)#pos O,V dim O,V
		
		#Lista Comandi AT
		ComandiAT=[
		"AT",
		"AT+RST",
		"AT+GMR",
		"AT+CWMODE?",
		"AT+CWMODE=1",
		"AT+CWMODE=3",
		"AT+CIOBAUD?",
		"AT+GMR",
		"AT+CHELLO",
		"AT+CWQAP",
		"AT+CWLAP",
		"AT+CWJAP=\"Network\",\"Password\"",
		"AT+CWJAP?",
		"AT+CIFSR",
		"AT+CIFSR=?",
		"AT+CIPSTATUS",
		"AT+CIPSTART=4,\"TCP\",\"www.google.com\",80",
		"AT+CIPSEND=4,50",
		"AT+CIPMUX=1",
		"AT+CIPSERVER=1,8080",
		"AT+CIPSEND=0,13",
		"Prova Testo",
		"AT+CIPSERVER=0,8080",
		"AT+CIPCLOSE"]
		
		for i in ComandiAT: 
			self.ui.LW_ATcom.addItem(i)
		
		#definizione segnali interfaccia
		self.connect(self.ui.B_quit, QtCore.SIGNAL("clicked()"),fine_sessione)
		self.connect(self.ui.B_con, QtCore.SIGNAL("clicked()"),Connessione_on)
		self.connect(self.ui.B_nocon, QtCore.SIGNAL("clicked()"),Connessione_off)
		self.connect(self.ui.B_Send, QtCore.SIGNAL("clicked()"),Inv_text)
		self.connect(self.ui.B_Atsend, QtCore.SIGNAL("clicked()"),Inv_send)
		self.connect(self.ui.LW_ATcom, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),Inv_at)
		# Pulsanti
		#self.connect(self.ui.B_at1, QtCore.SIGNAL("clicked()"),Inv_at1)
		#self.connect(self.ui.B_at2, QtCore.SIGNAL("clicked()"),Inv_at2)
		#Timer Echo 
		self.timer = QtCore.QTimer()
		QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), Legge_ESP)
		self.timer.start(500)

#---Legge da Arduino-----------------------------------------
def Legge_ESP():
	#da completare
	global con_status
	if con_status == 1:
		#print("Echo on")
		#app.processEvents()
		if conn.inWaiting() > 1:
			ret = conn.readline().strip( "\r\n" )
			#print ret
			if len(ret) > 1:
				#ret_ascii = ret.encode('ascii',errors='ignore')
				#window_a.ui.T_ser.append(ret_ascii)
				app.processEvents()
				window_a.ui.T_ser.append(ret)


#---Attiva Connessione---------------------------------------
def Connessione_on():
	# Apre connesione seriale con ESP
	global conn
	global con_status
	items = ("/dev/ttyUSB0","/dev/ttyUSB0","/dev/ttyACM0","/dev/ttyACM1")
	A_ser_port, ok = QtGui.QInputDialog.getItem(window_a, "QInputDialog.getItem()","USB Port:", items, 0, False)
	#print A_ser_port
	try:
		#A_ser_port="/dev/ttyUSB0"
		A_ser_vel="9600"
		conn=serial.Serial(str(A_ser_port), A_ser_vel,timeout=0.1, rtscts=False)
		window_a.ui.T_note.setText("Connessione con ESP avvenuta")
		con_status=1
		window_a.ui.B_con.hide()
		window_a.ui.B_nocon.show()
		
	except serial.serialutil.SerialException:
		window_a.ui.T_note.setText("Controllare la connessione con ESP")
	time.sleep(2)

#---Chiude connessione---------------------------------------
def Connessione_off():
	global con_status
	#print con_status
	if con_status == 1:
		conn.close()
		con_status=0
	window_a.ui.T_note.setText("Connessione Off")
	window_a.ui.B_con.show()
	window_a.ui.B_nocon.hide()
	#window_a.ui.B_legge.hide()
#---Fine lavoro, chiude tutto------------------------------------------
def fine_sessione():
	if con_status == 1:
		conn.close()
	quit()
#---Comando AT------------------------------------------
def Inv_at1():
	if con_status == 1:
		sCmd="AT"
		conn.write( sCmd + "\r\n")
#---Comando AT+RST------------------------------------------
def Inv_at2():
	if con_status == 1:
		sCmd="AT+RST"
		conn.write( sCmd + "\r\n")
#---Invia Text------------------------------------------
def Inv_text():
	sCmd=window_a.ui.TE_command.toPlainText()
	window_a.ui.T_note.setText(sCmd)
	if con_status == 1:
		conn.write( str(sCmd) + "\r\n")
#---Invia Text------------------------------------------
def Inv_send():
	sCmd=window_a.ui.TE_command.toPlainText()
	#window_a.ui.T_note.setText(sCmd)
	num=window_a.ui.SB_id.value()
	#print num
	sCmd1="AT+SEND=" + str(num) + "," + str(len(sCmd))
	window_a.ui.T_note.setText(sCmd1)
	if con_status == 1:
		conn.write( sCmd1 + "\r\n")
#---Invia Comando ------------------------------------------
def Inv_at():
	global con_status
	#txt="Prova AT"
	txt=window_a.ui.LW_ATcom.currentItem().text()
	#print txt
	window_a.ui.T_note.setText(txt)
	if con_status == 1:
		conn.write( str(txt) + "\r\n")

#---Funzione principale------------------------------------------------
if __name__ == '__main__':
	global con_status
	con_status=0
	app = QtGui.QApplication(sys.argv)
	window_a = Principale()
	window_a.show()
	window_a.ui.B_nocon.hide()
	#window_a.ui.B_legge.hide()
	sys.exit(app.exec_())
