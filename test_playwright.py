from playwright.sync_api import Playwright


def test_buy_stuff (playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context() # doesnt share cookies, cache, local storage
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    #page.get_by_placeholder("email@example.com").fill("test")
    page.locator("#userEmail").fill("jond33t@gmail.com")
    page.locator("#userPassword").fill("Asdfjkl1!")
    page.get_by_role("button", name="Login").click()




    page.close()
