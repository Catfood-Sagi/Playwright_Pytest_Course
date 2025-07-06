from playwright.sync_api import sync_playwright


# download event handler
def on_download(download):
    print("Download received!")
    download.save_as("night.jpg")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=200
    )
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

    # register listener
    page.once("download", on_download)

    # get the download button
    btn = page.get_by_role("link", name="Download free")

    # expect download
    with page.expect_download() as download_info: # this is a context manager that waits for the download event
        # trigger download
        btn.click()

    # Save using download_info
       # download = download_info.value  this is the download object
       # download.save_as("moon.jpg")   saves the file with the specified name

    browser.close()