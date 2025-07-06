def is_locator_overlapped(locator) -> bool:
    """
    Returns True if the given Playwright locator is overlapped
    by another element at its center point.

    Args:
        locator (Locator): Playwright locator for the element to check.

    Returns:
        bool: True if another element is covering it; False otherwise.
    """
    return locator.evaluate("""
        el => {
            if (!el) return false;
            const rect = el.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;
            const elAtPoint = document.elementFromPoint(x, y);
            return elAtPoint !== el && !el.contains(elAtPoint);
        }
    """)