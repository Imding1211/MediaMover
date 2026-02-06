# 📸 PhotoSorter - 照片／影片快速分類器

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/photo-sorter)

**使用 Streamlit 開發的本機照片與影片快速整理工具**

使用者可以逐一預覽資料夾中的圖片或影片，並透過按鈕將檔案快速分類到指定資料夾，大幅提升整理效率。

[功能特色](#-功能特色) •
[快速開始](#-快速開始) •
[使用說明](#-使用流程) •
[配置設定](#️-設定說明) •
[常見問題](#-注意事項)

</div>

---

## ✨ 功能特色

* **📷 支援圖片與影片即時預覽**
  * 圖片格式：`jpg / jpeg / png / gif / bmp / webp / heic / heif`
  * 影片格式：`mp4 / mov / avi / mkv / wmv / flv`

* **⚡ 以按鈕方式一鍵分類檔案**
  * 快速移動檔案到指定分類資料夾
  * 自訂分類標籤與目標路徑

* **🔄 智慧進度管理**
  * 使用 Streamlit Session State 保留處理進度
  * 支援跳過目前檔案
  * 全部處理完成後可重新掃描資料夾

* **🎨 友善的操作介面**
  * 即時顯示處理進度
  * 清楚的檔案路徑資訊
  * 響應式設計，適應不同螢幕尺寸

---

## 🖥️ 環境需求

* **Python 3.8 以上**（建議 3.9+）
* 本機可存取檔案系統（Windows / macOS / Linux）
* 建議至少 4GB RAM（處理大量檔案時）

---

## 🚀 快速開始

### 📥 方法一：使用執行檔（推薦新手）

適合不熟悉 Python 的使用者，無需安裝任何開發環境。

#### 1️⃣ 下載最新版本

前往 [Releases 頁面](https://github.com/yourusername/photo-sorter/releases/latest) 下載 `PhotoSorter.zip`

#### 2️⃣ 解壓縮並配置

解壓後在 `PhotoSorter.exe` 同目錄建立 `.env` 檔案：

```env
SOURCE_DIR=D:/Photos/ToSort
TARGET_CONFIG={"家人": "./Sorted/Family", "工作": "./Sorted/Work", "風景": "./Sorted/Scenery", "垃圾桶": "./Sorted/Trash"}
```

> 💡 可參考同目錄的 `.env.example` 範本

#### 3️⃣ 執行程式

雙擊 `PhotoSorter.exe`，瀏覽器將自動開啟 `http://localhost:8501`

---

### 💻 方法二：從原始碼執行（開發者）

適合需要自訂功能或進行開發的使用者。

#### 1️⃣ 克隆專案

```bash
git clone https://github.com/yourusername/photo-sorter.git
cd photo-sorter
```

#### 2️⃣ 建立虛擬環境（建議）

**Windows：**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux：**

```bash
python -m venv venv
source venv/bin/activate
```

#### 3️⃣ 安裝套件（⚠️ 必須執行）

本專案使用 `requirements.txt` 管理相依套件，**請先安裝後再啟動程式**：

```bash
pip install -r requirements.txt
```

#### 4️⃣ 配置設定

複製範本並編輯：

```bash
cp .env.example .env
```

編輯 `.env` 設定你的路徑（參考下方「設定說明」）

#### 5️⃣ 啟動程式

在專案根目錄執行：

```bash
streamlit run main.py
```

瀏覽器將自動開啟 `http://localhost:8501`

---

## ⚙️ 設定說明

### 📂 來源資料夾設定

在 `.env` 檔案中設定待分類照片的來源目錄：

```env
SOURCE_DIR=D:/Photos/ToSort
```

**支援格式：**
* Windows：`D:/Photos` 或 `D:\\Photos`
* macOS/Linux：`/Users/username/Photos`

系統會**遞迴掃描**此資料夾下的所有圖片與影片檔案。

---

### 🗂️ 分類目的地設定

可依需求調整分類按鈕名稱與對應的資料夾路徑：

```env
TARGET_CONFIG={"家人": "./Sorted/Family", "工作": "./Sorted/Work", "風景": "./Sorted/Scenery", "寵物": "./Sorted/Pets", "垃圾桶": "./Sorted/Trash"}
```

**格式說明：**
* 使用 JSON 格式
* 鍵（Key）：分類按鈕的顯示名稱
* 值（Value）：目標資料夾路徑（支援相對路徑和絕對路徑）

**範例配置：**

```json
{
  "家人": "./Sorted/Family",
  "工作": "./Sorted/Work",
  "風景": "./Sorted/Scenery",
  "寵物": "./Sorted/Pets",
  "美食": "./Sorted/Food",
  "旅遊": "./Sorted/Travel",
  "垃圾桶": "./Sorted/Trash"
}
```

**重要提示：**
* 目的地資料夾不存在時會**自動建立**
* 檔案會使用 **move（搬移）** 而非複製
* 請確保目標磁碟有足夠空間

---

## 🔁 使用流程

### 基本操作步驟

1. **啟動程式**
   * 執行 `PhotoSorter.exe` 或 `streamlit run main.py`
   * 瀏覽器自動開啟 `http://localhost:8501`

2. **自動掃描**
   * 程式自動掃描來源資料夾中的所有媒體檔案
   * 顯示總檔案數量

3. **預覽檔案**
   * 左側顯示當前照片或影片的預覽
   * 上方顯示處理進度（如：1 / 100）
   * 下方顯示完整檔案路徑

4. **快速分類**
   * 右側點擊分類按鈕（如「家人」、「工作」）
   * 檔案自動移動至指定資料夾
   * 自動前進到下一張

5. **跳過檔案**
   * 點擊「⏭️ 跳過此張」可略過不處理
   * 檔案保留在原位置

6. **完成整理**
   * 全部處理完成後顯示完成訊息 🎉
   * 點擊「🔄 重新掃描」可重新載入資料夾

---

## 🛠️ 進階功能

### 打包成執行檔

如需自行打包，請執行：

```bash
# 安裝 PyInstaller
pip install pyinstaller

# 執行打包
pyinstaller photo_sorter.spec --clean

# 輸出位置
# dist/PhotoSorter.exe
```

### 自訂支援格式

編輯 `main.py` 中的格式列表：

```python
# 新增圖片格式
IMAGE_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic', '.heif', '.tiff']

# 新增影片格式
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm']
```

### 變更預設埠號

編輯 `run_app.py`（僅限執行檔版本）：

```python
"--server.port=8502"  # 改成其他埠號
```

或在命令列指定（原始碼版本）：

```bash
streamlit run main.py --server.port 8502
```

---

## ⚠️ 注意事項

### 檔案安全

* ⚠️ 檔案會被**搬移（move）**而非複製，請確保來源資料已備份
* 若目的地資料夾已有同名檔案，可能導致搬移失敗
* **建議先使用測試資料夾進行驗證**

### 垃圾桶功能

* 「垃圾桶/刪除」目前僅為分類資料夾，**不會真正刪除檔案**
* 如需真正刪除，請手動清空該資料夾

### 效能建議

* **大量檔案**：建議每次處理 500-1000 張
* **網路磁碟**：建議先複製到本機處理
* **SSD vs HDD**：SSD 處理速度更快

### 路徑格式

* Windows 路徑請使用 `/` 或 `\\`（避免單個 `\`）
* `.env` 檔案請儲存為 **UTF-8** 編碼

---

## 🐛 疑難排解

### ❓ 找不到照片 / 顯示「所有檔案已處理完畢」

**可能原因：**
1. `.env` 中的 `SOURCE_DIR` 路徑不正確
2. 資料夾內沒有支援的檔案格式
3. 路徑使用了單個反斜線 `\`

**解決方法：**
```env
# ❌ 錯誤
SOURCE_DIR=D:\Photos\2024

# ✅ 正確
SOURCE_DIR=D:/Photos/2024
# 或
SOURCE_DIR=D:\\Photos\\2024
```

點擊程式中的「🔍 除錯資訊」查看詳細資訊。

---

### ❓ 無法讀取 .env 檔案 / UnicodeDecodeError

**原因：** `.env` 檔案編碼不正確

**解決方法：**
1. 用記事本或 VS Code 開啟 `.env`
2. 另存新檔，編碼選擇 **UTF-8**（不要選 UTF-8 with BOM）
3. 重新執行程式

---

### ❓ 照片無法預覽 / 顯示錯誤

**可能原因：**
1. 檔案損壞
2. 格式不支援
3. 檔案被其他程式佔用

**解決方法：**
* 確認檔案可以用其他軟體正常開啟
* 檢查檔案副檔名是否在支援列表中
* 關閉其他可能佔用檔案的程式（如相簿軟體）

---

### ❓ 移動檔案失敗

**可能原因：**
1. 目標資料夾沒有寫入權限
2. 磁碟空間不足
3. 檔案名稱衝突

**解決方法：**
* 以管理員身份執行程式（Windows）
* 檢查磁碟空間
* 確認目標資料夾沒有同名檔案

---

## 📌 可擴充功能建議

未來版本可能加入的功能：

- [ ] **鍵盤快捷鍵分類**（如 1 / 2 / 3 / D）
- [ ] **顯示 EXIF / 拍攝日期資訊**
- [ ] **重複檔案檢測**
- [ ] **真正刪除或移至系統垃圾桶**
- [ ] **分類結果統計報表**
- [ ] **AI 自動分類建議**
- [ ] **批次重新命名**
- [ ] **雲端同步功能**
- [ ] **多語言支援**

如有需求或建議，歡迎提交 [Issue](https://github.com/yourusername/photo-sorter/issues) 或 [Pull Request](https://github.com/yourusername/photo-sorter/pulls)！

---

## 📂 專案結構

```
photo-sorter/
├── 📄 main.py                 # Streamlit 主程式
├── 📄 run_app.py             # 啟動器（用於打包）
├── 📄 photo_sorter.spec      # PyInstaller 配置
├── 📄 .env.example           # 環境變數範本
├── 📄 .env                   # 環境變數配置（需自行建立）
├── 📄 requirements.txt       # Python 相依套件
├── 📄 README.md             # 專案說明文件
├── 📄 LICENSE               # 授權條款
├── 📄 .gitignore            # Git 忽略清單
├── 🖼️ icon.ico              # 應用程式圖示（可選）
└── 📁 dist/                 # 打包輸出目錄
    └── PhotoSorter.exe      # Windows 執行檔
```

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 如何貢獻

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 貢獻類型

- 🐛 回報 Bug
- 💡 提出新功能建議
- 📝 改善文件
- 🌍 翻譯成其他語言
- 🎨 改善 UI/UX

詳見 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📝 更新日誌

### [1.0.0] - 2026-01-28

#### ✨ 新增
- 初始版本發布
- 圖片和影片預覽功能
- 快速分類功能
- 自訂分類標籤
- 進度追蹤
- 打包成 Windows 執行檔

#### 🐛 修復
- 修復 .env 編碼問題
- 修復路徑解析錯誤

#### 📚 文件
- 完整的 README
- 配置說明
- 常見問題解答

---

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

---

## 👨‍💻 作者

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 致謝

感謝以下開源專案：

- [Streamlit](https://streamlit.io/) - 優秀的 Python Web 框架
- [PyInstaller](https://pyinstaller.org/) - Python 打包工具
- [Pillow](https://python-pillow.org/) - 圖片處理庫
- [python-dotenv](https://github.com/theskumar/python-dotenv) - 環境變數管理

---

## 📞 需要協助？

若需要協助補齊以下功能，歡迎提出需求：

- ⌨️ 加入鍵盤快捷鍵
- 📦 打包成 macOS / Linux 執行檔
- 🔧 其他客製化功能

**聯絡方式：**
- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/photo-sorter/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/photo-sorter/discussions)

---

<div align="center">

### ⭐ 如果這個專案對你有幫助，請給個星星！

**Made with ❤️ by [Your Name](https://github.com/yourusername)**

![GitHub stars](https://img.shields.io/github/stars/yourusername/photo-sorter?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/photo-sorter?style=social)

</div>