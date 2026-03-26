class CheckoutInfoPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.zip_code_input = page.locator("[data-test='postalCode']")
        

        self.continue_button = page.locator("[data-test='continue']")

    def enter_shipping_info(self, first, last, zip_code):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()