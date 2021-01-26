from pages.main_page import YandexSearchLocators, SearchImagePage

def test_search_image_yandex(browser):
    page = SearchImagePage(browser)
    page.go_to_site()
    page.get_windows()
    page.click_to_element(locator=YandexSearchLocators.LOCATOR_IMAGE_SEARCH)
    page.get_windows()
    page.switch_to_popup_window()
    page.click_to_element(locator=YandexSearchLocators.LOCATOR_UPLOAD_BUTTON)
    page.upload_image(locator=YandexSearchLocators.LOCATOR_FILE_INPUT, upload_file='автокран.jpg')
    page.get_list_of_results(upload_image='автокран')

