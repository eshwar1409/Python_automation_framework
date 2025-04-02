from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import AddCart


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    label = (By.CLASS_NAME, 'form-check-label')




    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    def shoplist(self):
        self.driver.find_element(*HomePage.shop).click()
        cart = AddCart(self.driver)
        return cart

    def Name(self):
        return self.driver.find_element(*HomePage.name)

    def Email(self):
        return self.driver.find_element(*HomePage.email)

    def PassWord(self):
        return self.driver.find_element(*HomePage.password)

    def CheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def Label(self):
        return self.driver.find_element(*HomePage.label)



