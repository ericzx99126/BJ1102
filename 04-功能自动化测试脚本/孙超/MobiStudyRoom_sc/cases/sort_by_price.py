import unittest
import time
import sys
from tools import HOST,open_browser
from appium.webdriver.common.touch_action import TouchAction
class SortByPrice(unittest.TestCase):
    '''排序'''
    def setUp(self):
        driver = open_browser()
        self.driver = driver
        self.cls_name = self.__class__.__name__
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    def test_case01(self):
        '''按照价格排序'''
        driver= self.driver
        mtd_name = sys._getframe().f_code.co_name
        try:
            driver.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
            driver.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("16621248657")
            driver.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("416416d")
            driver.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/llExam")[0].click()
            driver.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
            time.sleep(2)
            driver.find_element_by_id("com.offcn.yidongzixishi:id/iv_coach").click()
            driver.find_element_by_id("com.offcn.yidongzixishi:id/tvSort").click()
            time.sleep(2)
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/textName")[3].click()
            time.sleep(3)
            b=driver.find_elements_by_id('com.offcn.yidongzixishi:id/coursePrice')[0].text
            self.assertEqual(b,'￥1000.00')
        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}排序失败.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise
