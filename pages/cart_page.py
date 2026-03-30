from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_item_name = page.locator(".inventory_item_name")

    def click_checkout(self):
        self.checkout_button.click()