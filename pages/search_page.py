from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page


class SearchPage(Page):
    SEARCH_FIELD = (AppiumBy.XPATH,"//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia:id/search_src_text']")
    SEARCH_RESULT = (AppiumBy.XPATH, "//*[contains( @text, '{SUBSTR}')]")


    def _get_search_result_locator(self,expected_text):
        return [self.SEARCH_RESULT[0],self.SEARCH_RESULT[1].replace('{SUBSTR}',expected_text)]

    def input_search_text(self, search_text):
        self.input(search_text, *self.SEARCH_FIELD)
        self.driver.save_screenshot('screenshots/03_search_text.png')


    def verify_search_result(self, expected_text):
        locator = self._get_search_result_locator(expected_text)
        self.wait_for_element_appear(*locator)
        self.driver.save_screenshot('screenshots/04_search_result.png')

