import unittest
from tools import open_app
import time
from sys import _getframe

class Login(unittest.TestCase):
    '''登录退出模块'''
    def setUp(self):
        driver = open_app()
        self.driver = driver
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_case01(self):
        '''登录退出'''
        mtd_name = _getframe().f_code.co_name
        d = self.driver
        try:
            d.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("13261616954")
            d.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("wz19941212")
            d.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
            d.find_element_by_xpath("//android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
            d.find_element_by_id("com.offcn.yidongzixishi:id/rl_mine").click()
            va1 = d.find_element_by_xpath("//android.widget.TextView[@resource-id='com.offcn.yidongzixishi:id/userName']").text
            self.assertEqual('cou7180', va1, msg='页面中有用户名存在，测试不通过')
            print('登陆功能正常，测试通过')
            try:
                d.find_element_by_id("com.offcn.yidongzixishi:id/mineSettting").click()
                d.find_element_by_id("com.offcn.yidongzixishi:id/loginOut").click()
                va2 = d.find_element_by_id("com.offcn.yidongzixishi:id/tv_find_pwd").text
                self.assertEqual('找回密码', va2, msg='页面中没有找回密码选项，测试不通过')
                print('退出功能正常，测试通过')
            except AssertionError:
                d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_推出功能出错.png')
                raise
            except Exception:
                d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
                raise
        except AssertionError:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_登陆功能.png')
            raise
        except Exception:
            d.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise
