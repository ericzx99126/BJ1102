from appium import webdriver
# from configparser import ConfigParser as CP

# cp = CP()
# cp.read(__file__ + '/../config/config.ini')
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:620025"
caps["app"] = "D:\\apk\\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk"
caps["appPackage"] = "com.offcn.yidongzixishi"
caps["appActivity"] = "com.offcn.yidongzixishi.SplashActivity"
caps["noReset"] = False
# host = 'host1'
# xy = cp.get(host,'protocol')
# ip = cp.get(host,'ip')
# port = cp.get(host,'port')
# HOST = f'{xy}://{ip}:{port}'
def open_browser():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(5)
    return driver

