# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest
from tools import HOST
import sys
import time

class Login(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "5.1.1"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["app"] = "E:\\App_Project\\apk\\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk"
        caps["appPackage"] = "com.offcn.yidongzixishi"
        caps["appActivity"] = "com.offcn.yidongzixishi.SplashActivity"
        caps["noReset"] = False
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.get('%s/App_Code_han/' % HOST)
        driver.implicitly_wait(5)
        self.br = driver
        self.cls_name = self.__class__.__name__
    def tearDown(self):
        time.sleep(3)
        self.br.quit()

    def test_case01(self):
        '''正常流程-用户名登录'''
        driver = self.br
        mtd_name = sys._getframe().f_code.co_name

        try:
            el1 = driver.find_element_by_id("com.offcn.yidongzixishi:id/skip")
            el1.click()
            el2 = driver.find_element_by_id("com.offcn.yidongzixishi:id/et_phone")
            el2.send_keys("17353682510")
            el3 = driver.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd")
            el3.send_keys("Requiescat in pace")
            el4 = driver.find_element_by_id("com.offcn.yidongzixishi:id/btn_login")
            el4.click()
            el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
            el5.click()

            # TouchAction(driver).tap(x=357, y=913).perform()

        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_提示信息不正确.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise

    def test_case02(self):
        '''异常流程-用户名登录'''
        driver = self.br
        mtd_name = sys._getframe().f_code.co_name

        try:
            el1 = driver.find_element_by_id("com.offcn.yidongzixishi:id/skip")
            el1.click()
            el2 = driver.find_element_by_id("com.offcn.yidongzixishi:id/et_phone")
            el2.send_keys("17353682510")
            el3 = driver.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd")
            el3.send_keys("Requiescat in pace")
            el4 = driver.find_element_by_id("com.offcn.yidongzixishi:id/btn_login")
            el4.click()
            el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
            el5.click()

            # TouchAction(driver).tap(x=357, y=913).perform()

        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_提示信息不正确.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise