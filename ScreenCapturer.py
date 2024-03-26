# 导入必要的库
import os
import mss
import mss.tools
from datetime import datetime
import time

class ScreenCapturer:
    """
    截屏类，使用mss库进行截图并保存为以当前时间命名的文件。
    """

    def __init__(self, save_folder='./png', interval=2):
        """
        类的初始化方法。

        :param save_folder: 截图保存的文件夹，默认为'./png'
        :param interval: 截屏时间间隔，默认为2秒
        """
        self.save_folder = save_folder
        self.interval = interval
        # 确保保存文件夹存在
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    def capture(self):
        """
        进行单次截屏，并保存为文件。
        """
        with mss.mss() as sct:
            # 获取屏幕尺寸
            monitor = sct.monitors[1]
            filename = os.path.join(
                self.save_folder,
                datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'
            )

            # 截屏并保存
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
            print(f'截图已保存：{filename}')

    def start_capture(self):
        """
        开始连续截屏，根据设置的时间间隔。
        """
        try:
            while True:
                self.capture()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print('截屏停止')

# 主程序部分
if __name__ == '__main__':
    capturer = ScreenCapturer()
    capturer.start_capture()
