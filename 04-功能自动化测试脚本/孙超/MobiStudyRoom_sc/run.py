import unittest
import HTMLTestReportCN
import time
suite2 = unittest.defaultTestLoader.discover(start_dir='./cases/', pattern='*.py')
ts = time.strftime('%Y%m%d_%H%M%S')
runner2 = HTMLTestReportCN.HTMLTestRunner(stream=open('./reports/report_%s.html' % ts, 'wb'),
                                          title='移动自习室自动化测试报告',
                                          description='本测试覆盖了移动自习室所有主要功能、主要流程',
                                          tester='孙超')
runner2.run(suite2)







