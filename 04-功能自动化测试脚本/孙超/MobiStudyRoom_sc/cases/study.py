import unittest
import time
import sys
from tools import HOST,open_browser
from appium.webdriver.common.touch_action import TouchAction
class Study(unittest.TestCase):
    '''浏览申论范文'''
    def setUp(self):
        driver = open_browser()
        self.driver = driver
        self.cls_name = self.__class__.__name__
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    def test_case01(self):
        '''浏览申论范文'''
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
            driver.find_element_by_id("com.offcn.yidongzixishi:id/iv_study").click()
            TouchAction(driver).press(x=443, y=1224).move_to(x=52, y=-1043).release().perform()
            time.sleep(3)
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/book_user_item_item_tv")[2].click()
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/ziliaolist_item_name")[0].click()
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/img_select")[0].click()
            d=driver.find_element_by_id('com.offcn.yidongzixishi:id/title_main').text
            self.assertEqual(d, '范文精选-1	2016国家省级')
            time.sleep(2)
            TouchAction(driver).press(x=443, y=1224).move_to(x=52, y=-1043).release().perform()

        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}浏览范文错误.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise