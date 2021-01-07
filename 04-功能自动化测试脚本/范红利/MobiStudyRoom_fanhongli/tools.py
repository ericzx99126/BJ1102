from appium import webdriver


def open_app():
	caps = {
		"platformName": "Android",
		"platformVersion": "5.1.1",
		"deviceName": "127.0.0.1:62025",
		"app": "E:\\tool\\app自动化测试工具\\apk\\com.offcn.yidongzixishi_4.6.1_liqucn.com.apk",
		"appPackage": "com.offcn.yidongzixishi",
		"appActivity": "com.offcn.yidongzixishi.SplashActivity",
		"noReset": False,
		"unicodeKeyboard": True,
		"resetKeyboard": True
	}
	driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
	driver.implicitly_wait(5)
	return driver

