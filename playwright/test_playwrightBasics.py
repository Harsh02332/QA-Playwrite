
# If i have a custom requirements like instead of chromium i want to use firefox or i want to run my test in headless mode i can create a fixture and use that fixture in my test case.
from playwright.sync_api import Page
def test_playwriteBasics(playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin.zesty-go.com/")

# if i want to use cheromium without headless mode then i can use page fixture which is already available in playwright and i can directly use that in my test case without creating a new instance of browser and context.

def test_playwrightShortCut(page:Page):
    page.goto("https://admin.zesty-go.com/")