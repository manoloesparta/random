from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    for i in range(1000):
        url = "https://dilean12.sarahah.com/"
        browser.visit(url)
        browser.find_by_tag('textarea').fill('Ah que dijo')
        # Find and click the 'search' button
        button = browser.find_by_id('Send').click()

# brew install chromedriver
# pip install splinter