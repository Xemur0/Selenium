from selenium import webdriver


class Demoqa():

    driver = webdriver.Chrome()

    def send_form(self):
        self.driver.get('https://demoqa.com/')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]').click()
        self.driver.find_element_by_id('item-0').click()
        self.driver.find_element_by_id('userName').send_keys("Aleksandr Parafiynyk")
        self.driver.find_element_by_id('userEmail').send_keys('aleks.prfnk@blabla.com')
        self.driver.find_element_by_id('currentAddress').send_keys('Saint-Petersburg')
        self.driver.find_element_by_id('permanentAddress').send_keys('Planet Earth')
        self.driver.find_element_by_id('submit').click()