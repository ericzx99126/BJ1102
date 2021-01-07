# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest
from tools import HOST
import sys
import time

class Tiku(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "5.1.1"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["app"] = "E:\\App_Project\\apk\\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk"
        caps["appPackage"] = "com.offcn.yidongzixishi"
        caps["appActivity"] = "com.offcn.yidongzixishi.SplashActivity"
        caps["noReset"] = True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.get('%s/App_Code_han/' % HOST)
        driver.implicitly_wait(5)
        self.br = driver
        self.cls_name = self.__class__.__name__
    def tearDown(self):
        time.sleep(3)
        self.br.quit()

    def test_case01(self):
        '''正常流程-退出账号'''
        driver = self.br
        mtd_name = sys._getframe().f_code.co_name
        try:
            time.sleep(3)
            TouchAction(driver).tap(x=359, y=911).perform()
            TouchAction(driver).tap(x=628, y=1225).perform()
            driver.back()
            el1 = driver.find_element_by_id("com.offcn.yidongzixishi:id/iv_mine")
            el1.click()
            el2 = driver.find_element_by_id("com.offcn.yidongzixishi:id/mineSettting")
            el2.click()
            el3 = driver.find_element_by_id("com.offcn.yidongzixishi:id/loginOut")
            el3.click()

        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_提示信息不正确.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise

