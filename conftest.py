import pytest
from selene.support.shared import browser

@pytest.fixture(scope="function", autouse=True)
#autouse=True - фикстура будет автоматически запускаться перед тестом и не нужно прописывать эту фукстуру в тесте
#scope="function" - фикстура будет запускаться перед каждым тестом
def open_browser():
    browser.config.driver_name = 'firefox'
    browser.open('https://google.com')
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()



