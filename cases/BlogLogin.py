import time
from selenium.webdriver.common.by import By
from common.Utils import BlogDriver
class BlogLogin:
    url = ""
    driver = ""

    def __init__(self):
        self.url = "http://120.26.87.94:8080/blog_login.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def loginSucTest(self):
        time.sleep(2)
        #self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        #self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        # 对登录结果进⾏检测, 如果跳转到了博客列表⻚才算是登录成功了
        # self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > img")
        time.sleep(2)
        print("登陆成功")
        BlogDriver.getScreenShot()
        #self.driver.back()

    def loginFailTest(self):
        self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("111")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        print("⽤⼾名或密码错误!")
        BlogDriver.getScreenShot()
        self.driver.back()

#BlogLogin().loginSucTest()
#BlogLogin().loginFailTest()