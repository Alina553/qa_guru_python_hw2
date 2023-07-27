import pytest
from selene import be, have
from selene.support.shared import browser


def test_valid_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_invalid_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('asasasasadwqdccdqwe').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))

