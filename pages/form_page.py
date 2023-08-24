import time
from locators.form_page_locators import FormPageLocators as Locators
from pages.base_page import BasePage


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'Mirra'
        last_name = 'Evald'
        email = 'mirra.evald+test@gmail.com'
        password = 'JHg76fjshgf9892'
        password_confirm = 'JHg76fjshgf9892'
        self.element_is_visible(Locators.REG_LINK).click()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.PASSWORD_CONFIRM).send_keys(password_confirm)
        self.element_is_visible(Locators.REGISTER_BUTTON).click()

        time.sleep(5)

    def faild_way(self):
        first_name = ' '
        last_name = ' '
        email = ' '
        password = ' '
        password_confirm = ' '
        self.element_is_visible(Locators.REG_LINK).click()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.PASSWORD_CONFIRM).send_keys(password_confirm)
        self.element_is_visible(Locators.REGISTER_BUTTON).click()

        time.sleep(5)

    def password_one_symbol(self):
        first_name = 'Mirra'
        last_name = 'Evald'
        email = 'mirra.evald+test@gmail.com'
        password = 'U'
        password_confirm = 'U'
        self.element_is_visible(Locators.REG_LINK).click()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.PASSWORD_CONFIRM).send_keys(password_confirm)
        self.element_is_visible(Locators.REGISTER_BUTTON).click()

        time.sleep(5)

    def next_faild_way(self):
        first_name = 'Mirra'
        last_name = 'Evald'
        email = 'mirra.evald+test@gmail.com'
        password = 'hdgfyYrda798790'
        password_confirm = 'dhgPfy765'
        self.element_is_visible(Locators.REG_LINK).click()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.PASSWORD_CONFIRM).send_keys(password_confirm)
        self.element_is_visible(Locators.REGISTER_BUTTON).click()

        time.sleep(5)

    def sucsess_login(self):
        email = 'mirra.evald+test@gmail.com'
        password = 'JHg76fjshgf9892'
        self.element_is_visible(Locators.LOGIN_EMAIL).send_keys(email)
        self.element_is_visible(Locators.LOGIN_PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()

    time.sleep(5)

    def unsucsess_login(self):
        email = ''
        password = ''
        self.element_is_visible(Locators.LOGIN_EMAIL).send_keys(email)
        self.element_is_visible(Locators.LOGIN_PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()

    time.sleep(5)

    def upper_login(self):
        email = 'MIRRA.EVALD+TEST@GMAIL.COM'
        password = 'jh76FJSHGF9892'
        self.element_is_visible(Locators.LOGIN_EMAIL).send_keys(email)
        self.element_is_visible(Locators.LOGIN_PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()

    time.sleep(5)


