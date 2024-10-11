Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from behave import given, when, then
>>> from selenium import webdriver
>>>
>>> @given("I am on the OrangeHRM login page")
... def navigate_to_login_page(context):
...         context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth
