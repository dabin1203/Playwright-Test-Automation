from playwright.sync_api import Page

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("[data-test=finish]")

    def click_finish(self):
        self.finish_button.click()