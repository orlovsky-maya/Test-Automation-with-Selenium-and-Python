# One browser is created with scope="class" in the browser fixture

# Command: pytest -s -v 4_Testing_with_PyTest/test_fixture4.py


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")