from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_add_backpack_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.go_to_cart()
    
    assert cart_page.cart_item_name.inner_text() == "Sauce Labs Backpack"
    
    cart_page.click_checkout()

    info_page = CheckoutInfoPage(page)
    
    info_page.enter_shipping_info("Dabin", "Lee", "12345")
    
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    overview_page = CheckoutOverviewPage(page)
    expect(overview_page.total_label).to_contain_text("Total:")
    overview_page.click_finish()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    complete_page = CheckoutCompletePage(page)
    expect(complete_page.complete_header).to_have_text("Thank you for your order!")