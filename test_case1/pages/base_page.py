from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://yandex.ru/'

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator)).click()

    def get_windows(self):
        windows = list(self.driver.window_handles)
        is_here_more_then_one_window = len(windows) > 1
        return windows if is_here_more_then_one_window else False

