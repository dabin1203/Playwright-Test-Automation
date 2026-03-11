
from playwright.sync_api import sync_playwright, expect

# 동기(sync) 방식은 await를 쓰지 않습니다.
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    print("🌐 Sauce Demo로 이동합니다...")
    page.goto("https://www.saucedemo.com/")

    print("👤 로그인 정보를 입력합니다...")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
 
    page.locator("[data-test='inventory-item-name']").first.click()

    print("🛒 장바구니에 상품을 담습니다...")
    page.locator("#add-to-cart").click() 
    
    # 검증: Remove 버튼이 보이는지, 장바구니 숫자가 1인지 확인
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
  #  expect(page.locator(".shopping_cart_badge")).to_have_text("1")

"""
    print("📦 체크아웃을 진행합니다...")s
    page.locator("#shopping_cart_container").click() 
    expect(page.locator("#item_4_title_link")).to_have_text("Sauce Labs Backpack")
    page.locator("#checkout").click() 

    # 배송 정보 입력
    page.locator("#first-name").fill("Haeng-un")
    page.locator("#last-name").fill("Yusu")
    page.locator("#postal-code").fill("12345")
    page.locator("#continue").click()

    # 페이지 전환 검증
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    print("💰 마지막 결제 버튼을 누릅니다!")
    # [수정포인트] 동기 방식이므로 await를 삭제합니다.
    page.locator("#finish").click() 
        
    # 결과 확인
    # [수정포인트] expect 앞의 await도 삭제합니다.
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
        
    print("✅ 테스트 성공: 주문 완료 메시지를 확인했습니다!")
    
    browser.close()
    print("🏁 모든 테스트 프로세스가 대성공으로 종료되었습니다!")
"""




