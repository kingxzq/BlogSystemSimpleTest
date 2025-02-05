from selenium.webdriver.common.by import By
from common.Utils import BlogDriver
class BlogDetail:
    url = " "
    driver = ""
    def __init__(self):
        self.url = "http://120.26.87.94:8080/blog_detail.html?blogId=2"
        self.driver = BlogDriver.driver
        title = self.driver.title
         #列表⻚已经跳过来了，⽆需再指定url跳转
        if not title=="博客列表⻚":
            self.driver.get(self.url)
    def DetailCheck(self):
         #body > div.container > div.right > div:nth-child(1) > a
         BlogDriver.getScreenShot()
         self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.title")
         self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.date")
         self.driver.find_element(By.CSS_SELECTOR,"#detail > p")
         print("详情页跳转无误")