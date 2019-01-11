from . import helper
from selenium import webdriver
from selenium.common.exceptions import WebDriverException



class BaseDriver:
    """Wrapper class around Selenium webdriver 

    Starts a Selenium webdriver according to the parameters provided.

    Parameters
    ----------
    headless : bool
        Whether to start the browser in headless mode.
    user_agent : str, optional
        The `user_agent` string the webdriver should use.
    profile_path : str, optional
        The path of the browser profile.

    Attributes
    ----------
    driver : Selenium webdriver object 
        Corresponding Selenium webdriver object, for example 
        `selenium.webdriver.Chrome` in the case of `ChromeDriver`. 
    headless : bool
        Whether to start the browser in headless mode, same as the
        `headless` constructor parameter.
    agent : str
        The `user_agent` string the webdriver should use, same as the
        `user_agent` constructor parameter. 
    user_agent : str
        The `user_agent` string the webdriver is actually using. If not same 
        as the `agent` parameter, there is a possible bug.
    profile_path : str
        The path of the browser profile.
    
    Methods
    -------
    start()
        Start the Selenium webdriver, populating the `driver` attribute.
    close()
        `quit` the webdriver.
    """
    def __init__(self, headless=False, user_agent=None, profile_path=None):
        self._driver = None
        self.headless = headless
        self.agent = user_agent
        self.profile_path = profile_path

    def start(self):
        pass

    @property
    def driver(self):
        if not self._driver:
            self.start()
        return self._driver
    
    @property
    def user_agent(self):
        if not self.driver:
            return self.agent
        try:
            agent = self.driver.execute_script('return navigator.userAgent')
        except WebDriverException:
            self.driver.get('http://www.google.com')
            agent = self.driver.execute_script('return navigator.userAgent')
        return agent

    def close(self):
        if not self.driver:
            return
        self.driver.quit()

    def __del__(self):
        self.close()


class ChromeDriver(BaseDriver):
    def start(self):
        options = webdriver.ChromeOptions()
        if self.agent:
            options.add_argument('user-agent={}'.format(self.agent))
        if self.profile_path:
            options.add_argument('user-data-dir={}'.format(self.profile_path))
        if self.headless:
            options.add_argument('--headless')
            
        # Disables notifications in the Chrome instance to be opened.
        options.add_argument('--disable-notifications')
        prefs = {'profile.default_content_setting_values.notifications': 2}
        options.add_experimental_option('prefs', prefs)

        chromedriver_path = helper.find_executable('chromedriver')
        if chromedriver_path:
            self._driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        else:
            self._driver = webdriver.Chrome(chrome_options=options)


class FirefoxDriver(BaseDriver):
    def start(self):
        profile = webdriver.FirefoxProfile(self.profile_path) if self.profile_path else webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        if self.agent:
            profile.set_preference('general.useragent.override', self.agent)
        if self.headless:
            options.add_argument('--headless')

        geckodriver_path = helper.find_executable('geckodriver')
        if geckodriver_path:
            self._driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path=geckodriver_path)
        else:
            self._driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options)
