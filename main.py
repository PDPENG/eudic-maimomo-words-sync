from sync.eudic import fetch_all_english_words
from sync.utils import save_words_to_txt, load_txt_as_string
from sync.maimemo import update_memo_notepad
from sync.notify import send_feishu_message

from config import (
    TXT_OUTPUT_PATH,
    FEISHU_WEBHOOK,
    MEMO_API_TOKEN,
    MEMO_NOTEPAD_ID
)


def main():
    print("开始同步 Eudic → Maimemo ...")

    # 1. 抓取英文单词
    english_words = fetch_all_english_words()
    print(f"抓取完成，共 {len(english_words)} 个英文单词")

    # 2. 写入 TXT
    save_words_to_txt(english_words, TXT_OUTPUT_PATH)
    print(f"已写入到：{TXT_OUTPUT_PATH}")

    # 3. 从 TXT 读取并提交墨墨
    content = load_txt_as_string(TXT_OUTPUT_PATH)
    update_memo_notepad(content)

    # 4. 飞书通知
    send_feishu_message(
        FEISHU_WEBHOOK,
        title="🎉 Eudic → Maimemo 同步完毕",
        message=f"共同步 {len(english_words)} 个有效英文单词，请及时规划学习！",
    )

    print("全部完成！")


if __name__ == "__main__":
    main()
