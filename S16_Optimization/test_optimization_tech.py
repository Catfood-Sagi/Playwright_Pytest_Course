'''Intercept Request'''

'''
How to skip over the resousces that our test does not require

By default when we intiating any page navifation, playwright loads every resource
'''

import pytest
from playwright.sync_api import Page, expect, Route, Browser


@pytest.fixture
def browser_context_args():
    return {
        "java_script_enabled": False,
    }

def test_js(browser: Browser):
    browser.new_context(
        java_script_enabled =False
    )

# Defining resources we dont need for our tests
NOT_ALLOWED_RESOURCES = (
    "image", "font", "stylesheet", "media" # adding "Scripts" will skip js files 
)

 # Setting an on_route function that will abort any request that involve anwarranted resource type
def on_route(route: Route):
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)
def skip_resources(page: Page):
    page.route("**", on_route) # this will match all network requests. basically sayin "“Intercept every request, no matter the URL or path.”"


def test_page_has_docs_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="docs")

    expect(link).to_be_visible()


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    expect(page).to_have_url(
        "https://playwright.dev/python/docs/intro"
    )