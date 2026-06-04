from playwright.sync_api import sync_playwright

def test_browser_launch():
    with sync_playwright() as p:
        # Запуск в headless=False (с GUI) или headless=True (без GUI)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()