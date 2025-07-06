'''
Testing a progress bar.
Task - press the start button, wait untill the progress bar reaches 75% or more, then press the stop button.
the less the difference between the value of the stopped proress bar and 75% the better.

My Answer
'''
from playwright.sync_api import Page
def test_progress_bar(page: Page):
    page.goto("http://www.uitestingplayground.com/progressbar")
    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")
    progress_bar = page.get_by_role("progressbar")

    # Start the progress bar
    start_btn.click()

    while True:
        current_value = progress_bar.get_attribute("aria-valuenow")
        if current_value >= "75":  # it might be safer to to check it like >= 75
            break
    
    # Stop the progress bar
    stop_btn.click()
    print(f"Progress bar stopped at {current_value}%")
    assert current_value >= "75", f"Expected progress bar to reach 75%, but got {current_value}"



'''
Course Answer
from playwright.sync_api import Page


def test_progressbar(page: Page):
    page.goto("http://uitestingplayground.com/progressbar")

    progressbar = page.get_by_role("progressbar")

    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")

    # start progress
    start_btn.click()

    # check progress
    while True:
        valuenow = int(progressbar.get_attribute("aria-valuenow"))
        print(f"Percent: {valuenow}%")

        # progress more than or equal to 75
        if valuenow >= 75:
            break

    # stop progress
    stop_btn.click()

    assert valuenow >= 75

'''