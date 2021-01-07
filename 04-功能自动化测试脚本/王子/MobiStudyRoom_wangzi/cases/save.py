import unittest
from tools import open_app
from time import sleep
from sys import _getframe

class Save(unittest.TestCase):
    '''缓存模块'''
    def setUp(self):
        driver = open_app()
        self.driver = driver
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_case01(self):
        '''缓存功能'''
        mtd_name = _getframe().f_code.co_name
        d = self.driver
        d.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("13261616954")
        d.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("wz19941212")
        d.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
        d.find_element_by_xpath("//android.widget.LinearLayout[6]/android.widget.RelativeLayout").click()
        d.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
        try:
            sleep(1)
            d.tap([(114,1004),(518,1042)], duration=None)
            d.find_element_by_id("com.offcn.yidongzixishi:id/ziliaolist_item_name").click()
            d.find_element_by_xpath("//android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]").click()
            d.tap([(40, 707),(860, 795)], duration=None)
            d.find_element_by_id("com.offcn.yidongzixishi:id/headBack").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/couserdetial_xiazai").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/chakanhuancun").click()
            va = d.find_element_by_id("com.offcn.yidongzixishi:id/title").text
            self.assertEqual("党的十九大报告核心考点及命题",va,msg="缓存的文件不存在，测试不通过")
            print('缓存成功，测试通过')

        except AssertionError:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_缓存的文件不存在.png')
            raise
        except Exception:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise

