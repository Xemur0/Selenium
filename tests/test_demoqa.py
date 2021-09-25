from selenium_train.demoqa_task import Demoqa


class Test_Demoqa(Demoqa):

    def test_send_form(self, driver):

        obj = Demoqa()
        obj.send_form(driver)

        current_url = driver.current_url
        first_and_last_name = driver.find_element_by_id('userName').get_attribute('value')
        email_address = driver.find_element_by_id('userEmail').get_attribute('value')
        current_address = driver.find_element_by_id('currentAddress').get_attribute('value')
        permanent_address = driver.find_element_by_id('permanentAddress').get_attribute('value')

        assert current_url == 'https://demoqa.com/text-box'
        assert first_and_last_name == "Aleksandr Parafiynyk"
        assert email_address == 'aleks.prfnk@blabla.com'
        assert current_address == 'Saint-Petersburg'
        assert permanent_address == 'Planet Earth'

