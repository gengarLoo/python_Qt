# python 图形界面开发

> PySide2、PyQt5 都是基于著名的 Qt 库。
> Qt库里面有非常强大的图形界面开发库，但是Qt库是C++语言开发的，PySide2、PyQt5可以让我们通过Python语言使用Qt。
>但是 PySide2、PyQt5 这两者有什么区别呢？
>可以形象地这样说： PySide2 是Qt的 亲儿子 ， PyQt5 是Qt还没有亲儿子之前的收的 义子 （Riverbank Computing这个公司开发的）。
>那为什么 PyQt5 这个义子 反而比 PySide2 这个亲儿子更出名呢？
>原因很简单：PySide2 这亲儿子最近（2018年7月）才出生。
>但是亲儿子毕竟是亲儿子，Qt准备大力培养，PySide2 或许更有前途。
>已经在使用 PyQt5 的朋友不要皱眉， 两个库的使用 对程序员来说，差别很小：它们的调用接口几乎一模一样。
>如果你的程序是PyQt5开发的，通常只要略作修改，比如把导入的名字从 PyQt5 换成 PySide2 就行了。反之亦然

### 安装PyQt5

```python
pip install pyqt5
```

这边还要安装pyqt5-tools

```python
pip install pyqt5-tools
```

### 安装PySide2

```python
pip install pyside2
```

### 国内镜像

```python
pip install pyside2 -i https://pypi.douban.com/simple/
```

这边可以直接把本地获取python的源直接改为国内镜像

```python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

一些国内镜像:
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：https://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/ 
豆瓣：http://pypi.douban.com/simple/
```