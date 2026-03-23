from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # step1 : login 
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    print("로그인 성공")

    # step2 :   Add Product & Go to Cart
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")

    print("장바구니 상품 추가 후, 장바구니 이동")

    # step3 : Checkout: Information Input
    
    page.click("#checkout")
    page.fill("#first-name", "Dabin")
    page.fill("#last-name", "Tester")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    print("배송 정보 입력 완료")

    # step4 : Final Overview & Finish
    page.click("#finish")

    print("최종 결제 버튼 클릭")

    # step5 : Assert Checkout Complete (Core Point!)
    complete_header = page.locator(".complete-header")
    expect(complete_header).to_contain_text("Thank you for your order")


    print("로그인부터 최종 결제 완료까지 전체 프로세스 검증 성공")
    browser.close()