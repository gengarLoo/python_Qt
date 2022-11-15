
# 开发第一个基于PyQt5的桌面应用

> 必须使用两个类: QApplication 和 QWidget。都在PyQt5.QtWidgets。

## QtDesinger

> 扩展
> settings>Tools>External Tools

![](https://gitee.com/zhang-wangbin/iamge/raw/master/test/202211041400646.png)

## 将.ui文件转换为.py文件

> 法一：python命令行
> python -m PyQt5.uic.pyuic demo.ui -o demo.py
>
> 法二: pyuic 扩展
> settings>Tools>External Tools

```text
$FileName$ -o $FileNameWithoutExtension$.py -x
```

![](https://gitee.com/zhang-wangbin/iamge/raw/master/test/202211041400328.png)
