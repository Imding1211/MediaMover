import streamlit as st
import os
import shutil
from pathlib import Path

# --- 設定區 ---
SOURCE_DIR = "C:/Users/chihengting/Desktop/photo/照片"  # 例如 "C:/Photos/202401"
# 定義你的按鈕標籤與對應的目的地路徑
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