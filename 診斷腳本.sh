#!/bin/bash

echo "=== 台股評論 Prompt 生成器診斷腳本 ==="
echo "時間: $(date)"
echo ""

# 1. 檢查基本環境
echo "1. 檢查 Python 環境："
python3 --version
echo "Python 路徑: $(which python3)"
echo ""

# 2. 檢查必要模組
echo "2. 檢查必要模組："
echo -n "tkinter: "
python3 -c "import tkinter; print('✅ 可用')" 2>/dev/null || echo "❌ 缺失"

echo -n "pyperclip: "
python3 -c "import pyperclip; print('✅ 可用')" 2>/dev/null || echo "❌ 缺失"
echo ""

# 3. 檢查檔案結構
echo "3. 檢查檔案結構："
echo "專案目錄: $(pwd)"
echo "主程式檔案: $(ls -la stock_prompt_generator.py 2>/dev/null || echo '❌ 不存在')"
echo "應用程式包: $(ls -d *.app 2>/dev/null || echo '❌ 不存在')"
echo ""

# 4. 檢查應用程式包內部
echo "4. 檢查應用程式包內部："
APP_NAME="台股評論Prompt生成器.app"
if [ -d "$APP_NAME" ]; then
    echo "Info.plist: $(ls -la "$APP_NAME/Contents/Info.plist" 2>/dev/null || echo '❌ 不存在')"
    echo "啟動腳本: $(ls -la "$APP_NAME/Contents/MacOS/"* 2>/dev/null || echo '❌ 不存在')"
    echo "啟動腳本權限: $(stat -f "%A" "$APP_NAME/Contents/MacOS/"* 2>/dev/null || echo '❌ 無法檢查')"
else
    echo "❌ 應用程式包不存在"
fi
echo ""

# 5. 測試直接執行 Python 程式
echo "5. 測試直接執行 Python 程式："
if [ -f "stock_prompt_generator.py" ]; then
    echo "嘗試執行 Python 程式（5秒後自動停止）..."
    timeout 5 python3 stock_prompt_generator.py > /tmp/gui_test.log 2>&1 &
    PID=$!
    sleep 2

    if kill -0 $PID 2>/dev/null; then
        echo "✅ Python 程式可以啟動"
        kill $PID 2>/dev/null
    else
        echo "❌ Python 程式啟動失敗"
    fi

    # 檢查錯誤日誌
    if [ -f "/tmp/gui_test.log" ] && [ -s "/tmp/gui_test.log" ]; then
        echo "錯誤訊息:"
        cat /tmp/gui_test.log
    fi
else
    echo "❌ 找不到 stock_prompt_generator.py"
fi
echo ""

# 6. 測試啟動腳本
echo "6. 測試啟動腳本："
if [ -f "$APP_NAME/Contents/MacOS/台股評論Prompt生成器" ]; then
    echo "嘗試執行啟動腳本（5秒後自動停止）..."
    timeout 5 "$APP_NAME/Contents/MacOS/台股評論Prompt生成器" > /tmp/app_test.log 2>&1 &
    PID=$!
    sleep 2

    if kill -0 $PID 2>/dev/null; then
        echo "✅ 啟動腳本可以執行"
        kill $PID 2>/dev/null
    else
        echo "❌ 啟動腳本執行失敗"
    fi

    # 檢查錯誤日誌
    if [ -f "/tmp/app_test.log" ] && [ -s "/tmp/app_test.log" ]; then
        echo "啟動腳本輸出:"
        cat /tmp/app_test.log
    fi
else
    echo "❌ 找不到啟動腳本"
fi
echo ""

# 7. 檢查進程
echo "7. 檢查相關進程："
ps aux | grep -E "(stock_prompt|Python.*stock)" | grep -v grep || echo "沒有相關進程運行"
echo ""

# 8. 建議
echo "8. 診斷建議："
echo "請將以上診斷結果提供給開發者以協助修復問題。"

# 清理臨時檔案
rm -f /tmp/gui_test.log /tmp/app_test.log

echo ""
echo "=== 診斷完成 ==="