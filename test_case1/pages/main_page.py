import os

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_IMAGE_SEARCH = (By.XPATH, '//*[@data-id="images"]')
    LOCATOR_UPLOAD_BUTTON = (By.XPATH, '//*[@aria-label="Поиск по изображению"]')
    LOCATOR_FILE_INPUT = (By.XPATH, '//*[@class="cbir-panel__file-input"]')
    LOCATOR_SEARCH_IMAGE = (By.XPATH, '//*[@class="CbirPreview-Trimmer"]')


class SearchImagePage(BasePage):

    def switch_to_popup_window(self):
        window_handles = self.get_windows()
        try:
            current_handle_index = window_handles.index(self.driver.current_window_handle)
            self.driver.switch_to.window(window_handles[current_handle_index + 1])
        except IndexError:
            self.driver.switch_to.window(window_handles[-1])
        self.driver.maximize_window()

    def get_list_of_results(self, upload_image):
        WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located(YandexSearchLocators.LOCATOR_SEARCH_IMAGE))
        tag_result = self.driver.find_elements(By.XPATH, f'//div[text() = "Кажется, на '
                                                         f'изображении"]/following-sibling '
                                                         f'::div//span[contains( text(), '
                                                         f'"{upload_image}")]')

        assert tag_result

    def upload_image(self, locator, upload_file):
        file_input = self.find_element(locator)
        file_path = os.getcwd()
        file_input.send_keys(file_path + f'/{upload_file}')
        search_result = YandexSearchLocators.LOCATOR_SEARCH_IMAGE

        return search_result
