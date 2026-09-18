import os
import sys
import multiprocessing
import webview

# 获取正确的打包解压根目录（用于加载 index.html）
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(base_dir, 'index.html')

# 设置持久化缓存目录（存储在用户 Local AppData 目录下，保证关闭后不丢失历史记录）
storage_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'BookDiceData')

if __name__ == '__main__':
    # 防止 PyInstaller 打包后的子进程重复拉起窗口
    multiprocessing.freeze_support()

    # 创建桌面窗口
    window = webview.create_window(
        '选书骰子', 
        html_path, 
        width=980, 
        height=680, 
        resizable=True
    )
    # 启动 webview 并开启持久化存储
    webview.start(private_mode=False, storage_path=storage_dir)