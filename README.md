# webdriver-start
Reliable module for starting up Selenium Webdriver, with custom user-agent and user-profile

## Installation
Install it using pip: `pip install webdriver-start`

## Usage
```python
>>> from wdstart import wdstart
>>> driver = wdstart.webdriver('Chrome', user_agent='Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19(KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19')
>>> driver.driver
<selenium.webdriver.chrome.webdriver.WebDriver (session="46157cffe549da015b288cdabea94a29")>
>>> driver.driver.get('http://www.google.com')
>>> driver.driver.title
'Google'
>>> driver.user_agent
'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19(KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
```
