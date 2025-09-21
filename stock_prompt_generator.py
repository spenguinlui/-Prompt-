#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票評論 Prompt 生成器
功能：
1. 選擇 4 種不同的 prompt 範本
2. 選擇股票代號和名稱
3. 自動生成今日日期
4. 生成完整的 prompt 並可複製到剪貼簿
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
import os
from datetime import datetime
import pyperclip

class StockPromptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("股票評論 Prompt 生成器")
        self.root.geometry("1400x900")

        # 設定最小視窗大小
        self.root.minsize(1200, 700)

        # 載入股票資料
        self.stocks_data = self.load_stocks_data()

        # 載入 prompt 範本
        self.prompt_templates = self.load_prompt_templates()

        self.setup_ui()

    def load_stocks_data(self):
        """載入股票資料"""
        try:
            stock_file = "/Users/liu/sideproject/stock_commentary/data/taiwan_stocks_latest.json"
            if os.path.exists(stock_file):
                with open(stock_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('stocks', [])
            else:
                # 如果檔案不存在，提供一些常見股票作為示例
                return [
                    {"symbol": "2330", "name": "台積電"},
                    {"symbol": "2317", "name": "鴻海"},
                    {"symbol": "2454", "name": "聯發科"},
                    {"symbol": "2881", "name": "富邦金"},
                    {"symbol": "6505", "name": "台塑化"}
                ]
        except Exception as e:
            messagebox.showerror("錯誤", f"載入股票資料失敗：{str(e)}")
            return []

    def load_prompt_templates(self):
        """載入 prompt 範本"""
        templates = {}

        # Prompt 範本檔案路徑
        template_files = {
            "Perplexity": "/Users/liu/Documents/Obsidian Vault/股票評論 prompt/Perplexity.md",
            "ChatGPT": "/Users/liu/Documents/Obsidian Vault/股票評論 prompt/ChatGPT.md",
            "Claude": "/Users/liu/Documents/Obsidian Vault/股票評論 prompt/Claude.md",
            "Gemini": "/Users/liu/Documents/Obsidian Vault/股票評論 prompt/Gemini.md"
        }

        for name, file_path in template_files.items():
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        templates[name] = f.read()
                else:
                    templates[name] = f"範本檔案不存在：{file_path}"
            except Exception as e:
                templates[name] = f"讀取範本失敗：{str(e)}"

        return templates

    def setup_ui(self):
        """設置使用者介面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="5")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 配置網格權重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)  # 增加右側權重
        main_frame.rowconfigure(5, weight=1)     # 文字區域權重

        # 1. Prompt 範本選擇區
        ttk.Label(main_frame, text="選擇 Prompt 範本：", font=("Arial", 12, "bold")).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 2)
        )

        self.template_var = tk.StringVar(value="Perplexity")
        template_frame = ttk.Frame(main_frame)
        template_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 2))

        for i, template_name in enumerate(self.prompt_templates.keys()):
            ttk.Radiobutton(
                template_frame,
                text=template_name,
                variable=self.template_var,
                value=template_name
            ).grid(row=0, column=i, padx=(0, 20), sticky=tk.W)

        # 2. 股票選擇區
        ttk.Label(main_frame, text="選擇股票：", font=("Arial", 12, "bold")).grid(
            row=1, column=0, sticky=tk.W, pady=(5, 2)
        )

        stock_frame = ttk.Frame(main_frame)
        stock_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(5, 2))
        stock_frame.columnconfigure(1, weight=1)
        stock_frame.columnconfigure(3, weight=1)

        # 股票搜尋框
        ttk.Label(stock_frame, text="搜尋：").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.search_var = tk.StringVar()
        # 修復 Python 3.13 tkinter trace 語法
        try:
            self.search_var.trace('w', self.filter_stocks)
        except tk.TclError:
            # Python 3.13+ 新語法
            self.search_var.trace_add('write', self.filter_stocks)
        search_entry = ttk.Entry(stock_frame, textvariable=self.search_var, width=25)
        search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 15))

        # 股票下拉選單
        ttk.Label(stock_frame, text="股票：").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.stock_var = tk.StringVar()
        self.stock_combobox = ttk.Combobox(stock_frame, textvariable=self.stock_var, width=50, state="readonly")
        self.stock_combobox.grid(row=0, column=3, sticky=(tk.W, tk.E))

        # 初始化股票選項
        self.update_stock_options()

        # 3. 日期顯示區
        ttk.Label(main_frame, text="分析日期：", font=("Arial", 12, "bold")).grid(
            row=2, column=0, sticky=tk.W, pady=(5, 2)
        )

        date_frame = ttk.Frame(main_frame)
        date_frame.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=(5, 2))

        today = datetime.now().strftime("%Y-%m-%d")
        self.date_var = tk.StringVar(value=today)
        ttk.Label(date_frame, textvariable=self.date_var, font=("Arial", 11)).grid(row=0, column=0, sticky=tk.W)

        ttk.Button(date_frame, text="更新為今日", command=self.update_date).grid(row=0, column=1, padx=(20, 0))

        # 4. 操作按鈕區
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(6, 3))

        ttk.Button(
            button_frame,
            text="🚀 生成 Prompt",
            command=self.generate_prompt,
            style="Accent.TButton"
        ).pack(side=tk.LEFT, padx=(0, 15))

        ttk.Button(
            button_frame,
            text="📋 複製到剪貼簿",
            command=self.copy_to_clipboard
        ).pack(side=tk.LEFT, padx=(0, 15))

        ttk.Button(
            button_frame,
            text="🗑️ 清空內容",
            command=self.clear_content
        ).pack(side=tk.LEFT)

        # 5. 結果顯示區
        ttk.Label(main_frame, text="生成的 Prompt：", font=("Arial", 12, "bold")).grid(
            row=4, column=0, sticky=tk.W, pady=(5, 2)
        )

        # 文字顯示區域
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=100,
            height=25,
            font=("SF Mono", 11)
        )
        self.result_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(2, 0))

        # 配置樣式
        self.setup_styles()

    def setup_styles(self):
        """設置樣式"""
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 10, "bold"))

    def update_stock_options(self):
        """更新股票選項"""
        stock_options = [f"{stock['symbol']} - {stock['name']}" for stock in self.stocks_data]
        self.stock_combobox['values'] = stock_options
        if stock_options:
            self.stock_combobox.set(stock_options[0])

    def filter_stocks(self, *args):
        """根據搜尋條件過濾股票"""
        search_term = self.search_var.get().lower()
        if not search_term:
            self.update_stock_options()
            return

        filtered_stocks = [
            stock for stock in self.stocks_data
            if search_term in stock['symbol'].lower() or search_term in stock['name'].lower()
        ]

        stock_options = [f"{stock['symbol']} - {stock['name']}" for stock in filtered_stocks]
        self.stock_combobox['values'] = stock_options
        if stock_options:
            self.stock_combobox.set(stock_options[0])

    def update_date(self):
        """更新日期為今日"""
        today = datetime.now().strftime("%Y-%m-%d")
        self.date_var.set(today)

    def generate_prompt(self):
        """生成 prompt"""
        try:
            # 取得選擇的範本
            template_name = self.template_var.get()
            template_content = self.prompt_templates.get(template_name, "")

            if not template_content:
                messagebox.showerror("錯誤", "找不到選擇的範本")
                return

            # 取得股票資訊
            stock_selection = self.stock_var.get()
            if not stock_selection:
                messagebox.showerror("錯誤", "請選擇股票")
                return

            # 解析股票代號和名稱
            try:
                ticker, name = stock_selection.split(" - ", 1)
            except ValueError:
                messagebox.showerror("錯誤", "股票格式錯誤")
                return

            # 取得日期
            date = self.date_var.get()

            # 替換範本中的參數
            generated_prompt = template_content.replace("{TICKER}", ticker)
            generated_prompt = generated_prompt.replace("{NAME}", name)
            generated_prompt = generated_prompt.replace("{DATE_TPE}", date)
            # 向下相容：如果範本中仍有舊格式的日期參數也一併替換
            generated_prompt = generated_prompt.replace("{TODAY_YYYY-MM-DD}", date)

            # 顯示結果
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, generated_prompt)

            # 顯示成功訊息
            messagebox.showinfo("成功", f"已生成 {template_name} 的 prompt！")

        except Exception as e:
            messagebox.showerror("錯誤", f"生成 prompt 失敗：{str(e)}")

    def copy_to_clipboard(self):
        """複製內容到剪貼簿"""
        try:
            content = self.result_text.get(1.0, tk.END).strip()
            if not content:
                messagebox.showwarning("警告", "沒有內容可以複製")
                return

            pyperclip.copy(content)
            messagebox.showinfo("成功", "內容已複製到剪貼簿！")

        except Exception as e:
            messagebox.showerror("錯誤", f"複製失敗：{str(e)}")

    def clear_content(self):
        """清空內容"""
        self.result_text.delete(1.0, tk.END)

def main():
    """主程式"""
    try:
        # 檢查必要套件
        import pyperclip
    except ImportError:
        print("正在安裝必要套件...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
        import pyperclip

    # 建立主視窗
    root = tk.Tk()

    # 初始化應用程式
    app = StockPromptGenerator(root)

    # 確保視窗顯示在前台（在應用程式初始化後）
    root.update_idletasks()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.focus_force()

    # 設置視窗圖示和其他屬性
    root.resizable(True, True)

    # 在 macOS 上確保應用程式正確顯示
    if hasattr(tk, '_default_root') and tk._default_root:
        root.createcommand('exit', root.quit)

    # 啟動程式
    root.mainloop()

if __name__ == "__main__":
    main()