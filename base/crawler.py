import requests
from bs4 import BeautifulSoup


def sendRequest(url,encoding="utf-8"):
    Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False
    html = s.get(url, headers=Headers, timeout=400)
    html.encoding = encoding
    page = html.text
    soup = BeautifulSoup(page, features='html.parser')
    return page,soup


def read_html(path,encoding="utf-8"):
    htmlfile = open(path, 'r', encoding=encoding)
    return BeautifulSoup(htmlfile.read(), features="html.parser")

