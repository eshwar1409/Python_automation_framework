from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    confirmPage = (By.XPATH, "//input[@class='form-control']")
    #self.driver.find_element(By.XPATH, "//input[@class='form-control']")

    price = (By.XPATH, "//tbody/tr[1]/td[3]")
    #self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]")

    totalPrice = (By.CSS_SELECTOR, "tbody tr td:nth-child(4) strong:nth-child(1)")
    #self.driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(4) strong:nth-child(1)")

    checkout_button = (By.XPATH, "//button[normalize-space()='Checkout']")
    #self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()

    def QuantityInput(self):
        return self.driver.find_element(*ConfirmPage.confirmPage)

    def Price(self):
        return self.driver.find_element(*ConfirmPage.price)

    def TotalPrice(self):
        return self.driver.find_element(*ConfirmPage.totalPrice)

    def CheckOutButton(self):
        return self.driver.find_element(*ConfirmPage.checkout_button)


