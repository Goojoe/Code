#! python3
# mapIt.py - 使用url地址在浏览器中启动地图
# 命令行或剪贴板
import webbrowser
import sys
if len(sys.argv) > 1:
    # 从命令行获取地址。
    address = ' '.join(sys.argv[1:])
else:
    # 从剪贴板获取地址。
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
