"""
Standard and reliable module for starting up Selenium Webdriver, with custom user-agent and custom profiles.
"""

import drivers


def webdriver(name, incognito=False, user_agent=None, profile_path=None):
    """Starts and returns a Selenium Webdriver.

    Args:
        name (str): Name of the webdriver to be started [Chrome, Firefox, PhantomJs, HTMLUnit].
        user_agent (str): The user_agent string the webdriver should use.
        profile_path (str): The path of the browser profile [only for Firefox and Chrome].

    Returns:
        selenium.webdriver: A Selenium Webdriver according to the Args.
    """

    name = name.lower()

    if 'htmlunit' in name:
        return drivers.HTMLUnitDriver(incognito, user_agent, profile_path)
    elif 'chrome' in name:
        return drivers.ChromeDriver(incognito, user_agent, profile_path)
    elif 'firefox' in name:
        return drivers.FirefoxDriver(incognito, user_agent, profile_path)
    elif 'phantomjs' in name:
        return drivers.PhantomJSDriver(incognito, user_agent, profile_path)
