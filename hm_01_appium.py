from appium import webdriver
desired_caps = dict()
# 平台名字
desired_caps['platformName'] = 'Android'
# 平台版本
desired_caps['platformVersion'] = '5.1'
# 设备名
desired_caps['deviceName'] = '192.168.56.101:5555'
# 包名
desired_caps['appPackage'] = 'com.android.settings'
# 界面名/启动名
desired_caps['appActivity'] = '.Settings'
# 默认输入中文无效，需要这两行代码
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 因为appium每次启动应用时都会"重置应用"，才会出现本地保存，若不想重置，可直接在启动参数加一行代码
desired_caps['noReset'] = True
# 使用uiautomator2框架
desired_caps['automationName'] = 'Uiautomator2'
# 链接不同的手机 手机的设备号
desired_caps['udid'] = '192.168.49.101:5555'
# driver对象 填入服务器地址和端口号 链接appium
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.quit()