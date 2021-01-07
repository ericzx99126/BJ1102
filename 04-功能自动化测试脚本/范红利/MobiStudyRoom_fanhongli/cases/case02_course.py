import time
import unittest
from tools import open_app


class Study(unittest.TestCase):
	'''课程模块'''
	def setUp(self):
		driver = open_app()
		# 点击跳过
		driver.find_element_by_id('com.offcn.yidongzixishi:id/skip').click()
		# 输入手机号和密码
		driver.find_element_by_id('com.offcn.yidongzixishi:id/et_phone').send_keys('17882559887')
		driver.find_element_by_id('com.offcn.yidongzixishi:id/et_pwd').send_keys('123456Fhl')
		# 点击立即登录
		driver.find_element_by_class_name('android.widget.Button').click()
		time.sleep(3)
		# 选择国家公务员
		driver.find_element_by_xpath('//android.widget.TextView[@text="国家公务员"]').click()
		time.sleep(2)
		# 点击不升级
		driver.find_element_by_id('com.offcn.yidongzixishi:id/cancel').click()
		self.driver = driver

	def tearDown(self):
		time.sleep(2)
		self.driver.quit()

	def test_case01(self):
		'''收藏课程'''
		driver = self.driver
		try:
			# test_case02 收藏课程
			driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_coach').click()
			driver.find_element_by_xpath('//android.widget.RelativeLayout'
										 '[@resource-id="com.offcn.yidongzixishi:id/rl_root" and @index="1"]').click()
			# 点击收藏
			driver.find_element_by_id('com.offcn.yidongzixishi:id/toolbar_collect').click()
			time.sleep(2)
			# 返回
			driver.find_element_by_id('com.offcn.yidongzixishi:id/back_btn').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_mine').click()
			# 查看收藏目录
			driver.find_element_by_xpath('//android.widget.RelativeLayout[@index="6"]').click()
			kc = driver.find_element_by_id('com.offcn.yidongzixishi:id/courseTitle').text
			# 断言
			self.assertTrue('2020版新疆公务员考试' in kc, msg='收藏失败')
		except AssertionError:
			driver.save_screenshot('./pics/收藏失败.png')
			raise
		except Exception:
			driver.save_screenshot('./pics/其他错误.png')
			raise

	def test_case02(self):
		'''课程筛选'''
		driver = self.driver
		try:
			# test_case03 课程筛选
			driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_coach').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/tvArea').click()
			# 选择价格100-499
			driver.find_element_by_xpath('//android.widget.TextView[@text="￥ 100-499" and @index="6"]').click()
			# 点击确定
			driver.find_element_by_id('com.offcn.yidongzixishi:id/btn_yes').click()
			# 定位价格
			prices = driver.find_elements_by_id('com.offcn.yidongzixishi:id/coursePrice')
			lst = []
			for i in prices:
				a = i.text
				lst.append(float(a[1:]))
			# 断言
			self.assertTrue(min(lst) >= 100 and max(lst) <= 499, msg='价格不在筛选范围内')
		except AssertionError:
			driver.save_screenshot('./pics/价格不在筛选范围内.png')
			raise
		except Exception:
			driver.save_screenshot('./pics/其他错误.png')
			raise

	def test_case03(self):
		'''课程价格正序排序'''
		driver = self.driver
		try:
			# test_case04 课程排序
			driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_coach').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/tvSort').click()
			# 点击价格正序
			driver.find_element_by_xpath('//android.widget.TextView[@text="价格正序"]').click()
			# 定位价格
			prices = driver.find_elements_by_id('com.offcn.yidongzixishi:id/coursePrice')
			lst = []
			for i in prices:
				a = i.text
				lst.append(float(a[1:]))
			lst2 = lst
			lst2.sort()
			# 断言
			self.assertTrue(lst2 == lst, msg='课程排序错误')
		except AssertionError:
			driver.save_screenshot('./pics/课程排序错误.png')
			raise
		except Exception:
			driver.save_screenshot('./pics/其他错误.png')
			raise


if __name__ == '__main__':
	unittest.main()


