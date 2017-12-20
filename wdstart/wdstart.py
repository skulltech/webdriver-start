"""
Standard and reliable module for starting up Selenium Webdriver, with custom user-agent and custom profiles.
"""

from . import drivers


def webdriver(name, incognito=False, user_agent=None, profile_path=None):
    """
    Starts and returns a wrapped Selenium Webdriver object.

    Starts a selenium webdriver according to the given specifications, 
    and returns an object of a wrapper class around Selenium. To learn 
    more about this wrapper class, refer to the docs of the `drivers` 
    module.

    Parameters
    ----------
        name : str
            Name of the webdriver to be started. Supported webdrivers 
            are Chrome, Firefox, PhantomJs and HTMLUnit.
        user_agent : str, optional
            The `user_agent` string the webdriver should use.
        profile_path : str, optional
            The path of the browser profile (only for Firefox and Chrome).

    Returns
    -------
        drivers.BaseDriver
            A object of a class inherited from `drivers.BaseDriver`, 
            such as `ChromeDriver`. This is a wrapper class around 
            selenium webdriver object. For details, refer to the docs 
            of the `drivers` module.
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
