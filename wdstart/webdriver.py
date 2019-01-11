"""
Standard and reliable module for starting up Selenium Webdriver, with custom user-agent and custom profiles.
"""

from . import drivers



def Chrome(headless=False, user_agent=None, profile_path=None):
    """
    Starts and returns a Selenium webdriver object for Chrome.

    Starts a Selenium webdriver according to the given specifications, 
    and returns the corresponding `selenium.webdriver.Chrome` object.

    Parameters
    ----------
    headless : bool
        Whether to start the browser in headless mode.
    user_agent : str, optional
        The `user_agent` string the webdriver should use.
    profile_path : str, optional
        The path of the browser profile (only for Firefox and Chrome).

    Returns
    -------
    `selenium.webdriver.Chrome`
        Selenium webdriver, according to the given specifications.
    """
    chromedriver = drivers.ChromeDriver(headless, user_agent, profile_path)
    return chromedriver.driver


def Firefox(headless=False, user_agent=None, profile_path=None):
    """
    Starts and returns a Selenium webdriver object for Firefox.

    Starts a Selenium webdriver according to the given specifications, 
    and returns the corresponding `selenium.webdriver.Chrome` object.

    Parameters
    ----------
    headless : bool
        Whether to start the browser in headless mode.
    user_agent : str, optional
        The `user_agent` string the webdriver should use.
    profile_path : str, optional
        The path of the browser profile (only for Firefox and Chrome).

    Returns
    -------
    `selenium.webdriver.Firefox`
        Selenium webdriver, according to the given specifications.
    """
    firefoxdriver = drivers.FirefoxDriver(headless, user_agent, profile_path)
    return firefoxdriver.driver
