import unittest
from tools import open_app
from time import sleep
from sys import _getframe

class Subject(unittest.TestCase):
    '''科目模块'''
    def setUp(self):
        driver = open_app()
        self.driver = driver
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_case01(self):
        '''切换科目'''
        mtd_name = _getframe().f_code.co_name
        d = self.driver
        d.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("13261616954")
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("wz19941212")
        d.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
        d.find_element_by_xpath("//android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
        try:
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_mine").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/examType").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/iv_head_commit").click()
            d.swipe(500, 1200, 500, 500, 1000)
            d.swipe(500, 1200, 500, 300, 1000)
            d.find_element_by_xpath("//android.widget.LinearLayout[13]/android.widget.RelativeLayout/android.widget.TextView").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/headRight").click()
            d.find_element_by_xpath("//android.view.View[2]/android.widget.LinearLayout/android.widget.TextView[2]").click()
            va = d.find_element_by_id("com.offcn.yidongzixishi:id/examType").text
            self.assertEqual('社会工作师',va,msg='切换失败，测试不通过')
            print('切换科目成功,测试通过')
        except AssertionError:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_切换失败.png')
            raise
        except Exception:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise

