import unittest
import time
from tools import open_browser
from appium.webdriver.common.touch_action import TouchAction
import sys

class Look(unittest.TestCase):
    '''浏览内容'''

    def setUp(self):
        br = open_browser()
        self.br = br
        self.cls_name = self.__class__.__name__

    def tearDown(self):
        time.sleep(2)
        self.br.quit()

    def test_case01(self):
        '''浏览行测内容'''
        br = self.br
        mtd_name = sys._getframe().f_code.co_name

        try:
            br.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys('17774020355')
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys('w6010009')
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_login').click()
            br.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
            time.sleep(2)
            TouchAction(br).tap(x=448, y=1168).perform()
            time.sleep(2)
            br.find_element_by_xpath('//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/book_user_item_item_tv" and @text="行测五大专项核心知识点"]').click()
            br.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/ziliaolist_item_name" and @text="第三章 判断推理"]').click()
            br.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/ziliaolist_item_name" and @text="155. [文章] 【智力推理】知识点介绍"]').click()
            show=br.find_element_by_id('com.offcn.yidongzixishi:id/tv_content')

            self.assertIn('智力推理',show.text,msg='显示内容不正确')

        except AssertionError:
           br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_显示内容不正确.png')
           raise
        except Exception:
           br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
           raise

    def test_case02(self):
        '''浏览19大报告'''
        br = self.br
        mtd_name = sys._getframe().f_code.co_name

        try:
            br.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys('17774020355')
            br.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys('w6010009')
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_login').click()
            br.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()
            time.sleep(2)
            TouchAction(br).tap(x=448, y=1168).perform()
            time.sleep(2)
            br.find_element_by_xpath('//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/book_user_item_item_tv" and @text="党的十九大报告核心考点及命题"]').click()
            br.find_element_by_xpath('//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/ziliaolist_item_name" and @text="第一章 报告电子版下载"]').click()
            br.find_element_by_xpath('//android.widget.TextView[@resource-id="com.offcn.yidongzixishi:id/ziliaolist_item_name" and @text="1. [资料] 党的十九大报告核心考点及命题"]').click()
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_download').click()
            time.sleep(2)
            br.find_element_by_id('com.offcn.yidongzixishi:id/btn_openwithotherapp').click()
            c=br.find_element_by_id('com.offcn.yidongzixishi:id/btn_openwithotherapp')
            r=c.is_displayed()
            self.assertEqual(r,False,msg='展示信息不正确')
        except AssertionError:
            br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_展示信息不正确.png')
            raise
        except Exception:
            br.save_screenshot(f'./pics/{self.cls_name}_{mtd_name}_其他错误.png')
            raise




