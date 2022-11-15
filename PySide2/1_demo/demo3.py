from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import os,sys
# os.chdir(sys.path[0])


# 创建一个类
class MainWindow:
    def __init__(self):
        # 注意这里如果UI文件直接在根目录，使用'testUI.ui'
        self.ui = QUiLoader().load("./ui/stats.ui")

        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textedit.toPlainText()
        
        QMessageBox.about(self.ui,"info",info)

if __name__ == "__main__":
    app = QApplication([])
    # 实例化窗口
    mainwindow = MainWindow()
    mainwindow.ui.show()
    app.exec_()