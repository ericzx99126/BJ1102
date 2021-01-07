import unittest
import HTMLTestReportCN as HTR
import time

# 自动识别并装载用例
suite = unittest.defaultTestLoader.discover(start_dir='./cases/', pattern='case*.py')

# 创建执行器
ts = time.strftime('%m%d_%H%M%S')

runner = HTR.HTMLTestRunner(stream=open(f'./reports/report_{ts}.html', 'wb'),
							title='MobiStudyRoom自动化测试报告',
							description='本测试覆盖了MobiStudyRoom所有主要功能和流程',
							tester='Holly')

# 使用执行器 执行用例集合
runner.run(suite)


