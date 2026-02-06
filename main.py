import streamlit as st
import os
import sys
import shutil
import json
from pathlib import Path
from dotenv import load_dotenv

# 🔥 取得正確的執行路徑
def get_base_path():
    """取得程式的基礎路徑"""
    if getattr(sys, 'frozen', False):
        # 打包後的環境
        return os.path.dirname(sys.executable)
    else:
        # 開發環境
        return os.path.dirname(os.path.abspath(__file__))

# 設定基礎路徑
BASE_DIR = get_base_path()

# 🔥 從正確的路徑載入 .env（指定編碼）
env_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_path):
    try:
        # 先嘗試 UTF-8
        load_dotenv(env_path, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            # 如果失敗，嘗試 UTF-8-sig（移除 BOM）
            load_dotenv(env_path, encoding='utf-8-sig')
        except UnicodeDecodeError:
            try:
                # 最後嘗試系統預設編碼（Windows 通常是 cp950 或 gbk）
                load_dotenv(env_path, encoding='cp950')
            except:
                st.error(f"❌ 無法讀取 .env 檔案，請檢查編碼格式")
else:
    st.warning(f"⚠️ 找不到 .env 檔案於：{env_path}")

# --- 設定區 ---
SOURCE_DIR = os.getenv("SOURCE_DIR", "")
TARGET_CONFIG_STR = os.getenv("TARGET_CONFIG", "")

try:
    TARGET_CONFIG = json.loads(TARGET_CONFIG_STR)
except json.JSONDecodeError:
    TARGET_CONFIG = {
        "家人": "./Sorted/Family",
        "工作": "./Sorted/Work",
        "風景": "./Sorted/Scenery",
        "垃圾桶/刪除": "./Sorted/Trash"
    }

# 支援的檔案格式
IMAGE_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv']

def get_all_files(source):
    file_list = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if Path(file).suffix.lower() in IMAGE_EXTS + VIDEO_EXTS:
                file_list.append(os.path.join(root, file))
    return file_list


# --- Streamlit 介面 ---
st.set_page_config(page_title="照片快速分類器", layout="wide")
st.title("📸 相片/影片快速整理工具")

# 初始化 Session State
if 'files' not in st.session_state:
    st.session_state.files = get_all_files(SOURCE_DIR)
    st.session_state.index = 0

if st.session_state.index < len(st.session_state.files):
    current_file = st.session_state.files[st.session_state.index]
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.write(f"目前進度: {st.session_state.index + 1} / {len(st.session_state.files)}")
        st.caption(f"檔案路徑: {current_file}")
        
        # 根據檔案類型預覽
        ext = Path(current_file).suffix.lower()
        if ext in IMAGE_EXTS:
            st.image(current_file, use_container_width=True)
        elif ext in VIDEO_EXTS:
            st.video(current_file)

    with col2:
        st.subheader("分類目的地")
        for label, path in TARGET_CONFIG.items():
            if st.button(f"分類至: {label}", key=label, use_container_width=True):
                # 確保目的地資料夾存在
                os.makedirs(path, exist_ok=True)
                
                # 移動檔案
                try:
                    shutil.move(current_file, os.path.join(path, os.path.basename(current_file)))
                    st.success(f"已移動至 {label}")
                    # 前進到下一張
                    st.session_state.index += 1
                    st.rerun()
                except Exception as e:
                    st.error(f"搬移失敗: {e}")
        
        st.divider()
        if st.button("跳過此張 ⏭️", use_container_width=True):
            st.session_state.index += 1
            st.rerun()

else:
    st.balloons()
    st.success("所有檔案已處理完畢！")
    if st.button("重新掃描"):
        st.session_state.files = get_all_files(SOURCE_DIR)
        st.session_state.index = 0
        st.rerun()