from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import math
from selenium.webdriver.support.ui import Select
# Укажите путь к ChromeDriver
chromedriver_path = 'F:/Chromedriver123-0-6312-122/chromedriver.exe'

# Укажите путь к исполняемому файлу Opera GX
opera_executable_path = 'C:/Users/kiril/AppData/Local/Programs/Opera GX/launcher.exe'

# Настройки для Opera GX
options = Options()
options.binary_location = opera_executable_path

options.add_argument('--side-profile-name=33363838345F31383136323831353735')
options.add_argument('--side-profile-no-gx-sounds')
options.add_argument('--side-profile-muted')
options.add_argument('--with-feature:side-profiles')
options.add_argument('--incognito')
# Добавьте аргументы командной строки
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
#options.add_argument('--disable-gpu')
options.add_argument('--disable-usage-statistics-question')
options.add_argument('--no-default-browser-check')



# Создайте сервис для ChromeDriver
service = Service(chromedriver_path)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    browser = webdriver.Chrome(options=options, service=service)
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    button =  browser.find_element(By.ID, "button")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    
    browser.quit()