from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

def test_invalid_login_wrong_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login("standard_user", "wrong_password123")
    
    expect(login_page.error_message_locator).to_be_visible()
    
    error_text = login_page.get_error_message_text()
    assert "Epic sadface" in error_text