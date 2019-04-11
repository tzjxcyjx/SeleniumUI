#coding = utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)#{"x":123,"y":234}
left = code_element.location["x"]
top = code_element.location["y"]

# print(code_element.size["width"])
# print(code_element.size["height"])
right = code_element.size["width"]+ left
height = code_element.size["height"] + top
print(left,top,right,height)
im = Image.open("E:/imooc.png")

img = im.crop((left, top, right, height))

img.save("E:/imooc1.png")
# for i in range(5):
#     user_email = ''.join(random.sample("1234567890acfg", 5))+ "@163.com"
#     print(user_email)
#element  = driver.find_element_by_class_name("controls")
#locator = (By.CLASS_NAME,"controls")
#EC.visibility_of_element_located(element)   # 检查当前元素是否可见
#EC.presence_of_element_located()     # 检查当前元素是否在DOM 元素里
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

# print(email_element.get_attribute("placeholder"))   #get_attribute() 传入属性名，如果想要获取到文本框中的输入值，而div 中找不到时候，试试“value”属性
# email_element.send_keys("test@163.com")
# print(email_element.get_attribute("value"))
# driver.close()

# 判断打开的页面是否正 确： 页面元素（页面元素加载需要时间）和 title（比较高效）
# driver.find_element_by_id("register_email").send_keys("18111111@163.com")
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_name_element = user_name_element_node.find_element_by_class_name("form-control")
# #print(len(user_name_element))
# user_name_element.send_keys("sdfsfsf")
# driver.find_element_by_name("password").send_keys("111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")