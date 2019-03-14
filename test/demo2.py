from time import sleep
import json
from selenium import webdriver # 从selenium导入webdriver


def readCookieFile(path):
    #读入cookies文件，准备将其写入网站，以跳过扫码登录部分
    with open(path) as f:
        cookieDic = json.load(f)
        return cookieDic


if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.vreadtech.com/hh.php?id=WestChina_Hospital')
    driver.find_element_by_id("name").send_keys("菠萝因子")
    driver.find_element_by_id("idx").click()
    sleep(2)#等待网站加载，可尝试修改为selenium提供的方法  https://selenium-python-zh.readthedocs.io/en/latest/waits.html
    driver.find_elements_by_class_name("search_modal")[0].find_elements_by_tag_name("a")[0].click()
    for x in dict(readCookieFile("../data/cookie.json")).values():
        driver.add_cookie(x)
    #这里已经可以开始获取文章链接
    #添加下面备注部分的代码

    print("当前cookies",driver.get_cookies())
    # driver.close()

    """
    以 https://www.vreadtech.com 作为跳板 获取公众号历史文章信息
    1、可以尝试使用selenium 操作chrome driver 翻页，以获取全部文章的链接
    2、通过requests 根据链接 下载页面
    3、设计数据库，保存获取的文章信息（图片、文字、标题、来源等等都需要记录）
    
    注意：
    获取的文章链接可能存在有效期
    """

