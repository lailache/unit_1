import pytest

from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", False),
    ("", "", False),
])
def test_purchase(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected_result:

        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information("Laila", "Che", "001")
        checkout_page.finish()

        assert checkout_page.is_order_complete()
    else:

        assert login_page.is_error_message_displayed()
