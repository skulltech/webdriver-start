from urllib.error import URLError
from urllib.request import urlopen

from . import helper
from selenium import webdriver as WD
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


class BaseDriver:
    def __init__(self, incognito=False, user_agent=None, profile_path=None):
        self.driver = None
        self.name = None
        self.incognito = incognito
        self.agent = user_agent
        self.profile_path = profile_path

    @property
    def user_agent(self):
        try:
            agent = self.driver.execute_script('return navigator.userAgent')
        except WebDriverException:
            self.driver.get('http://www.google.com')
            agent = self.driver.execute_script('return navigator.userAgent')
        return agent


class ChromeDriver(BaseDriver):
    def __init__(self, incognito=False, user_agent=None, profile_path=None):
        super().__init__(incognito, user_agent, profile_path)
        self.__start()

    def __start(self):
        self.name = 'Chrome'
        opt = Options()

        if self.agent:
            opt.add_argument('user-agent={}'.format(self.agent))
        if self.profile_path:
            opt.add_argument('user-data-dir={}'.format(self.profile_path))

        # Some enhancements to the WebDriver to be opened.
        opt.add_argument('--disable-notifications')
        prefs = {'profile.default_content_setting_values.notifications': 2}
        opt.add_experimental_option('prefs', prefs)

        chromedriver_path = helper.find_executable('chromedriver')
        if chromedriver_path:
            self.driver = WD.Chrome(chromedriver_path, chrome_options=opt)
        else:
            self.driver = WD.Chrome(chrome_options=opt)


class FirefoxDriver(BaseDriver):
    def __init__(self, incognito=False, user_agent=None, profile_path=None):
        super().__init__(incognito, user_agent, profile_path)
        self.__start()

    def __start(self):
        self.name = 'Firefox'
        if self.profile_path:
            fp = WD.FirefoxProfile(self.profile_path)
        else:
            fp = WD.FirefoxProfile()

        if self.agent:
            fp.set_preference('general.useragent.override', self.agent)

        geckodriver_path = helper.find_executable('geckodriver')
        if geckodriver_path:
            self.driver = WD.Firefox(firefox_profile=fp, executable_path=geckodriver_path)
        else:
            self.driver = WD.Firefox(firefox_profile=fp)


class HTMLUnitDriver(BaseDriver):
    def __init__(self, incognito=False, user_agent=None, profile_path=None):
        super().__init__(incognito, user_agent, profile_path)
        self.__start()
        
    def __start(self):
        self.name = 'HTMLUnit'
        try:
            urlopen('http://localhost:4444/wd/hub/status')
        except URLError:
            helper.start_selenium_server()
        self.__wait_for_server()

        dcap = WD.DesiredCapabilities.HTMLUNITWITHJS
        if self.user_agent:
            dcap['version'] = self.user_agent

        self.driver = WD.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=dcap)

    def __wait_for_server(self):
        while True:
            try:
                urlopen('http://localhost:4444/wd/hub/status')
            except URLError:
                time.sleep(0.1)
            else:
                break


class PhantomJSDriver(BaseDriver):
    def __init__(self, incognito=False, user_agent=None, profile_path=None):
        super().__init__(incognito, user_agent, profile_path)
        self.__start()
        
    def __start(self):
        self.name = 'PhantomJS'
        dcap = WD.DesiredCapabilities.PHANTOMJS
        if self.agent:
            dcap['version'] = self.agent

        phantomjs_path = helper.find_executable('phantomjs')
        if phantomjs_path:
            self.driver = WD.PhantomJS(phantomjs_path, desired_capabilities=dcap)
        else:
            self.driver = WD.PhantomJS(desired_capabilities=dcap)
