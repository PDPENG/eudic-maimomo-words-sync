![banner](img.png)

# 📘 Eudic-Maimemo-Words Sync Tool

自动从 **欧路词典（Eudic）“生词本动态 API”** 抓取最新单词，过滤中文、去重、排序后生成 `all_words.txt`，并同步更新到 **墨墨背单词（Maimemo）云词本**。
每次运行后自动发送 **飞书通知**。

本项目适合：

* 使用 **欧路查词 + 墨墨记忆** 的用户
* 需要长期稳定自动化同步的用户
* 在服务器定时运行

---


## 🔧 功能特性

* ✔ 自动从欧路词典 API 抓取最新生词
* ✔ 自动过滤中文 → 仅保留英文词汇
* ✔ 自动去重、排序
* ✔ 自动生成 `all_words.txt`
* ✔ 同步到墨墨云词本（Notepad）
* ✔ 飞书通知你任务成功和词数量
* ✔ 支持服务器定时任务（crontab）

---

## 📂 项目结构

```
eudic-maimomo-words-sync/
├── main.py                 # 主程序（抓取 + 清洗 + 生成 txt + 上传 + 通知）
├── config.py               # 配置（API KEY / URL / 路径）
├── sync/
│   ├── eudic.py            # 欧路抓取逻辑
│   ├── maimemo.py          # 墨墨提交模块
│   ├── notify.py           # 飞书通知模块
│   └── utils.py            # 工具模块
├── all_words.txt           # 自动生成的词表文件
├── requirements.txt        # Python 依赖模块列表
└── README.md
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/PDPENG/eudic-maimomo-words-sync.git
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 编辑配置文件

打开：

```
config.py # 由 config.example.py 修改而来
```

填入：

```python
EUDIC_API_KEY = "你的欧路 API key"
MAIMEMO_TOKEN = "你的墨墨 token"
LARK_WEBHOOK = "你的飞书 webhook 地址"

TXT_PATH = "/your-path/all_words.txt"
```

---

## ▶️ 手动运行一次

```bash
python main.py
```

成功后日志会看到：

```
开始同步 Eudic → Maimemo ...
抓取完成，共 2200 个英文单词
已写入到：your-path ...
提交至墨墨云词本中...
✅ 墨墨提交成功
✅ 飞书通知已发送
全部完成！
```

---

## 🛰 服务器自动化（crontab）

编辑定时任务：

```bash
crontab -e
```

例如每月 1 日自动执行：

```
0 3 1 * * /usr/bin/python3 /eudic-maimomo-words-sync/main.py >> /home/yourname/cron.log 2>&1
```

---

## 🔔 飞书通知示例

运行成功后飞书会推送：

```
抓取任务已完成，总计 XXXX 个单词
```

数字会自动根据本次抓取数量变化。

---


## 接口文档

1. 墨墨背单词：https://open.maimemo.com/document
2. 欧路词典：https://my.eudic.net/OpenAPI/Doc_Index#-api-doc

---

## 📝 License

MIT License.