import unittest
from cases.login import Login
import HTMLTestReportCN
import time

# 创建用例容器
suite = unittest.TestSuite()

# 向容器中装载用例
# 第一种：基本装载方式：逐个装载
suite.addTest(Login('test_case01'))
# suite.addTest(Login('test_case02'))
# suite.addTest(Login('test_case03'))
# suite.addTest(SearchGoods('test_case01'))
# suite.addTest(SearchGoods('test_case02'))

# 第二种：以类为单位装载
# Python3.8以下支持
# suite.addTest(unittest.makeSuite(Login))
# suite.addTest(unittest.makeSuite(SearchGoods))

# 第三种：自动识别、自动装载
# 使用unittest模块下的defaultTestLoader工具
# suite2 = unittest.defaultTestLoader.discover(start_dir='./cases/', pattern='*.py')

# 创建执行器
# runner = unittest.TextTestRunner()

ts = time.strftime('%Y%m%d_%H%M%S')

runner2 = HTMLTestReportCN.HTMLTestRunner(stream=open('./reports/report_%s.html' % ts, 'wb'),
                                          title='iWebShop自动化测试报告',
                                          description='本测试覆盖了iWebShop所有主要功能、主要流程',
                                          tester='大明')

# 使用执行器执行用例集合
# runner.run(suite)
# runner.run(suite2)
# runner2.run(suite2)
runner2.run(suite)
