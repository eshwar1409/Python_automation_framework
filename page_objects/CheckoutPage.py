from selenium.webdriver.common.by import By


class AddCart:

    def __init__(self,driver):
        self.driver = driver

    #CartList_1 = (By.XPATH, "//div[@class='card h-100']")
    CartList_1 = (By.CSS_SELECTOR, ".card-title a")

    footer_button = (By.CSS_SELECTOR, ".card-footer button")
    #product.find_element(By.XPATH, "div/button").click()

    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

    def CartList(self):
        return self.driver.find_elements(*AddCart.CartList_1)

    def Footer(self):
        return self.driver.find_element(*AddCart.footer_button)

    def CheckOut(self):
        return self.driver.find_element(*AddCart.checkout)

