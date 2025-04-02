from datetime import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.CheckoutPage import AddCart
from page_objects.ConfirmPage import ConfirmPage
from page_objects.HomePage import HomePage
from page_objects.PurchasePage import PurchasePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        cart = homepage.shoplist()
        log.info("retriving the list")
        products = cart.CartList()

        for product in products:
            name = product.text
            log.info(name)

            if name == "Blackberry":
               cart.Footer().click()

        check = AddCart(self.driver)
        check.CheckOut().click()
        values = ConfirmPage(self.driver)
        quantity = values.QuantityInput()
        a = int(quantity.get_attribute("value"))
        b = a + 1
        print(b)
        quantity.clear()
        quantity.send_keys(str(b))

        price = ConfirmPage(self.driver)
        pieceOfPrice = price.Price()
        print(pieceOfPrice.text)
        #time.sleep(5)
        Total = ConfirmPage(self.driver)
        total = Total.TotalPrice()
        print(total.text)

        checkout = ConfirmPage(self.driver)
        checkout.CheckOutButton().click()

        countryInput = PurchasePage(self.driver)
        countryInput.Country().send_keys("In")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        checkbox = PurchasePage(self.driver)
        checkbox.CheckBox().click()

        confirm = PurchasePage(self.driver)
        confirm.ConfirmButton().click()

        alert_message = PurchasePage(self.driver)
        alertMessage = alert_message.AlertMsg().text
        assert "Success!" in alertMessage
        print(alertMessage)






