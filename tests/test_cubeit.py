from playwright.sync_api import Page, expect, Error

import pytest

BASE_URL = 'http://127.0.0.1:8000/'


def test_cube(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder('enter number...').fill('5')
    page.get_by_role('button', name='Cube').click()
    result = page.locator('p#result')

    expect(result).to_contain_text('125')


def test_empty_input(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder('enter number...').fill('')
    page.get_by_role('button', name='Cube').click()
    result = page.locator('p#result')

    expect(result).to_have_text('Enter something!')


def test_string_input(page: Page):
    page.goto(BASE_URL)

    with pytest.raises(Error):
        assert page.get_by_placeholder('enter number...').fill('qwerty/.,')


