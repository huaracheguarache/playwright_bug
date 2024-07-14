from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

with sync_playwright() as p:
    browser = p.firefox.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0')
    page = context.new_page()
    try:
        page.goto("https://www.bamble.kommune.no/", timeout=30000)
    except PlaywrightTimeoutError:
        print('Firefox timed out!')
    else:
        print('Firefox succeeded!')
    finally:
        context.close()
        browser.close()

    browser = p.chromium.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                             ' Chrome/126.0.0.0 Safari/537.36')
    page = context.new_page()
    try:
        page.goto("https://www.bamble.kommune.no/", timeout=30000)
    except PlaywrightTimeoutError:
        print('Chromium timed out!')
    else:
        print('Chromium succeeded!')
    finally:
        context.close()
        browser.close()

    browser = p.webkit.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15'
                                             ' (KHTML, like Gecko) Version/17.5 Safari/605.1.15')
    page = context.new_page()
    try:
        page.goto("https://www.bamble.kommune.no/", timeout=30000)
    except PlaywrightTimeoutError:
        print('Webkit timed out!')
    else:
        print('Webkit succeeded!')
    finally:
        context.close()
        browser.close()
