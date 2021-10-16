from selenium_train.demoqa_task import Demoqa

class Test_Demoqa(Demoqa):

    def test_input_text_in_send_form(self):

        obj = Demoqa()
        obj.send_form()

        assert obj.driver.current_url == 'https://demoqa.com/text-box'
        assert obj.driver.find_element_by_id('userName').get_attribute('value') == "Aleksandr Parafiynyk"
        assert obj.driver.find_element_by_id('userEmail').get_attribute('value') == 'aleks.prfnk@blabla.com'
        assert obj.driver.find_element_by_id('currentAddress').get_attribute('value') == 'Saint-Petersburg'
        assert obj.driver.find_element_by_id('permanentAddress').get_attribute('value') == 'Planet Earth'

        obj.driver.close()