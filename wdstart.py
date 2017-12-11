"""
Standard and reliable module for starting up Selenium Webdriver, with custom user-agent and custom profiles.
"""

import os
import subprocess
import sys
from urllib.request import urlopen
from urllib.error import URLError

from selenium import webdriver as WD
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options



def webdriver(name, user_agent=None, profile_path=None):
    """Starts and returns a Selenium Webdriver.

    Args:
        name (str): Name of the webdriver to be started [Chrome, Firefox, PhantomJs, HTMLUnit].
        user_agent (str): The user_agent string the webdriver should use.
        profile_path (str): The path of the browser profile [only for Firefox and Chrome].

    Returns:
        selenium.webdriver: A Selenium Webdriver according to the Args.
    """

    name = name.lower()
    driver = None

    if name == 'htmlunit':
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
        driver = WD.Remote(command_executor="http://localhost:4444/wd/hub",
                                  desired_capabilities=dcap)

    if name == 'firefox':
        if profile_path:
            fp = WD.FirefoxProfile(profile_path)
        else:
            fp = WD.FirefoxProfile()

        if user_agent:
            fp.set_preference('general.useragent.override', user_agent)

        driver = WD.Firefox(fp)

    if name == 'chrome':
        opt = Options()
        if user_agent:
            opt.add_argument('user-agent={user_agent}'.format(user_agent=user_agent))
        if profile_path:
            opt.add_argument('user-data-dir={profile_path}'.format(profile_path=profile_path))

        opt.add_argument("--disable-notifications")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        opt.add_experimental_option("prefs", prefs)

        chromedriver_path = find_binary_file('chromedriver')
        if chromedriver_path:
            driver = WD.Chrome(chromedriver_path, chrome_options=opt)
        else:
            driver = WD.Chrome(chrome_options=opt)

    if name == 'phantomjs':
        dcap = DesiredCapabilities.PHANTOMJS
        if user_agent:
            dcap["phantomjs.page.settings.userAgent"] = user_agent

        phantomjs_path = find_binary_file('phantomjs')
        if phantomjs_path:
            driver = WD.PhantomJS(phantomjs_path, desired_capabilities=dcap)
        else:
            driver = WD.PhantomJS(desired_capabilities=dcap)

    return driver
