import os
import shutil
import sys
import threading
import warnings

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow

warnings.filterwarnings('ignore')


class basicconfig(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        # 设置其他窗口无法与之交互，直到该模态窗口关闭
        # self.setWindowModality(Qt.ApplicationModal)

        self.m_bPressed = False
        self.m_point = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.m_bPressed = True
            self.m_point = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.m_bPressed:
            self.move(event.globalPos() - self.m_point)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.m_bPressed = False

    def closeEvent(self, event):
        # 在关闭窗口时销毁（delete）该窗口
        self.deleteLater()
        # 调用父类的 closeEvent 方法，以确保窗口的正常关闭
        super().closeEvent(event)

    def becomeMin(self):
        self.showMinimized()

    def becomeMax(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def closeWindow(self):
        self.close()

    def quitWindow(self):
        clear_temp_thread = threading.Thread(target=self.clear_temp_threading)
        clear_temp_thread.start()
        clear_temp_thread.join()
        sys.exit()

    def clear_temp_threading(self):
        # 获取当前文件的目录
        current_dir = os.path.dirname(__file__)
        # 构建Temp文件夹的路径
        temp_dir = os.path.abspath(os.path.join(current_dir, '..', 'Temp'))
        # 遍历Temp文件夹中的所有文件和文件夹
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            # 如果是文件，直接删除
            if os.path.isfile(file_path):
                os.remove(file_path)
            # 如果是文件夹，递归删除
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
