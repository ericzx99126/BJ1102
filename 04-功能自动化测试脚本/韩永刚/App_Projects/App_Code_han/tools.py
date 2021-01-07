from selenium import webdriver
from configparser import ConfigParser as CP

#配置抽离
HOST = "http://localhost:4723/wd/hub"

# cp = CP()
# cp.read(__file__ + '/../config/config.ini')
# host = 'host1'
# xy = cp.get(host,'protocol')
# ip = cp.get(host,'ip')
# port = cp.get(host,'port')

# HOST = f'{xy}://{ip}:{port}'
# print(HOST)

# def open_app():
#     br = webdriver.Chrome()
#     br.implicitly_wait(5)
#     br.maximize_window()
#     return br

