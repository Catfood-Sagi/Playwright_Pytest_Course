'''
Handling dynamic table can be tricky, especially when the table structure is not static.
What we need to do:
first get the value from the label
then, i need to locate the cpu column header
and then find the row with "Chrome" value
'''

from playwright.sync_api import Page, expect

def test_dynamic_table(page: Page):
    page.goto("http://uitestingplayground.com/dynamictable")
    
    # given chrome CPU value
    label = page.locator("p.bg-warning").inner_text() # will return the text inside the p element 
    chrome_percentage = label.split()[-1] # get only the value%

    # locate all column headers
    column_headers = page.get_by_role("columnheader", name="CPU")

def test_dynamic_table(page: Page):

    page.goto("http://uitestingplayground.com/dynamictable")
    
    # given chrome CPU value
    label = page.locator("p.bg-warning").inner_text() # will return the text inside the p element 
    chrome_percentage = label.split()[-1] # get only the value%

    # locate all column headers
    column_headers = page.get_by_role("columnheader")
    cpu_column = None

    # find column header with "CPU"
    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)

        if column_header.inner_text() == "CPU":
            cpu_column = index
            break
    
    # make sure CPU column is found
    assert cpu_column != None

    # second rowgroup with values
    rowgroup = page.get_by_role("rowgroup").last
    # row with "Chrome" value
    chrome_row = rowgroup.get_by_role("row").filter(
        has_text="Chrome"
    )
    # cell with cpu value
    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    # expect given cpu value to match cell value
    expect(chrome_cpu).to_have_text(chrome_percentage)