from playwright.sync_api import *
import pytest

NOT_ALLOWED_RESOURCES = (
    "image", "font", "stylesheet", "media"
)

def on_route(route: Route):
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()


with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    context = browser.new_context(
        storage_state="playwright\.auth\storage_state.json"
    )
    page = context.new_page()
    page.route("**", on_route)
    page.goto("https://gmail.com")

    new_emails = []
    emails = page.locator("div.UI table tr")

    for email in emails.all():
        is_new_email = email.locator(
            "td li[data-tooltip='Mark as read']"
        ).count() == 1

        if is_new_email:
            sender = email.locator("td span[email]:visible").inner_text()
            title = email.locator("td span[data-thread-id]:visible").inner_text()

            new_emails.append(
                [sender, title]
            )

    if len(new_emails) == 0:
        print("No new emails 📫!")
    else:
        print(f"{len(new_emails)} new email\s 📩!")
        print("-"*30)

        for new_email in new_emails:
            print(new_email[0]+":", new_email[1])
            print("-"*30)

    
    context.close()