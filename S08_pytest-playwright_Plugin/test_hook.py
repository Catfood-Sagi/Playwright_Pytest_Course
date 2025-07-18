import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True, scope="function") 
# autouse=True means this fixture will be automatically used by all tests in this module.
# while this can help to avoid repeating the fixture in each test, it can also make tests
# less explicit.
def visit_playwright(page: Page):
    # setup
    page.goto("https://playwright.dev/python")
    # yield value and pause
    yield page
    # teardown
    page.close()
    print("\n[ Fixture ]: page closed!")


def test_page_has_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()


def test_get_started_visits_docs(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL