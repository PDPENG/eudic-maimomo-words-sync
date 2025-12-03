import requests


def send_feishu_message(webhook, title, message):
    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {"title": {"tag": "plain_text", "content": title}},
            "elements": [
                {
                    "tag": "div",
                    "text": {"tag": "lark_md", "content": message}
                }
            ]
        }
    }

    r = requests.post(webhook, json=payload, timeout=10)

    if r.status_code == 200:
        print("✅ 飞书通知已发送")
    else:
        print(f"❌ 飞书通知失败: {r.status_code}\n{r.text}")
