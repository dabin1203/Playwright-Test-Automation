from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # step1 : login 
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    print("로그인 성공")

    # step2 : Add item to cart
    add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    print("장바구니 추가")
        
    browser.close()