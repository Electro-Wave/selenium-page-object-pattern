import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser(request):
    options = Options()
    #options.add_argument("--headless")
    browser = Chrome(options=options)

    def fin():
        browser.quit()

    request.addfinalizer(fin)
    return browser