import unittest
import time
from tools import open_browser
from appium.webdriver.common.touch_action import TouchAction
import sys

class Login(unittest.TestCase):
    '''登录'''

    def setUp(self):
        br = open_browser()
        self.br = br
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        time.sleep(2)
        self.br.quit()

    def test_case01(self):
        '''正确的账号密码登录'''
        br = self.br
        mtd_name = sys._getframe().f_code.co_name

        try:
            br.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys('17774020355')
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys('w6010009')
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_login').click()
            choice=br.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
            s=choice.is_displayed()
            self.assertTrue(s,msg='登录失败')

        except AssertionError:
           br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_登录失败.png')
           raise
        except Exception:
           br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
           raise

    def test_case02(self):
        '''登录-退出登陆'''
        br = self.br
        mtd_name = sys._getframe().f_code.co_name
        keys='17774020355'
        try:
            br.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys(f'{keys}')
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys('w6010009')
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_login').click()
            br.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
            time.sleep(2)
            TouchAction(br).tap(x=448, y=1168).perform()
            time.sleep(2)
            br.find_element_by_id("com.offcn.yidongzixishi:id/iv_mine").click()
            br.find_element_by_id("com.offcn.yidongzixishi:id/mineSettting").click()
            br.find_element_by_id("com.offcn.yidongzixishi:id/loginOut").click()
            user=br.find_element_by_id('com.offcn.yidongzixishi:id/et_phone')
            self.assertIn(keys, user.text,msg='退出登陆失败')
        except AssertionError:
            br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_退出登陆失败.png')
            raise
        except Exception:
            br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise




