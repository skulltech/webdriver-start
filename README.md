# webdriver-start
Reliable module for starting up Selenium Webdriver, with custom user-agent and user-profile

## Installation
Install it using pip: `pip install webdriver-start`

## Usage
```python
import wdstart
driver = wdstart.start_webdriver('Chrome', user_agent='Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19(KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19', profile_path='C:\Users\SkullTech\AppData\Local\Google\Chrome\User Data')
```
