# Checking if an element is in the viewport

def is_fully_visible(locator):
    return locator.evaluate("""
        (el) => {
            function isVisible(element) {
                if (!element) return false;

                const style = window.getComputedStyle(element);
                if (style.display === "none" || style.visibility === "hidden" || parseFloat(style.opacity) === 0) {
                    return false;
                }

                const rect = element.getBoundingClientRect();
                if (
                    rect.bottom <= 0 ||
                    rect.right <= 0 ||
                    rect.top >= (window.innerHeight || document.documentElement.clientHeight) ||
                    rect.left >= (window.innerWidth || document.documentElement.clientWidth)
                ) {
                    return false;
                }

                // Check if element is inside all scrollable ancestors
                let parent = element.parentElement;
                while (parent) {
                    const pStyle = window.getComputedStyle(parent);
                    const overflowY = pStyle.overflowY;
                    const overflowX = pStyle.overflowX;

                    if (["auto", "scroll", "hidden"].includes(overflowY) || ["auto", "scroll", "hidden"].includes(overflowX)) {
                        const parentRect = parent.getBoundingClientRect();

                        // If element is outside parent's visible area, it's clipped
                        if (
                            rect.bottom <= parentRect.top ||
                            rect.top >= parentRect.bottom ||
                            rect.right <= parentRect.left ||
                            rect.left >= parentRect.right
                        ) {
                            return false;
                        }
                    }
                    parent = parent.parentElement;
                }
                return true;
            }
            return isVisible(el);
        }
    """)