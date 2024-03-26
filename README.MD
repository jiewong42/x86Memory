# x86Memory 电脑记忆
X86Memory 是一款记录你电脑操作的python程序  

X86Memory是一款参考了[rewind](https://www.rewind.ai/)、[Memento](https://github.com/apirrone/Memento)、[Windrecorder](https://github.com/yuka-friends/Windrecorder)的软件。
## 初衷与历程
在一开始，我想分析在电脑上花费的时间都用到了哪里，我试过好多软件，都不满意，遂止。  
当 rewind 出来的时候，我想体验，但它只提供了mac版本。  
2024年3月初的时候，我已经接触了[bigdl-llm](https://marketing.intel.cn/bigdl-llm)很长时间了，我又注意到 Memento ，我想为他加上本地llm的功能，但我不是很能理解这个仓库。我又看到了 Memento ，我对它的原理很喜欢，但它是在ubuntu上构建的，windows上有一些兼容问题（这些问题解决了，但我败在了openai密钥上）。我于是想参照它的功能实现一个windows版本的。  
工作原理:
- 该应用程序每 2 秒截取一次屏幕截图
- 它将屏幕截图编译成 h264 视频片段以提高存储效率
- 它使用 OCR 从图像中提取文本
- 它索引 sqlite3 数据库和 vectordb 中的文本
- 它使用 FTS5 搜索文本
- 它使用 LLM（通过 OpenAI 的 API 的 GPT）与时间线聊天

我又看见了Kevin Chen的 [拆解 Rewind 应用程序](https://kevinchen.co/blog/rewind-ai-app-teardown/)，这篇博文的分析对我帮助更大。

我历经了几天时间的“拼搏”，实现了：
- 低储存的屏幕截屏
- 截屏转视频
- 获取前台窗口名称，存到数据库
- 提取截图的文本存到数据库
- 打包成exe

有这些问题：
- 截图直接编译为h264的编码器问题，png转mp4可以实现
- ocr识别效果不好
- 脚本打包成exe兼容性问题，无法通过测试（重复点击程序，会导致两份数据库写入）

我在重复点击程序导致双份写入的时候，想了一些解决方案（新建一个json，当程序运行时，改变一个json值，结束时改变一个json值，程序通过读取这个值来判断），但也没有解决。如你所见，我还没有加上llm的功能。

我又读到了李开复对于“AI原生”的思考，我这个程序确实不是AI原生的，我也曾试过用多模态的模型来直接识别，但我无法量化[InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer)这个模型。

......

到今天3月25日，我还是想把这个项目完成，我上传两个基础的文件，截图类 ScreenCapturer 和 窗口名称类 WindowTracker，重新开发。


## 使用方法
```
pip install pygetwindow
pip install mss
```
## 当前进度
封装了一个 WindowTracker 类，提供了可调用的方法，可以获取当前窗口的名字，并存到sqlite数据库中。
封装了一个 ScreenCapturer 类，提供了调用的方法，可以截屏，并保存到文件夹中，
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
