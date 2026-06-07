
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

#pywright test for UI basic code.

def test_coreLocators(page:Page):
    page.goto("https://admin.zesty-go.com/")
    page.get_by_placeholder("Enter your email").fill("implicittechgroup@gmail.com")
    page.get_by_placeholder("Enter your password").fill("123456")
    #page.get_by_role("button", name="Forgot your password?").click()
    page.get_by_role("button", name="Sign Me In").click()
    # The OTP we want to enter
    otp_code = "123456"
    
    # Find all 6 input boxes using their CSS classes
    otp_boxes = page.locator("input.form-control.text-center.fs-4.fw-bold")
    
    # Loop through each digit and put it in the corresponding box
    for i, digit in enumerate(otp_code):
        otp_boxes.nth(i).fill(digit)
