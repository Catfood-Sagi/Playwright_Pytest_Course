import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("button", name="Switch between dark and light").click()
    page.get_by_role("button", name="Switch between dark and light").click()
    page.get_by_role("button", name="Search (Ctrl+K)").click()
    page.get_by_role("searchbox", name="Search").fill("codegen")
    page.get_by_role("searchbox", name="Search").press("Enter")
