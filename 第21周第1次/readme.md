# Week 1 — Project Refactoring & Watchlist CLI

本周目标不是增加功能，而是把旧项目升级成 **真正的工程结构**。  
你将看到：模块化、目录规范化、数据隔离、文档化、可维护性提升。

---

## 📌 1. 项目目标（Project Goal）

本项目通过对旧代码进行工程化重构，达到以下目标：

- 从“能运行的脚本”升级为“可维护的工程”
- 建立统一的目录结构（src / data / docs / tests）
- 拆分模块职责（analysis / check / get_answers）
- 添加 `.gitignore`，避免上传缓存与隐私数据
- 编写专业 README 文档
- 完成 Week1 必交代码：**Watchlist CLI**

---

## 📌 2. 目录结构（Project Structure）

project/
│  .gitignore
│  main.py
│  attack.py
│  security result.md
│  security_table.md
│
├─data/
│    user_logs.jsonl
│
└─src/
├─analysis/
│    analysis.py
│    save_user_logs.py
│    └─data/
│         info.py
│         user_logs.jsonl
│
├─check/
│    ifallowed.py
│    isok.py
│    └─data/
│         info.py
│         strangethings.py
│
└─get_answers/
load_answers.py

### 📌 模块职责说明

- **main.py** — 项目入口  
- **attack.py** — 安全攻击模拟逻辑  
- **src/analysis/** — 日志分析、用户行为分析  
- **src/check/** — 安全检查、权限判断  
- **src/get_answers/** — 加载答案、数据处理  
- **data/** — 用户日志与原始数据（已被 `.gitignore` 忽略）

---

## 📌 3. Watchlist CLI（Week1 必交代码）

此 CLI 程序允许用户：

- 添加公司  
- 删除公司  
- 查看监控列表  
- 保存到 JSON  
- 从 JSON 加载  

代码位于：

project/src/watchlist.py

核心功能：

```python
def add_company(watchlist): ...
def delete_company(watchlist): ...
def view_watchlist(watchlist): ...
def save_watchlist(watchlist): ...
def load_watchlist(): ...
数据文件：

project/data/watchlist.json
📌 4. 工程化改进（Refactoring Improvements）
本周对旧项目进行了以下工程化升级：

拆分模块 → 代码职责更清晰

添加 .gitignore → 避免上传缓存与隐私数据

统一目录结构 → 更符合 GPT 公司工程标准

数据隔离 → 所有数据放入 data/

文档化 → 添加 README

可维护性提升 → 更容易协作与扩展

📌 5. .gitignore（专业版）
本项目使用的 .gitignore：

__pycache__/
*.pyc
*.pyo
*.pyd

venv/
.env/
.venv/

.vscode/
.idea/

.DS_Store
Thumbs.db

logs/
*.log

data/
src/**/data/
*.jsonl
*.csv

build/
dist/
*.egg-info/

*.tmp
*.bak
📌 6. 如何运行（Usage）
运行主项目
python main.py
运行 Watchlist CLI：
python src/watchlist.py