from page_objects.locators import SignInPageLocators
from page_objects.locators import RegistrationPageLocators


class SignInPage():

    def __init__(self, driver):
        self.driver = driver
        # locators:
        self.sign_in_link = SignInPageLocators.sign_in_link
        self.create_email_input = SignInPageLocators.create_email_input
        self.create_button = SignInPageLocators.create_button
        self.sign_in_email_input = SignInPageLocators.sign_in_email_input
        self.sign_in_passwd_input = SignInPageLocators.sign_in_passwd_input
        self.sign_in_button = SignInPageLocators.sign_in_button
        self.register_button = RegistrationPageLocators.register_button

    def open_sign_in_page(self):
        self.driver.get("http://automationpractice.com")
        self.driver.find_element(*self.sign_in_link).click()

    def open_registration_form(self, email):
        self.driver.find_element(*self.create_email_input).send_keys(email)
        self.driver.find_element(*self.create_button).click()

    def is_register_button(self):
        return self.driver.find_element(*self.register_button).is_displayed()

    def log_in(self, email, passwd):
        self.driver.find_element(*self.sign_in_email_input).send_keys(email)
        self.driver.find_element(*self.sign_in_passwd_input).send_keys(passwd)
        self.driver.find_element(*self.sign_in_button).click()