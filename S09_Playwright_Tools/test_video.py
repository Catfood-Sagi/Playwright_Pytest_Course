import pytest
from playwright.sync_api import Browser, Page
import shutil
from pathlib import Path
import datetime


DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(browser: Browser):
    context = browser.new_context(
        record_video_dir="video/"
    )
    page = context.new_page()

    page.goto("https://playwright.dev/python")

    theme_btn = page.get_by_role('button', name="Switch between dark and light mode (currently system mode)")
    theme_btn.click()

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL
    page.close()

'''
    # There is an option to change the video name
    # In order to do it you muse close the page or context first

    timestamp = datetime.datetime.now().strftime("%H-%M")
    video_path = page.video.path()
    new_name = f"recodring_{timestamp}.webm"
    shutil.move(video_path, Path("video") / new_name)

'''