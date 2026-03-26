class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.add_to_cart_btn.click()

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()    