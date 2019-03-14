from base.crawler import *
page,soup = sendRequest("https://mp.weixin.qq.com/s?__biz=MzI1MjMyMzIxMw==&mid=2247488941&idx=1&sn=7c91fe73cf342b975a0bc0e6ff42d306&chksm=e9e4214fde93a859bef0e43b0bf21767ff73c13cbb2fa573d7a6b858c521be51c7fbf9ed9b4a#rd")
print(page)
with open("../files/page.html","w",encoding="utf-8") as f:
    f.write(page)
f.close()