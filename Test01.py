import time
import datetime
import os  # 导入 os 模块

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#驱动程序管理的自动化
#创建驱动对象
#设置无头模式
options = webdriver.ChromeOptions()
options.add_argument("-headless")
#页面加载策略 normal 默认值, 等待所有资源下载 none 完全不会阻塞WebDriver
#eager DOM访问已准备就绪, 但诸如图像的其他资源可能仍在加载
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
# #1.打开浏览器
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# #2.输⼊百度网址:https://www.baidu.com
# driver.get("https://www.baidu.com")
# time.sleep(2)
#
# #3、找到输⼊框并输入“C++”
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("C++")
# time.sleep(2)
#
# #4、找到“百度⼀下”按钮并点击
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(2)
#
# #5、关闭浏览器
# driver.quit()

# #1.打开浏览器
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# #2.输⼊bing网址:https://cn.bing.com/
# driver.get("https://cn.bing.com/")
# time.sleep(2)
#
# #3、找到输⼊框并输入“C++”
# driver.find_element(By.CSS_SELECTOR,"#sb_form_q").send_keys("C++")
# time.sleep(2)
#
# #4、找到“搜索”按钮并点击
# #driver.find_element(By.CSS_SELECTOR,"#sb_form_go").click()
# # 隐藏或禁用使用 JavaScript 强制点击按钮
# driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "#sb_form_go"))
# time.sleep(2)
#
# #5、关闭浏览器
# driver.quit()


# #找到输⼊框并输入“C++”
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("C++")
# time.sleep(2)

# #清除重新输入“java”
# driver.find_element(By.CSS_SELECTOR,"#kw").clear()
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("java")
# time.sleep(2)

# #找到“百度⼀下”按钮并点击
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(2)
#
# # 等待热搜列表加载完毕
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="hotsearch-item odd"]/a/span[@class="title-content-title"]')))
#
# # 获取第一个热搜项的标题文本
# text = driver.find_element(By.XPATH, '//*[@class="hotsearch-item odd"]/a/span[@class="title-content-title"]').text
# print(f"text: {text}")
#
# #获取当前⻚⾯标题,获取当前⻚⾯URL
# title = driver.title
# url = driver.current_url
# print(title)
# print(url)

## 切换窗⼝
# curWindow = driver.current_window_handle
# allWindows = driver.window_handles
# for window in allWindows:
#     if window != curWindow:
#         driver.switch_to.window(window)
# time.sleep(2)

#窗⼝最⼤化
driver.maximize_window()
time.sleep(2)
# #窗⼝最⼩化
# driver.minimize_window()
# time.sleep(2)
# #窗⼝全屏
# driver.fullscreen_window()
# time.sleep(2)
# #⼿动设置窗⼝⼤⼩
# driver.set_window_size(1024,768)
# time.sleep(2)


# # 获取当前脚本的绝对路径并创建完整的路径
# base_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本路径
# image_folder = os.path.join(base_path, 'images')  # 在当前脚本目录下创建 images 文件夹
#
# # 如果文件夹不存在，则创建它
# if not os.path.exists(image_folder):
#     os.makedirs(image_folder)
#
# print("Current working directory:", os.getcwd())
#
# # 简单版本
# driver.save_screenshot(os.path.join(image_folder, 'image.png'))
#
# # 高阶版本：使用当前时间生成动态文件名
# filename = "autotest-" + datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '.png'
# driver.save_screenshot(os.path.join(image_folder, filename))


# #警告弹窗+确认弹窗
# alert = driver.switchTo.alert
# #确认
# alert.accept()
# #取消
# alert.dismiss()
#
# #提⽰弹窗
# alert = driver.switchTo.alert
# alert.send_keys("hello")
# alert.accept()
# alert.dismiss()

# #强制等待
# time.sleep(2)
# #隐式等待,隐式等待作⽤域是整个脚本的所有元素。即只要driver对象没有被释放掉（ driver.quit() ），隐式等待就⼀直⽣效
# driver.implicitly_wait(5)
# #显示等待，在指定超时时间范围内只要满⾜操作的条件就会继续执⾏后续代码
# wait=WebDriverWait(driver,2)
# wait.until(EC.invisibility_of_element((By.XPATH,'//*[@id="2"]/div/div/div[3]/div[1]/div[1]/div')))

# #隐式等待设置为10s，显⽰等待设置为15s，那么结果会是5+10=15s吗？
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver,15)
# start = time.time()
# try:
#  res = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="2"]/div/div/div[3]/div[1]/div[1]/div/div/div')))
# except:
#  end = time.time()
#  print("no such element")
# driver.quit()
# print(end-start)

# # 浏览器的前进、后退、刷新
# driver.back()
# time.sleep(2)
#
# driver.forward()
# time.sleep(2)
#
# driver.refresh()
# time.sleep(2)

# #上传文件
# driver.get("file:///E:/study/Test/selenium-html/upload.html")
# ele = driver.find_element(By.CSS_SELECTOR,"body > div > div > input[type=file]")
# time.sleep(2)
# ele.send_keys("E:\\study\\Test\\1.txt")
# time.sleep(2)

# 关闭浏览器
driver.quit()