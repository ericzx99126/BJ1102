import unittest
import HTMLTestReportCN
import time
from cases.login import Login
from cases.exam import Exam
from cases.subject import Subject
from cases.save import Save


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(Exam))
suite.addTest(unittest.makeSuite(Subject))
suite.addTest(unittest.makeSuite(Save))

ts = time.strftime('%H%M%S')
runner = HTMLTestReportCN.HTMLTestRunner(stream=open('./reports/report_%s.html' % ts, 'wb'),
                                         title='APP自动化测试报告',
                                         description='本次测试包含了MobiStudyRoom的几个主要功能',
                                         tester='王子')

runner.run(suite)
