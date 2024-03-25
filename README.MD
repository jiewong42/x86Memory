# x86Memory 电脑记忆
X86Memory 是一款记录你电脑操作的python程序
## 使用方法
```
pip install pygetwindow
python WindowTracker.py
```
## 当前进度
封装了一个WindowTracker类，提供了可调用的方法，可以获取当前窗口的名字，并存到sqlite数据库中。

## 开发文档

WindowTracker.py：
``` python
tracker = WindowTracker('window_tracking.db')  //初始化类
tracker.create_table() //创建数据库
tracker.track_window_activity() //追踪窗口
```
ScreenCapturer.py:
``` python
capturer = ScreenCapturer()  //初始化类
capturer.capture_screen() //截图
```
