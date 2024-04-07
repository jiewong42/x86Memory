# x86Memory 电脑记忆
X86Memory 是一款记录你电脑操作的python程序  

X86Memory是一款参考了[rewind](https://www.rewind.ai/)、[Memento](https://github.com/apirrone/Memento)、[Windrecorder](https://github.com/yuka-friends/Windrecorder)的软件。

## 工作原理:
- 该应用程序每 2 秒截取一次屏幕截图
- 它将屏幕截图编译成 h264 视频片段以提高存储效率
- 它使用 OCR 从图像中提取文本
- 它索引 sqlite3 数据库和 vectordb 中的文本
- 它使用 FTS5 搜索文本
- 它使用 LLM（通过 OpenAI 的 API 的 GPT）与时间线聊天

## 当前进度
正处于 MVP 构造阶段
2023.3.26:新增 WindowTracker2 类，只有在窗口标题发生变化时，才会向数据库写入新的记录。  
2023.3.25:封装了一个 ScreenCapturer 类，提供了调用的方法，可以截屏，并保存到文件夹中。  
2023.3.25:封装了一个 WindowTracker 类，提供了可调用的方法，可以获取当前窗口的名字，并存到sqlite数据库中。

## 使用方法
```
pip install pygetwindow
pip install mss
```

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
