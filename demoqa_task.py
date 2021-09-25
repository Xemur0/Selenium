
class Demoqa():

    def send_form(self, driver):
        driver.get('https://demoqa.com/')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]').click()

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[1]/div[2]/input') \
            .send_keys("Aleksandr Parafiynyk")

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[2]/div[2]/input') \
            .send_keys('aleks.prfnk@blabla.com')

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[3]/div[2]/textarea') \
            .send_keys('Saint-Petersburg')

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[4]/div[2]/textarea') \
            .send_keys('Planet Earth')

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div/button').click()

