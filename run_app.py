import os
import sys
import webbrowser
import time
from pathlib import Path
from streamlit.web import cli as stcli
from threading import Thread

def get_resource_path(relative_path):
    """取得資源檔案的絕對路徑（支援開發環境和打包後環境）"""
    try:
        # PyInstaller 建立的臨時資料夾路徑
        base_path = sys._MEIPASS
    except AttributeError:
        # 開發環境的路徑
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def open_browser():
    time.sleep(3)  # 等待伺服器啟動
    webbrowser.open('http://localhost:8501')

if __name__ == '__main__':
    # 取得 main.py 的正確路徑
    main_script = get_resource_path('main.py')
    
    # 確認檔案存在
    if not os.path.exists(main_script):
        print(f"錯誤：找不到 main.py")
        print(f"搜尋路徑：{main_script}")
        print(f"當前目錄：{os.getcwd()}")
        print(f"sys._MEIPASS：{getattr(sys, '_MEIPASS', '不存在')}")
        input("按 Enter 鍵關閉...")
        sys.exit(1)
    
    # 啟動瀏覽器
    Thread(target=open_browser, daemon=True).start()
    
    # 🔥 關鍵修改：移除 server.port，加入 global.developmentMode=false
    sys.argv = [
        "streamlit",
        "run",
        main_script,
        "--global.developmentMode=false",  # 關閉開發模式
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
        "--server.address=localhost",
        "--server.port=8501"  # 現在可以正常使用了
    ]
    sys.exit(stcli.main())
