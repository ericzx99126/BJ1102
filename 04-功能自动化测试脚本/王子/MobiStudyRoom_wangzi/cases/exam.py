import unittest
from tools import open_app
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from sys import _getframe

class Exam(unittest.TestCase):
    '''模拟考试模块'''
    def setUp(self):
        driver = open_app()
        self.driver = driver
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_case01(self):
        '''模拟考试'''
        mtd_name = _getframe().f_code.co_name
        d = self.driver
        d.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("13261616954")
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("wz19941212")
        d.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
        d.find_element_by_xpath("//android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
        try:
            d.find_element_by_id("com.offcn.yidongzixishi:id/rl_test").click()
            d.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[4]/android.widget.ImageView").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/pager_data_list_item_iv").click()
            sleep(2)
            TouchAction(d).press(x=460, y=1203).move_to(x=3, y=-298).release().perform()
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_describe").send_keys("测试")
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_next").click()
            sleep(2)
            TouchAction(d).press(x=460, y=1203).move_to(x=3, y=-298).release().perform()
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_describe").send_keys("测试")
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_next").click()
            sleep(2)
            TouchAction(d).press(x=460, y=1203).move_to(x=3, y=-298).release().perform()
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_describe").send_keys("测试")
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_next").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_describe").send_keys("测试")
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_head_submit_error").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/tv_submit").click()
            va = d.find_element_by_id("com.offcn.yidongzixishi:id/questionNum").text
            self.assertIn('总题量',va,msg='交卷失败，测试不通过')
            print('交卷成功,测试通过')
        except AssertionError:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_交卷失败.png')
            raise
        except Exception:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise

