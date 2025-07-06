def scroll_to_element(locator):
    '''
    Scrolling to the location of the element
    '''
    locator.scroll_into_view_if_needed()
    elem_box = locator.bounding_box()
    viewport = locator.page.viewport_size

    elem_top = elem_box["y"]
    elem_bottom = elem_box["y"] + elem_box["height"]
    view_top = 0
    view_bottom = viewport["height"]

    if elem_bottom > view_bottom or elem_top < view_top:
        scroll_y = max(0, elem_bottom - viewport["height"])
        locator.page.evaluate(f"window.scrollTo(0, {scroll_y})")


def scroll_to_element2(locator):
    '''
    Tries to scroll the element into full view.
    First scrolls the page, then scrolls the parent container if still needed.
    '''
    # Step 1: Try to scroll the page
    elem_box = locator.bounding_box()
    viewport = locator.page.viewport_size
    page = locator.page

    if elem_box and viewport:
        elem_top = elem_box["y"]
        elem_bottom = elem_box["y"] + elem_box["height"]
        view_top = 0
        view_bottom = viewport["height"]

        if elem_bottom > view_bottom or elem_top < view_top:
            scroll_y = max(0, elem_top - 20)  # Small buffer for safety
            locator.page.evaluate(f"window.scrollTo(0, {scroll_y})")

    # STEP 2: Re-check visibility and scroll the container (div)
    elem_box = locator.bounding_box()
    if not elem_box:
        return

    # Get parent container (scrollable div)
    container = locator.locator("..")

    # Pass both handles separately
    container_handle = container.element_handle()
    target_handle = locator.element_handle()

    if not container_handle or not target_handle:
        return

    page.evaluate(
        """
        ([container, target]) => {
            if (!container || !target) return;

            const containerRect = container.getBoundingClientRect();
            const targetRect = target.getBoundingClientRect();

            const isAbove = targetRect.top < containerRect.top;
            const isBelow = targetRect.bottom > containerRect.bottom;

            if (isAbove) {
                container.scrollTop -= (containerRect.top - targetRect.top);
            } else if (isBelow) {
                container.scrollTop += (targetRect.bottom - containerRect.bottom);
            }
        }
        """,
        [container_handle, target_handle]
    )

def scroll_to_element3(locator):
    '''
    Ensure the element is fully visible on screen.
    Scrolls both the page and a potential scrollable container.
    '''

    page = locator.page
    viewport = page.viewport_size

    if not viewport:
        return

    # Step 1: Scroll the page if the element is partially or fully out of view
    elem_box = locator.bounding_box()
    if not elem_box:
        return

    elem_top = elem_box["y"]
    elem_bottom = elem_box["y"] + elem_box["height"]
    view_top = 0
    view_bottom = viewport["height"]

    fully_visible_in_page = elem_top >= view_top and elem_bottom <= view_bottom

    if not fully_visible_in_page:
        # Scroll page so the element's top is near top of screen
        scroll_y = max(0, elem_top - 20)
        page.evaluate(f"window.scrollTo(0, {scroll_y})")

        # Re-check bounding box after scrolling
        elem_box = locator.bounding_box()
        if not elem_box:
            return

    # Step 2: Scroll container if needed
    container = locator.locator("xpath=ancestor::*[contains(@style, 'overflow')]").first
    container_handle = container.element_handle()
    target_handle = locator.element_handle()

    if not container_handle or not target_handle:
        return

    page.evaluate(
        """
        ([container, target]) => {
            const containerRect = container.getBoundingClientRect();
            const targetRect = target.getBoundingClientRect();

            const isAbove = targetRect.top < containerRect.top;
            const isBelow = targetRect.bottom > containerRect.bottom;

            if (isAbove) {
                container.scrollTop -= (containerRect.top - targetRect.top);
            } else if (isBelow) {
                container.scrollTop += (targetRect.bottom - containerRect.bottom);
            }
        }
        """,
        [container_handle, target_handle]
    )

    # Optional: confirm final visibility
    final_box = locator.bounding_box()
    if final_box:
        final_top = final_box["y"]
        final_bottom = final_box["y"] + final_box["height"]
        if not (final_top >= 0 and final_bottom <= viewport["height"]):
            raise Exception("Element is still not fully visible on screen")
