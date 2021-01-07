import unittest
import time
import sys
from tools import HOST,open_browser
from appium.webdriver.common.touch_action import TouchAction
class Answer(unittest.TestCase):
    '''浏览答题报告'''
    def setUp(self):
        driver = open_browser()
        self.driver = driver
        self.cls_name = self.__class__.__name__
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    def test_case01(self):
        '''浏览zxs答题报告'''
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
            driver.find_element_by_id("com.offcn.yidongzixishi:id/iv_test").click()
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/tiku_first_ft_gr_item_iv")[2].click()
            time.sleep(2)
            driver.find_elements_by_id("com.offcn.yidongzixishi:id/pager_list_item_tv")[0].click()
            time.sleep(2)
            TouchAction(driver).press(x=548, y=579).move_to(x=17, y=-363).release().perform()
            c=driver.find_elements_by_id('com.offcn.yidongzixishi:id/error_pars_ti')[0].text
            self.assertEqual(c,'错题解析')
        except AssertionError:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}答题错误.png')
            raise
        except Exception:
            driver.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise