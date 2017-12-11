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



def find_file(name, path):
    """Returns the path of a file in a directory"""

    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_selenium_server():
    """Returns the path of the 'standalone-server-standalone-x.x.x.jar' file."""

    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            try:
                if '-'.join(name.split('-')[:3]) == 'selenium-server-standalone':
                    return os.path.join(root, name)
            except IndexError:
                pass


def find_binary_file(name):
    """Returns the path of binary file in a given directory"""

    binary_path = None

    if sys.platform.startswith('win'):
        binary_path = find_file(name=name + '.exe', path=os.getcwd())
    elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        binary_path = find_file(name=name, path=os.getcwd())

    if binary_path:
        return binary_path
    else:
        print('[!] {name} not found in the working directory.'.format(name=name))


def start_selenium_server():
    """Starts the Java Standalone Selenium Server."""

    seleniumserver_path = find_selenium_server()
    if not seleniumserver_path:
        print('[!] The file "standalone-server-standalone-x.x.x.jar" not found.')
        return

    cmd = ['java', '-jar', seleniumserver_path]
    subprocess.Popen(cmd)


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
