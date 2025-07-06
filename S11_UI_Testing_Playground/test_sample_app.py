'''
In this task, i will write a simple test where im filiing and submitting a form

Requirements:
1. Any non empty username and 'pwd' as password should result in a successful login
2. Upon sucssful login, a welcome message should be displayed reading "Welcome, {username}!"
3. Any other username and password should result in an error message "Invalid username/password"
'''
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def visit_test_page(page: Page):
    page.goto("http://uitestingplayground.com/sampleapp")


def test_successful_login(page: Page):
    username = "user"
    password = "pwd"

    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")

    login_btn = page.get_by_role("button", name="Log In")

    username_input.fill(username)
    password_input.fill(password)

    login_btn.click()

    label = page.locator("label#loginstatus")

    expect(label).to_have_text(f"Welcome, {username}!")


def test_failed_login(page: Page):
    username = "username"
    password = "cnasdjc"

    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")

    login_btn = page.get_by_role("button", name="Log In")

    username_input.fill(username)
    password_input.fill(password)

    login_btn.click()

    label = page.locator("label#loginstatus")

    expect(label).to_have_text("Invalid username/password")