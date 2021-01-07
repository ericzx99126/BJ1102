import time
import unittest
from tools import open_app


class Study(unittest.TestCase):
	'''题库模块'''
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

	def test_case(self):
		'''交卷'''
		driver = self.driver
		try:
			# test_case05 交卷
			driver.find_element_by_id('com.offcn.yidongzixishi:id/rl_test').click()
			driver.find_element_by_xpath('//android.widget.TextView[@text="专项练习"]').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/llSelectQuestion').click()
			# 提交试卷
			driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_head_submit_error').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_submit').click()
			qn = driver.find_element_by_id('com.offcn.yidongzixishi:id/questionNum').text
			# 断言
			self.assertTrue('总题量' in qn and '答对' in qn, msg='交卷失败')
		except AssertionError:
			driver.save_screenshot('./pics/交卷失败.png')
			raise
		except Exception:
			driver.save_screenshot('./pics/其他错误.png')
			raise


if __name__ == '__main__':
	unittest.main()






