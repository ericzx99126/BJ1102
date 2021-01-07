from appium import webdriver
from configparser import ConfigParser as CP

cp = CP()
cp.read(__file__ + '/../config/config.ini')
host = 'host1'
hp = cp.get(host, 'protocol')
name = cp.get(host, 'ip')
port = cp.get(host, 'port')
HOST = f'{hp}://{name}:{port}'

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62025"
caps["app"] = "E:\\apk\\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk"
caps["appPackage"] = "com.offcn.yidongzixishi"
caps["appActivity"] = "com.offcn.yidongzixishi.SplashActivity"
caps["noReset"] = False
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True

def open_app():
    driver = webdriver.Remote(f'{HOST}/wd/hub', caps)
    driver.implicitly_wait(5)
    return driver