# 📱 應用程式安裝說明

## 🎯 快速使用

現在您有兩種方式使用台股評論 Prompt 生成器：

### 方式一：點擊應用程式圖示 ⭐️ 推薦
1. 找到專案目錄中的 `台股評論Prompt生成器.app`
2. 雙擊圖示即可啟動
3. 首次啟動可能需要允許 macOS 安全性設定

### 方式二：終端機執行
```bash
python stock_prompt_generator.py
```

## 🚀 首次設定

### 1. 移動到應用程式資料夾（可選）
```bash
# 複製應用程式到 Applications 資料夾
cp -r "台股評論Prompt生成器.app" /Applications/

# 或拖拽到 Applications 資料夾
```

### 2. 設定安全性（如果需要）
如果 macOS 阻止應用程式啟動：
1. 開啟「系統偏好設定」→「安全性與隱私」
2. 在「一般」標籤中，點擊「強制打開」或「允許」
3. 或執行以下指令：
```bash
xattr -d com.apple.quarantine "台股評論Prompt生成器.app"
```

## 🎨 應用程式圖示

- **設計風格**：現代化金融應用程式風格
- **主色調**：藍色漸層背景配紫紅色前景
- **圖形元素**：股票走勢圖、數據點
- **文字標示**：「台股 Prompt」

## 📋 系統需求

- **作業系統**：macOS 10.13 或更高版本
- **Python**：3.7+ （必須已安裝）
- **套件**：tkinter、pyperclip

## 🔧 故障排除

### 問題 1：應用程式無法啟動
**解決方法**：
1. 確認已安裝 Python 3：`python3 --version`
2. 安裝 tkinter：`brew install python-tk@3.11`
3. 檢查安全性設定

### 問題 1.5：應用程式啟動但沒有畫面
**解決方法**：
1. 檢查 Activity Monitor（活動監視器）中是否有 Python 進程運行
2. 嘗試直接執行：`cd 專案目錄 && python3 stock_prompt_generator.py`
3. 如果仍無畫面，重新啟動電腦後再試
4. 或手動執行：
```bash
cd "/Users/liu/sideproject/台股評論Prompt生成器"
python3 stock_prompt_generator.py
```

### 問題 2：提示缺少 pyperclip
**解決方法**（選擇任一方法）：
```bash
# 方法一：使用 --user 標誌
pip install pyperclip --user

# 方法二：使用 pipx
brew install pipx
pipx install pyperclip

# 方法三：允許系統套件（不建議）
pip install pyperclip --break-system-packages
```

### 問題 3：圖示不顯示
**解決方法**：
1. 重新整理 Finder：`killall Finder`
2. 清除圖示快取：`sudo find /private/var/folders/ -name com.apple.dock.iconcache -exec rm {} \;`

## ⚡ 進階使用

### 創建桌面捷徑
```bash
# 創建捷徑到桌面
ln -s "/Applications/台股評論Prompt生成器.app" ~/Desktop/
```

### 加入 Dock
1. 打開 Applications 資料夾
2. 拖拽應用程式圖示到 Dock
3. 現在可以從 Dock 快速啟動

### 設定開機自動啟動
1. 「系統偏好設定」→「使用者與群組」
2. 選擇「登入項目」
3. 點擊「+」，選擇應用程式

## 📞 技術支援

如有問題，請：
1. 檢查系統需求是否滿足
2. 查看 GitHub Issues：https://github.com/spenguinlui/-Prompt-
3. 提交新的問題回報

---

**Made with ❤️ for Taiwan Stock Market Analysis**