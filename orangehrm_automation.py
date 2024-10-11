Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> from selenium.webdriver.common.by import By
>>> from selenium.webdriver.support.ui import WebDriverWait
>>> from selenium.webdriver.support import expected_conditions as EC
>>>
>>> # Configuración del navegador
>>> driver = webdriver.Chrome() 

DevTools listening on ws://127.0.0.1:52429/devtools/browser/470f7042-4e29-4e5d-969a-fa63134fb85f
>>>
>>> # Iniciar sesión en la página de OrangeHRM
>>> driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
>>> username_input = driver.find_element_by_name("username")
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    username_input = driver.find_element_by_name("username")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'WebDriver' object has no attribute 'find_element_by_name'
>>> password_input = driver.find_element_by_name("password")
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    password_input = driver.find_element_by_name("password")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'WebDriver' object has no attribute 'find_element_by_name'
>>> username_input.send_keys("admin")
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    username_input.send_keys("admin")
    ^^^^^^^^^^^^^^
NameError: name 'username_input' is not defined
>>> password_input.send_keys("admin")
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    password_input.send_keys("admin")
    ^^^^^^^^^^^^^^
NameError: name 'password_input' is not defined
>>> driver.find_element_by_xpath("//button[@type='submit']").click()
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    driver.find_element_by_xpath("//button[@type='submit']").click()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'
>>>
>>> # Esperar a que se cargue la página de inicio
>>> WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))
True
>>>
>>> # Dirigirse a la funcionalidad "Recruitment"
>>> driver.find_element_by_link_text("Recruitment").click()
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    driver.find_element_by_link_text("Recruitment").click()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'WebDriver' object has no attribute 'find_element_by_link_text'
>>>
>>> # Realizar el proceso de contratación de una persona
>>> driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'
>>> # Rellenar los formularios de contratación
>>> # ...
>>> # Validar que los datos de la persona correspondan a los diligenciados en los formularios y el estado sea contratad\o "Hired"Created TensorFlow Lite XNNPACK delegate for CPU.
