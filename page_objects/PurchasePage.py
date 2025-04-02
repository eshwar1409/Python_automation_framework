from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self,driver):
        self.driver = driver

    country = (By.XPATH, "//input[@id='country']")
    #self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("In")

    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    #self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

    confirmButton = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    #self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

    alertMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    #self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

    def Country(self):
        return self.driver.find_element(*PurchasePage.country)

    def CheckBox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def ConfirmButton(self):
        return self.driver.find_element(*PurchasePage.confirmButton)

    def AlertMsg(self):
        return self.driver.find_element(*PurchasePage.alertMessage)


