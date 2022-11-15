# 控件学习

---

## 按钮

###### 按钮点击

```python
button.clicked.connect(handleCalc)

def handleCalc:
  ...
```

###### 改变文本

```python
# 改变按钮的文本
button.setText(text)
```

###### 启用 | 禁用 按钮

```python
button.setEnabled(true | false)
```

###### 设置按钮图标

```python
from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon

# 设置图标
button.setIcon("xxx.png")

# 设置图标大小
button.setIconSize(QSize(xx,xx))
```

## 单行文本框
