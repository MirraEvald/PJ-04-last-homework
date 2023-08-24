from datetime import time
from selenium import *
from pages.base_page import URL
from pages.form_page import FormPage


class TestFormPage:
    # Страница успешно открывается
    def test_form(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()


    # позитивный тест формы регистрации с корректными данными (имя,фамилия, почта, пароль, подтверждение пароля)
    def test_form(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.fill_fields_and_submit()

    # Негативный тест с пробелами в заполняемых полях
    def test_negative_empty_form(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.faild_way()

    # Негативный тест с одним символом в поле пароль
    def test_negative_one_symbol(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.password_one_symbol()

    # Негативный тест с валидными имененем, фамилией, почтой и не совпадающими паролями
    def test_negative_form(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.next_faild_way()

    # позитивный тест авторизации с валидными данными
    def test_sucsess_login(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.sucsess_login()

    # негативный тест авторизации с пустыми полями ввода
    def test_unsucsess_login(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.unsucsess_login()

    # негативный тест авторизации с введенными данными в верхнем регистре
    def test_upper_login(self, driver):
        form_page = FormPage(driver, URL)
        form_page.open()
        form_page.upper_login()
