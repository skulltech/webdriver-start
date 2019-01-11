# webdriver-start
Reliable module for starting up Selenium Webdriver with custom modifications. Supports —
- Custom `user-agent`
- Custom user profile.
- Headless mode.
- Firefox and Chrome webdrivers. Open an issue if you want support for more.


## Installation
Install it using pip —

```console
$ pip install webdriver-start
```

## Usage

For Chrome
```python
>>> from wdstart import webdriver
>>> driver = webdriver.Chrome(headless=True, user_agent='this is a custom user-agent', user_profile='/path/to/profile/')
>>> driver
<selenium.webdriver.chrome.webdriver.WebDriver (session="46157cffe549da015b288cdabea94a29")>
>>> driver.get('http://www.google.com')
>>> driver.title
'Google'
>>> driver.execute_script('return navigator.userAgent')
'this is a custom user-agent'
```

Similarly, for Firefox
```python
>>> from wdstart import webdriver
>>> driver = webdriver.Firefox(headless=True, user_agent='this is a custom user-agent', user_profile='/path/to/profile/')
>>> driver
<selenium.webdriver.chrome.webdriver.WebDriver (session="46157cffe549da015b288cdabea94a29")>
>>> driver.get('http://www.google.com')
>>> driver.title
'Google'
>>> driver.execute_script('return navigator.userAgent')
'this is a custom user-agent'
```
