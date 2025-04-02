import pytest
from selenium.webdriver.common.by import By

from TestData.HomepageTestData import TestDataHomePage
from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePageLogin(BaseClass):

    def test_case2(self,inputData):
        homepage_1 = HomePage(self.driver)
        homepage_1.Name().send_keys(inputData["Name"])
        # driver.find_element(By.NAME, 'name').send_keys("Eshwar")
        homepage_1.Email().send_keys(inputData["Email"])
        # driver.find_element(By.NAME, 'email').send_keys("Abcd@gmail.com")
        homepage_1.PassWord().send_keys(inputData["Password"])
        # driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456789")
        homepage_1.CheckBox().click()
        # driver.find_element(By.ID, 'exampleCheck1').click()

        Label = homepage_1.Label().text
        print(Label)
        assert "Check" in Label
        self.driver.find_element(By.XPATH, '//option[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[id=inlineRadio2]').click()
        self.driver.find_element(By.NAME, 'bday').send_keys("03/12/2023")
        self.driver.find_element(By.CSS_SELECTOR, 'input[value=Submit]').click()

        self.driver.refresh()

    @pytest.fixture(params=TestDataHomePage.getData("TC_2"))
    def inputData(self,request):
        return request.param