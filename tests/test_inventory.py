from playwright.sync_api import expect
from pages.login_page import LoginPage       
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

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