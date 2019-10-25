from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time
import csv
import datetime
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md

# 继承QThread
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = QtCore.pyqtSignal(str)
    def __init__(self,ip,path):
        super(Runthread, self).__init__()
        self.ip = ip
        self.path = path
    def __del__(self):
        self.wait()

    def run(self):
        # self.statusBar.showMessage('test')
        print('启动线程：'+self.ip)
        self.heart_status(self.ip,self.path)
        # self._signal.emit('数据采集正在执行中！')  # 注意这里与_signal = pyqtSignal(str)中的类型相同

    def heart_status(self,ip_post,path):
        # 远程连接到slave端（从）
        ip = ip_post
        port = 502
        master = mt.TcpMaster(ip, port)
        master.set_timeout(5.0)
        yuanzu1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        yuanzu2= yuanzu1
        # status = master.execute(slave=1, function_code=2, starting_address=10200, quantity_of_x=24)
        # status_last = status
        # 获取想要的寄存器的数据
        while True:
            try:
                i = 0
                status = master.execute(slave=1, function_code=2, starting_address=10200, quantity_of_x=24)
                if yuanzu2 == status:
                        print("相同数据，无变化,IP:",ip)
                        print("status==", status)
                else:
                    if status != yuanzu1 :
                        print("不相同数据，有变化且不是全0,IP:",ip)
                        print("status==", status)
                        print(type(status))
                        for num_none1 in status:
                            i = i + 1
                            if num_none1 == 1 :
                                print("i=",i)
                                self.write_excel(ip,i,path)
                yuanzu2 = status
                time.sleep(0.5)
            except:
                if ip == '10.1.1.10' :
                    self._signal.emit('一号采集器正在尝试重新启动')
                else:
                    self._signal.emit('二号采集器正在尝试重新启动')
    def write_excel(self,ip,i,path):
        now_time = datetime.datetime.now()
        today = str(datetime.datetime.today())[0:10]+'.csv'#按照今天日期进行文件命名
        today = "D:\\" + path + today
        print(today)
        with open('saigui.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
            saigui_chicun = ("".join(rows[i-1]))
            print(saigui_chicun)
        if ip == "10.1.1.11" :
            i = i + 24
            input_saigui_num = "采集的是"+str(i)+"号塞规！"
            input_saigui_chicun = "塞规尺寸是："+("".join(rows[i-1]))
            input_saigui_nowtime = "采集时间是："+str(now_time)[0:19]
            data = [input_saigui_num,input_saigui_chicun,input_saigui_nowtime]
        else :
            input_saigui_num = "采集的是" + str(i) + "号塞规！"
            input_saigui_chicun = "塞规尺寸是：" + ("".join(rows[i - 1]))
            input_saigui_nowtime = "采集时间是：" + str(now_time)[0:19]
            data = [input_saigui_num, input_saigui_chicun, input_saigui_nowtime]
        with open(today,mode='a',newline='') as file1:
            writer= csv.writer(file1)
            writer.writerow(data)
        self._signal.emit(str(data))