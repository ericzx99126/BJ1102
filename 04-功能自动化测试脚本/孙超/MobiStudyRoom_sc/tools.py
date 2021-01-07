from appium import webdriver
from configparser import ConfigParser as CP

cp = CP()
cp.read(__file__ + '/../config/config.ini')
host = 'host1'
xy = cp.get(host,'protocol')
ip = cp.get(host,'ip')
port = cp.get(host,'port')
HOST = f'{xy}://{ip}:{port}'
def open_browser():
    caps ={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62026",
  "app": "E:\\apk\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk",
  "appPackage": "com.offcn.yidongzixishi",
  "appActivity": "com.offcn.yidongzixishi.SplashActivity",
  "noReset": False,
  "unicodeKeyboard": True,
  "resetKeyboard": True
}
    driver = webdriver.Remote('%s/wd/hub' % HOST,caps)
    driver.implicitly_wait(5)
    return driver

