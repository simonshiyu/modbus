import modbus_ui_inherit_process
import sys

if __name__ == "__main__":
    app = modbus_ui_inherit_process.QtWidgets.QApplication(sys.argv)
    mainWindow = modbus_ui_inherit_process.QtWidgets.QMainWindow()
    modbus_ui_inherit_process.mywindow(mainWindow)
    sys.exit(app.exec_())