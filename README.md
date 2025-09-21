# 台股評論 Prompt 生成器

一個簡單易用的 GUI 應用程式，用於生成台灣股票評論的 AI prompt，支援 4 種不同 AI 平台的範本格式。

## 📸 預覽

![應用程式截圖](docs/screenshot.png)

## ✨ 功能特色

- 🤖 **四種 AI 平台範本**：支援 Perplexity、ChatGPT、Claude、Gemini
- 📊 **完整台股清單**：內建 638 檔台灣上市櫃股票資料
- 🔍 **智慧搜尋**：可依股票代號或公司名稱快速搜尋
- 📅 **自動日期**：自動帶入今日日期，也可手動調整
- 📋 **一鍵複製**：生成後可直接複製到剪貼簿
- 🎯 **參數替換**：自動替換範本中的變數參數（支援新舊格式）

## 🔧 系統需求

### 必要依賴
- **Python 3.7+**
- **tkinter**（GUI 框架）
- **pyperclip**（剪貼簿操作）

### macOS 安裝依賴

#### 1. 安裝 tkinter
```bash
# 使用 Homebrew 安裝 tkinter
brew install python-tk@3.11  # 替換為您的 Python 版本
```

#### 2. 安裝 Python 套件
```bash
pip install pyperclip
```

### Windows 安裝依賴
```bash
# tkinter 通常已內建，只需安裝 pyperclip
pip install pyperclip
```

### Linux 安裝依賴
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk
pip install pyperclip

# CentOS/RHEL
sudo yum install tkinter
pip install pyperclip
```

## 🚀 安裝與執行

### 方法一：點擊應用程式圖示 ⭐️ 推薦
```bash
# 克隆專案
git clone https://github.com/spenguinlui/-Prompt-.git
cd 台股評論Prompt生成器

# 安裝依賴
pip install -r requirements.txt

# 雙擊應用程式圖示
# 找到 "台股評論Prompt生成器.app" 並雙擊啟動
```

### 方法二：終端機執行
```bash
# 克隆專案
git clone https://github.com/spenguinlui/-Prompt-.git
cd 台股評論Prompt生成器

# 安裝依賴
pip install -r requirements.txt

# 執行應用程式
python stock_prompt_generator.py
```

### 方法三：開發模式
```bash
# 克隆專案
git clone https://github.com/spenguinlui/-Prompt-.git
cd 台股評論Prompt生成器

# 創建虛擬環境（建議）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 執行應用程式
python stock_prompt_generator.py
```

## 📖 使用說明

### 1. 選擇 Prompt 範本
在應用程式上方選擇要使用的 AI 平台：
- **Perplexity**：多輪網頁檢索，附可點擊來源
- **ChatGPT**：瀏覽功能，覆蓋檢查表
- **Claude**：長文本友好，四階段流程
- **Gemini**：網頁優先，重點摘錄表

### 2. 搜尋與選擇股票
- 在搜尋框輸入股票代號（如：2330）或公司名稱（如：台積電）
- 從下拉選單選擇目標股票
- 支援模糊搜尋，輸入部分關鍵字即可過濾

### 3. 確認分析日期
- 預設為今日日期（YYYY-MM-DD 格式）
- 可點擊「更新為今日」按鈕重置為當前日期

### 4. 生成並使用 Prompt
- 點擊「生成 Prompt」按鈕
- 在下方文字區域查看生成的完整 prompt
- 點擊「複製到剪貼簿」
- 貼到任何 AI 平台使用

## 📁 專案結構

```
台股評論Prompt生成器/
├── stock_prompt_generator.py             # 主程式
├── 台股評論Prompt生成器.app/             # macOS 應用程式包 ⭐️
│   ├── Contents/
│   │   ├── Info.plist                   # 應用程式資訊
│   │   ├── MacOS/台股評論Prompt生成器    # 啟動腳本
│   │   └── Resources/                   # 圖示資源
├── README.md                            # 專案說明
├── APP_安裝說明.md                      # 應用程式安裝指南
├── requirements.txt                     # Python 依賴
├── .gitignore                           # Git 忽略檔案
├── docs/                                # 文件目錄
│   └── screenshot.png                   # 應用程式截圖
└── stock_commentary/                    # 股票資料目錄
    └── data/
        ├── taiwan_stocks_latest.json    # 台股清單（JSON）
        ├── taiwan_stocks_latest.csv     # 台股清單（CSV）
        └── README.md                    # 資料說明
```

## 🔧 設定

### Prompt 範本來源
應用程式會從以下路徑載入 prompt 範本：
```
/Users/您的用戶名/Documents/Obsidian Vault/股票評論 prompt/
├── Perplexity.md
├── ChatGPT.md
├── Claude.md
└── Gemini.md
```

如果範本檔案不存在，請確認路徑正確或聯繫專案維護者。

### 股票資料更新
如需更新股票清單，可執行：
```bash
cd stock_commentary
python comprehensive_stock_list_crawler.py
```

## 🤝 參與貢獻

歡迎提交 Issues 和 Pull Requests！

### 開發步驟
1. Fork 專案
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📝 變更日誌

### v1.3.3 (2025-09-21)
- 🎨 調整 GUI 介面比例和佈局
- ✅ 放大視窗尺寸（1400x900）
- ✅ 改善文字顯示區域大小和字體
- ✅ 優化按鈕樣式，新增圖示
- ✅ 進一步修復應用程式包啟動問題

### v1.3.2 (2025-09-21)
- 🔧 修復 GUI 視窗顯示問題
- ✅ 改善 tkinter 視窗前台顯示
- ✅ 新增視窗焦點強制獲取
- ✅ 完善故障排除文件

### v1.3.1 (2025-09-21)
- 🔧 修復應用程式包路徑問題
- ✅ 解決「找不到程式檔案」錯誤
- ✅ 改善 Python 環境相容性
- ✅ 支援多種 pyperclip 安裝方法

### v1.3.0 (2025-09-21)
- 📱 新增 macOS 應用程式包（.app）
- ✅ 可點擊圖示直接啟動，無需終端機
- ✅ 自動檢查依賴套件並提示安裝
- ✅ 精美的應用程式圖示設計
- ✅ 完整的安裝說明文件

### v1.2.0 (2025-09-21)
- 🔄 大幅更新 ChatGPT 範本
- ✅ 強化目標價收斂邏輯（Low/Mid/High + 單一 Mid）
- ✅ 新增估值決策樹（PE/P/B/PS 代理路徑）
- ✅ 增強可執行觸發條件與出場規則
- ✅ 量化門檻標準化（S_flow, R_float, z_V, CR）

### v1.1.0 (2025-09-21)
- 🔄 更新 prompt 範本格式
- ✅ 支援新的日期參數 `{DATE_TPE}`
- ✅ 向下相容舊格式 `{TODAY_YYYY-MM-DD}`
- ✅ 優化範本結構（兩段式流程）

### v1.0.0 (2025-01-15)
- 🎉 初始版本發布
- ✅ 支援四種 AI 平台範本
- ✅ 完整台股清單（638檔）
- ✅ GUI 介面
- ✅ 一鍵複製功能

## ⚠️ 注意事項

- 本工具僅供學習和個人使用
- 生成的 prompt 內容僅為範本，不構成投資建議
- 股票資料來源於公開資訊，請以官方公告為準

## 📞 技術支援

如遇到問題，請：
1. 查看本 README 的故障排除部分
2. 在 GitHub Issues 中搜尋相關問題
3. 提交新的 Issue 並詳細描述問題

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

---

**Made with ❤️ for Taiwan Stock Market Analysis**