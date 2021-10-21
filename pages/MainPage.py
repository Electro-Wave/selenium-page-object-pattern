from .BasePage import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def open(self):
        return self._open_page(MainPageLocators.URL)

    def input_filed_hour(self, value):
        return self.input_value(MainPageLocators.Form.INPUT_HOUR, value)

    def input_filed_minute(self, value):
        return self.input_value(MainPageLocators.Form.INPUT_MINUTE, value)

    def input_filed_from(self, value):
        return self.input_value(MainPageLocators.Form.INPUT_FROM, value)

    def input_filed_to(self, value):
        return self.input_value(MainPageLocators.Form.INPUT_TO, value)

    def click_mode_optimal(self):
        return self.click(MainPageLocators.Form.MODE_OPTIMAL)

    def click_mode_custom(self):
        return self.click(MainPageLocators.Form.MODE_CUSTOM)

    def click_mode_fastest(self):
        return self.click(MainPageLocators.Form.MODE_FASTEST)

    def click_icon_drive(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_DRIVE)

    def click_icon_bike(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_BIKE)

    def click_icon_car(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_CAR)

    def click_icon_taxi(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_TAXI)

    def click_icon_walk(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_WALK)

    def click_icon_scooter(self):
        return self.click(MainPageLocators.Form.ICON_TYPE_SCOOTER)

    def present_result_time_price(self):
        elem = self.get_text(MainPageLocators.Form.RESULT_TIME_PRICE).split("\n")
        return " ".join(elem)