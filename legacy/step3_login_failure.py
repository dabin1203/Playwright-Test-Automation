from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # step1 : login 
    page.goto("https://www.saucedemo.com/")

    # step2 : Login failure test (Invalid ID/PW)
    page.fill("#user-name", "non-standard_user")
    page.fill("#password", "non-standard_sauce")
    page.click("#login-button")

    # step3 : Assert Error Message
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("Username and password do not match")
        
    print("테스트 완료: 로그인 실패 에러 메시지 검증 성공")
    browser.close()