import sys, os,csv
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from modbus_ui import Ui_mainWindow
import modbus_qt_process
import time

class mywindow(QtWidgets.QMainWindow,Ui_mainWindow):
    str_pass_signal = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(mywindow,self).__init__(parent)
        self.setupUi(self)
        self.input_lineEdit()
        self.show()
        # self.pushButton.clicked.connect(self.pushbutton_clicked)
        # self.str_pass_signal.connect(self.pass_signal)
        # self.textBrowser.append('zijixiede')
        self.pushButton_2.clicked.connect(self.lineEdit_save_into_csv)
        self.pushButton_3.clicked.connect(self.start_run)
        self.pushButton_3.clicked.connect(self.lineEdit_disable)
    def lineEdit_disable(self):
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)

    def input_lineEdit(self):
        self.lineEdit_1.setText(self.int_lineEdit(1))
        self.lineEdit_2.setText(self.int_lineEdit(2))
        self.lineEdit_3.setText(self.int_lineEdit(3))
        self.lineEdit_4.setText(self.int_lineEdit(4))
        self.lineEdit_5.setText(self.int_lineEdit(5))
        self.lineEdit_6.setText(self.int_lineEdit(6))
        self.lineEdit_7.setText(self.int_lineEdit(7))
        self.lineEdit_8.setText(self.int_lineEdit(8))
        self.lineEdit_9.setText(self.int_lineEdit(9))
        self.lineEdit_10.setText(self.int_lineEdit(10))
        self.lineEdit_11.setText(self.int_lineEdit(11))
        self.lineEdit_12.setText(self.int_lineEdit(12))
        self.lineEdit_13.setText(self.int_lineEdit(13))
        self.lineEdit_14.setText(self.int_lineEdit(14))
        self.lineEdit_15.setText(self.int_lineEdit(15))
        self.lineEdit_16.setText(self.int_lineEdit(16))
        self.lineEdit_17.setText(self.int_lineEdit(17))
        self.lineEdit_18.setText(self.int_lineEdit(18))
        self.lineEdit_19.setText(self.int_lineEdit(19))
        self.lineEdit_20.setText(self.int_lineEdit(20))
        self.lineEdit_21.setText(self.int_lineEdit(21))
        self.lineEdit_22.setText(self.int_lineEdit(22))
        self.lineEdit_23.setText(self.int_lineEdit(23))
        self.lineEdit_24.setText(self.int_lineEdit(24))
        self.lineEdit_25.setText(self.int_lineEdit(25))
        self.lineEdit_26.setText(self.int_lineEdit(26))
        self.lineEdit_27.setText(self.int_lineEdit(27))
        self.lineEdit_28.setText(self.int_lineEdit(28))
        self.lineEdit_29.setText(self.int_lineEdit(29))
        self.lineEdit_30.setText(self.int_lineEdit(30))
        self.lineEdit_31.setText(self.int_lineEdit(31))
        self.lineEdit_32.setText(self.int_lineEdit(32))
        self.lineEdit_33.setText(self.int_lineEdit(33))
        self.lineEdit_34.setText(self.int_lineEdit(34))
        self.lineEdit_35.setText(self.int_lineEdit(35))
        self.lineEdit_36.setText(self.int_lineEdit(36))
        self.lineEdit_37.setText(self.int_lineEdit(37))
        self.lineEdit_38.setText(self.int_lineEdit(38))
        self.lineEdit_39.setText(self.int_lineEdit(39))
        self.lineEdit_40.setText(self.int_lineEdit(40))
        self.lineEdit_41.setText(self.int_lineEdit(41))
        self.lineEdit_42.setText(self.int_lineEdit(42))
        self.lineEdit_43.setText(self.int_lineEdit(43))
        self.lineEdit_44.setText(self.int_lineEdit(44))
        self.lineEdit_45.setText(self.int_lineEdit(45))
        self.lineEdit_46.setText(self.int_lineEdit(46))
        self.lineEdit_47.setText(self.int_lineEdit(47))
        self.lineEdit_48.setText(self.int_lineEdit(48))
    def int_lineEdit(self,i):
        # import csv
        with open('saigui.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
        return " ".join(rows[i - 1])

    def pushbutton_clicked(self,data):
        print(data)
        # self.textBrowser.append('test')
        self.str_pass_signal.emit(data)

    def pass_signal(self,i):
        self.textBrowser.append(i)

    def lineEdit_save_into_csv(self):
        with open('saigui.csv','w',newline='') as csvfile:
            text1 = [float(self.lineEdit_1.text())]
            text2 = [float(self.lineEdit_2.text())]
            text3 = [float(self.lineEdit_3.text())]
            text4 = [float(self.lineEdit_4.text())]
            text5 = [float(self.lineEdit_5.text())]
            text6 = [float(self.lineEdit_6.text())]
            text7 = [float(self.lineEdit_7.text())]
            text8 = [float(self.lineEdit_8.text())]
            text9 = [float(self.lineEdit_9.text())]
            text10 = [float(self.lineEdit_10.text())]
            text11 = [float(self.lineEdit_11.text())]
            text12 = [float(self.lineEdit_12.text())]
            text13 = [float(self.lineEdit_13.text())]
            text14 = [float(self.lineEdit_14.text())]
            text15 = [float(self.lineEdit_15.text())]
            text16 = [float(self.lineEdit_16.text())]
            text17 = [float(self.lineEdit_17.text())]
            text18 = [float(self.lineEdit_18.text())]
            text19 = [float(self.lineEdit_19.text())]
            text20 = [float(self.lineEdit_20.text())]
            text21 = [float(self.lineEdit_21.text())]
            text22 = [float(self.lineEdit_22.text())]
            text23 = [float(self.lineEdit_23.text())]
            text24 = [float(self.lineEdit_24.text())]
            text25 = [float(self.lineEdit_25.text())]
            text26 = [float(self.lineEdit_26.text())]
            text27 = [float(self.lineEdit_27.text())]
            text28 = [float(self.lineEdit_28.text())]
            text29 = [float(self.lineEdit_29.text())]
            text30 = [float(self.lineEdit_30.text())]
            text31 = [float(self.lineEdit_31.text())]
            text32 = [float(self.lineEdit_32.text())]
            text33 = [float(self.lineEdit_33.text())]
            text34 = [float(self.lineEdit_34.text())]
            text35 = [float(self.lineEdit_35.text())]
            text36 = [float(self.lineEdit_36.text())]
            text37 = [float(self.lineEdit_37.text())]
            text38 = [float(self.lineEdit_38.text())]
            text39 = [float(self.lineEdit_39.text())]
            text40 = [float(self.lineEdit_40.text())]
            text41 = [float(self.lineEdit_41.text())]
            text42 = [float(self.lineEdit_42.text())]
            text43 = [float(self.lineEdit_43.text())]
            text44 = [float(self.lineEdit_44.text())]
            text45 = [float(self.lineEdit_45.text())]
            text46 = [float(self.lineEdit_46.text())]
            text47 = [float(self.lineEdit_47.text())]
            text48 = [float(self.lineEdit_48.text())]
            writer = csv.writer(csvfile)
            writer.writerow(text1)
            writer.writerow(text2)
            writer.writerow(text3)
            writer.writerow(text4)
            writer.writerow(text5)
            writer.writerow(text6)
            writer.writerow(text7)
            writer.writerow(text8)
            writer.writerow(text9)
            writer.writerow(text10)
            writer.writerow(text11)
            writer.writerow(text12)
            writer.writerow(text13)
            writer.writerow(text14)
            writer.writerow(text15)
            writer.writerow(text16)
            writer.writerow(text17)
            writer.writerow(text18)
            writer.writerow(text19)
            writer.writerow(text20)
            writer.writerow(text21)
            writer.writerow(text22)
            writer.writerow(text23)
            writer.writerow(text24)
            writer.writerow(text25)
            writer.writerow(text26)
            writer.writerow(text27)
            writer.writerow(text28)
            writer.writerow(text29)
            writer.writerow(text30)
            writer.writerow(text31)
            writer.writerow(text32)
            writer.writerow(text33)
            writer.writerow(text34)
            writer.writerow(text35)
            writer.writerow(text36)
            writer.writerow(text37)
            writer.writerow(text38)
            writer.writerow(text39)
            writer.writerow(text40)
            writer.writerow(text41)
            writer.writerow(text42)
            writer.writerow(text43)
            writer.writerow(text44)
            writer.writerow(text45)
            writer.writerow(text46)
            writer.writerow(text47)
            writer.writerow(text48)
        self.textBrowser.clear()
        self.textBrowser.append("保存完毕！")
    
    def start_run(self):
        path = self.lineEdit.text()
        self.thread1 = modbus_qt_process.Runthread('10.1.1.10',path)
        self.thread2 = modbus_qt_process.Runthread('10.1.1.11',path)
        # str_signal = self.thread1._signal.connect(self.thread1.start)
        # print(str_signal)
        self.thread1.start()
        self.thread1._signal.connect(self.pass_signal)
        self.textBrowser.append("一号采集器正在运行！")
        # time.sleep(2)
        self.thread2.start()
        self.thread2._signal.connect(self.pass_signal)
        self.textBrowser.append("二号采集器正在运行！")