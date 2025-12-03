import requests
import time
from collections import OrderedDict
import re
from config import EUDIC_API_TOKEN, EUDIC_LANGUAGE

HEADERS = {"Authorization": EUDIC_API_TOKEN, "User-Agent": "Mozilla/5.0"}
BASE = "https://api.frdic.com/api/open/v1/studylist/words"
CATS_URL = f"https://api.frdic.com/api/open/v1/studylist/category?language={EUDIC_LANGUAGE}"

EN_WORD_RE = re.compile(r"^[a-zA-Z\-']+$")


def safe_get(url, timeout=10, retry=2):
    for i in range(retry + 1):
        try:
            return requests.get(url, headers=HEADERS, timeout=timeout)
        except:
            time.sleep(1)
    raise RuntimeError(f"GET 失败：{url}")


def get_books():
    r = safe_get(CATS_URL)
    return r.json().get("data", [])


def detect_page_start(category_id):
    url0 = f"{BASE}?language={EUDIC_LANGUAGE}&category_id={category_id}&page=0&page_size=500"
    url1 = f"{BASE}?language={EUDIC_LANGUAGE}&category_id={category_id}&page=1&page_size=500"

    ok0 = bool(safe_get(url0).json().get("data"))
    ok1 = bool(safe_get(url1).json().get("data"))

    return 0 if ok0 else 1


def get_words_of_book(book_id):
    page = detect_page_start(book_id)
    all_items = []

    while True:
        url = f"{BASE}?language={EUDIC_LANGUAGE}&category_id={book_id}&page={page}&page_size=500"
        r = safe_get(url)
        data = r.json().get("data", [])
        if not data:
            break
        all_items.extend(data)
        if len(data) < 500:
            break
        page += 1

    # 去重
    seen = OrderedDict()
    for it in all_items:
        w = it.get("word")
        if w:
            seen[w] = None

    return list(seen.keys())


def fetch_all_english_words():
    books = get_books()

    all_words = OrderedDict()
    for b in books:
        wid = b["id"]
        words = get_words_of_book(wid)
        for w in words:
            all_words[w] = None

    english = [w for w in all_words if EN_WORD_RE.match(w)]
    return english
