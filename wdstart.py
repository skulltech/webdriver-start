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

import drivers



def webdriver(name, user_agent=None, profile_path=None):
    """Starts and returns a Selenium Webdriver.

    Args:
        name (str): Name of the webdriver to be started [Chrome, Firefox, PhantomJs, HTMLUnit].
        user_agent (str): The user_agent string the webdriver should use.
        profile_path (str): The path of the browser profile [only for Firefox and Chrome].

    Returns:
        selenium.webdriver: A Selenium Webdriver according to the Args.
    """

    if name == 'htmlunit':
        return drivers.HTMLUnitDriver()

    if name == 'firefox':
        return drivers.FirefoxDriver()

    if name == 'chrome':
        return drivers.ChromeDriver()

    if name == 'phantomjs':
        return drivers.PhantomJSDriver()
