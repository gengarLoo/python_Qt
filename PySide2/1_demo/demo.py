from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
# PySide2.QtWidgets 控件库
# QApplication,QMainWindow,QPushButton,QPlainTextEdit都是控件基类对象QWidget的子类

def handleCalc():
    # 获取文本内容
    info = textEdit.toPlainText()
    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'
    # 对话框
    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )

if __name__ == "__main__":
    # QApplication：提供图形界面程序的底层管理功能
    # 初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…
    # QApplication要做如此重要的初始化操作，所以，我们必须在任何界面控件对象创建前，先创建它。
    app = QApplication([])

    # 要在界面上 创建一个控件 ，就需要在程序代码中 创建 这个 控件对应类 的一个 实例对象
    # 在 Qt 系统中，控件（widget）是 层层嵌套 的，除了最顶层的控件，其他的控件都有父控件。
    
    # 主窗口
    # 实例化 QMainWindow 主窗口时，却没有指定 父控件， 因为它就是最上层的控件了
    window = QMainWindow()
    # resize 设置控件的大小
    window.resize(500, 400)
    # move 设置控件(主窗口)在屏幕的显示位置
    window.move(300, 310)
    # 窗口标题
    window.setWindowTitle('薪资统计')

    # 文本框
    # QPlainTextEdit、QPushButton 实例化时，都有一个参数window
    # 指定它的父控件对象 是 window 对应的QMainWindow 主窗口。
    textEdit = QPlainTextEdit(window)
    # 提示文本
    textEdit.setPlaceholderText("请输入薪资表")
    # 设置文本框在主窗口的显示位置
    textEdit.move(10,25)
    # 设置文本框的大小
    textEdit.resize(300,350)

    # 按钮
    button = QPushButton('统计', window)
    button.move(380,80)
    button.clicked.connect(handleCalc)

    # 放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码
    window.show()

    # 最后 ，通过下面这行代码
    # 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。
    app.exec_()