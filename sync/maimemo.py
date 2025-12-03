import requests
from config import MEMO_API_TOKEN, MEMO_NOTEPAD_ID


def update_memo_notepad(content):

    url = f"https://open.maimemo.com/open/api/v1/notepads/{MEMO_NOTEPAD_ID}"

    payload = {
        "notepad": {
            "status": "UNPUBLISHED",
            "content": content,
            "title": "欧路词典生词本",
            "brief": "欧路 API 自动同步",
            "tags": ["词典"]
        }
    }

    headers = {
        "Authorization": f"Bearer {MEMO_API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    print("提交至墨墨云词本中...")

    r = requests.post(url, json=payload, headers=headers, timeout=10)

    if r.status_code in (200, 201):
        print("✅ 墨墨提交成功")
    else:
        print(f"❌ 墨墨提交失败：{r.status_code}")
        print(r.text)
