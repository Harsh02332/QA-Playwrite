import re
from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    """
    A simple test to navigate to a website and check its title.
    """
    print("\nNavigating to Playwright website...")
    page.goto("https://playwright.dev/")
    
    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Playwright"))
    print("Title verified successfully!")

def test_search_functionality(page: Page):
    """
    A test to interact with elements on the page.
    """
    page.goto("https://playwright.dev/")
    
    # Click the 'Get Started' link/button
    print("Clicking 'Get Started'...")
    page.get_by_role("link", name="Get started").click()
    
    # Verify that the URL changed to the intro page
    expect(page).to_have_url(re.compile(".*intro"))
    print("URL verified successfully!") 