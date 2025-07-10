# Импортируем WebDriver для управления браузером
from selenium import webdriver

# Для настройки запуска Chrome (установка драйвера)
from selenium.webdriver.chrome.service import Service as ChromeService

# Для поиска элементов по типам (By.ID и т.д.)
from selenium.webdriver.common.by import By

# Автоматическая загрузка драйвера Chrome
from webdriver_manager.chrome import ChromeDriverManager


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запуск браузера в фоновом режиме (без графического интерфейса)
options.add_argument("--headless")

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
login_url = "https://www.saucedemo.com/inventory.html"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"
expecting_title = "Products"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод логина
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(valid_username)
print("Input login")

# Ввод пароля
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_password)
print("Input password")

# Клик по кнопке "Login"
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Получение текущего URL
current_url = driver.current_url
print(f"Current URL: {current_url}")

# Проверка соответствия ожидаемого URL
assert current_url == login_url, f"URL does not match. Expected: {login_url}, got: {current_url}"
print("URL correct")

# Поиск заголовка 'Products'
page_title = driver.find_element(By.XPATH, "//span[@class='title']").text
print(f"Page title: {page_title}")

# Проверка заголовка страницы
assert page_title == expecting_title, f"Titles does not match. Expected: {expecting_title}, got {page_title}"
print("Title correct")