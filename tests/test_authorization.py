from playwright.sync_api import Page
import pytest

from pages.login_page import LoginPage

creds = {
    ("user.name@gmail.com", "password"): "Invalid email and password",
    ("user.name@gmail.com", "  "): "Invalid email, empty password",
    ("  ", "password"): "Empty email, invalid password",
}


@pytest.mark.parametrize("email, password", creds.keys(), ids=creds.values())
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization  # Добавили маркировку authorization
def test_wrong_email_or_password_authorization(email: str, password: str, login_page: LoginPage):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
