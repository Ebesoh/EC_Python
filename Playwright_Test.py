import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner/")
    page.get_by_role("link", name="Docs").click()
    page.get_by_role("link", name="API", exact=True).click()
    page.locator("#docsNav").get_by_role("link", name="Getting Started").click()
    page.get_by_role("link", name="Command-line Runner", exact=True).click()
    page.get_by_role("link", name="Control Flow", exact=True).click()
    page.get_by_role("link", name="Code Export", exact=True).click()
    page.get_by_role("link", name="Frequently Asked Questions", exact=True).click()
    page.get_by_role("link", name="Plugins").click()
    page.get_by_role("link", name="Emitting Code").click()
    page.get_by_role("link", name="Exporting Code", exact=True).click()
    page.get_by_role("heading", name="API Reference").click()
