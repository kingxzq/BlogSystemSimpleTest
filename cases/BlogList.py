import time

from selenium.webdriver.common.by import By
from common.Utils import BlogDriver
class BlogList:
    url = ""
    driver = ""
    def __init__(self):
        self.driver = BlogDriver.driver
        self.url = "http://120.26.87.94:8080/blog_list.html"
        self.driver.get(self.url)

     # 前提：登陆状态下才能进⼊到列表⻚
    def ListTest(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.title")
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.desc")
        # articles = self.driver.find_elements(By.CSS_SELECTOR, "body > div.container > div.right > div")
        # assert len(articles) > 10
        # 点击⽂章
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > a").click()
        # title = self.driver.title
        # assert title == "博客详情⻚"
        print("博客控件无误")
        BlogDriver.getScreenShot()