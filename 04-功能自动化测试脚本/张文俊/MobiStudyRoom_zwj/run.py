import unittest
from cases.login import Login
from cases.look import Look
import HTMLTestReportCN
import time

suite = unittest.TestSuite()

suite.addTest(Login('test_case01'))
suite.addTest(Login('test_case02'))
suite.addTest(Look('test_case01'))
suite.addTest(Look('test_case02'))

ts = time.strftime('%Y%m%d_%H%M%S')
runner = HTMLTestReportCN.HTMLTestRunner(stream=open('./reports/report_%s.html' % ts, 'wb'),
                                          title='移动自习室APP自动化测试报告',
                                          description='本测试覆盖了移动自习室所有主要功能、主要流程',
                                          tester='张文俊')


runner.run(suite)
