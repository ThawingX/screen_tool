import keyboard
import threading
from screentool.recorder import start_recording
from screentool.set_hovering import start_hovering_hotkey


def start_recording_hotkey():
    start_recording()


def main():
    # 注册快捷键组合，当按下Ctrl + F1时调用start_recording_hotkey函数
    keyboard.add_hotkey("ctrl+f1", start_recording_hotkey)
    # 当按下 Ctrl + F2 时调用start_hover_hotkey函数
    keyboard.add_hotkey("ctrl+f2", start_hovering_hotkey)

    # 监听快捷键
    keyboard.wait("esc")  # 当按下esc键时退出监听


if __name__ == "__main__":
    # 在单独的线程中启动监听，以免阻塞主线程
    screentool_listening_thread = threading.Thread(target=main)
    screentool_listening_thread.start()
