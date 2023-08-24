from selenium.webdriver.common.by import By


class FormPageLocators:
    REG_LINK = (By.CSS_SELECTOR, "#kc-register")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.CSS_SELECTOR, '#address')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#password-confirm')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.rt-btn--orange')
    LOGIN_EMAIL = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'kc-login')