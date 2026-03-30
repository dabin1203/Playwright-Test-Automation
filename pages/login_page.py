from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pw):
        self.username_input.fill(user)
        self.password_input.fill(pw)
        self.login_button.click()

    @property
    def error_message_locator(self):
        return self.page.locator("[data-test='error']")

    def get_error_message_text(self):
        return self.error_message_locator.inner_text()    