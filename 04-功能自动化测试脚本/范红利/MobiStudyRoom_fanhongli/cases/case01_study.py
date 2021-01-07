import time
import unittest
from tools import open_app


class Study(unittest.TestCase):
	'''学习模块'''
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
		'''添加考试科目'''
		driver = self.driver
		try:
			# test_case01  添加考试科目
			# 添加考试
			driver.find_element_by_id('com.offcn.yidongzixishi:id/tv_type').click()
			driver.find_element_by_id('com.offcn.yidongzixishi:id/iv_head_commit').click()
			driver.find_elements_by_id('com.offcn.yidongzixishi:id/llExam')[3].click()
			# 保存
			driver.find_element_by_id('com.offcn.yidongzixishi:id/headRight').click()
			# 断言
			xds = driver.find_elements_by_id('com.offcn.yidongzixishi:id/examName')[1].text
			self.assertTrue(xds == '选调生', msg='添加考试失败')
		except AssertionError:
			driver.save_screenshot('./pics/添加考试失败.png')
			raise
		except Exception:
			driver.save_screenshot('./pics/其他错误.png')
			raise


if __name__ == '__main__':
	unittest.main()





