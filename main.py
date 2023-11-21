import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class ADriver:

    def __init__(self, url_page):
        self.url_page = url_page

    def search_and_show(self, n: str):
        itog = set()
        # Программа выведет:
        driver = webdriver.Chrome()
        driver.get(self.url_page)  # загружаем страницу с поиском авто по категориям
        assert "Купить авто" in driver.title  # регистрируем текстовое поле и имитируем ввод строки "Купить авто"
        search = driver.find_element(By.CLASS_NAME, "input-input-Zpzc1")
        search.send_keys(n)
        open_search = driver.find_element(By.CLASS_NAME, "desktop-15w37ob")
        open_search.click()
        time.sleep(10)  # ставим на паузу, чтобы страница прогрузилась
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # загружаем страницу и извлекаем ссылки через атрибут class
        all_publications2 = \
            soup.find_all('a', {'class': 'iva-item-sliderLink-uLz1v'})
        print(len(all_publications2))
        # форматируем результат
        for article in all_publications2:
            obj_i = "https://www.avito.ru" + article['href']
            itog.add(obj_i)
        for index, value in enumerate(itog):
            print(f'{index}:{value}')


first_test = ADriver("https://www.avito.ru/all/avtomobili?cd=1")
first_test.search_and_show("audi a5")


