from urllib.request import urlopen
from urllib.error import URLError

from selenium import webdriver as WD
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options



class BaseDriver:
	def __init__(self, incognito=False, user_agent=None, profile_path=None):
		self.driver = None
		self.name = None
		self.incognito = incognito
		self.user_agent = user_agent
		self.profile_path = profile_path

    @property
    def user_agent(self):
        return self.driver.execute_script("return navigator.userAgent")

	def __start(self):
		pass


class ChromeDriver(BaseDriver):
	def __start(self, name, incognito=False, user_agent=None, profile_path=None):
        opt = Options()

        if user_agent:
            opt.add_argument('user-agent={}'.format(user_agent))
        if profile_path:
            opt.add_argument('user-data-dir={}'.format(profile_path))

        # Some enhancements to the webdriver to be opened.
        opt.add_argument('--disable-notifications')
        prefs = {'profile.default_content_setting_values.notifications': 2}
        opt.add_experimental_option('prefs', prefs)

        driver_path = find_binary_file('chromedriver')
        self.driver_path = driver_path or '$PATH'
        if driver_path:
            self.driver = WD.Chrome(driver_path, chrome_options=opt)
        else:
            self.driver = WD.Chrome(chrome_options=opt)


class FirefoxDriver(BaseDriver):
    def __start(self, name, incognito=False, user_agent=None, profile_path=None):
        if self.profile_path:
            fp = WD.FirefoxProfile(self.profile_path)
        else:
            fp = WD.FirefoxProfile()

        if self.user_agent:
            fp.set_preference('general.useragent.override', user_agent)

        self.driver = WD.Firefox(fp)


class HTMLUnitDriver(BaseDriver):
	def __start(self):
        while True:
            try:
                urlopen('http://localhost:4444/wd/hub/status')
            except URLError:
                start_selenium_server()
            else:
                break

        if user_agent:
            pass
        dcap = WD.DesiredCapabilities.HTMLUNITWITHJS
        driver = WD.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=dcap)


class PhantomJSDriver(BaseDriver):
	def __start(self):
        dcap = DesiredCapabilities.PHANTOMJS
        if self.user_agent:
            dcap["phantomjs.page.settings.userAgent"] = user_agent

        phantomjs_path = find_binary_file('phantomjs')
        if phantomjs_path:
            self.driver = WD.PhantomJS(phantomjs_path, desired_capabilities=dcap)
        else:
            self.driver = WD.PhantomJS(desired_capabilities=dcap)
