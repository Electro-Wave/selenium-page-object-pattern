import pytest
from pages import MainPage
from test_data import test_data_1


# тест расчета стоимости и времени поездки режима "Оптимальный"
@pytest.mark.parametrize("hour, minute, from_, to", test_data_1)
def test_result_time_price_mode_optimal(browser, hour, minute, from_, to):
    page = MainPage(browser)
    page.open().input_filed_hour(hour).input_filed_minute(minute) \
        .input_filed_from(from_).input_filed_to(to).click_mode_optimal()
    assert page.present_result_time_price() == "Авто ~ 16 руб. В пути 2 мин."


# тест расчета стоимости и времени поездки режима "Быстрый"
@pytest.mark.parametrize("hour, minute, from_, to", test_data_1)
def test_result_time_price_mode_fastest(browser, hour, minute, from_, to):
    page = MainPage(browser)
    page.open().input_filed_hour(hour).input_filed_minute(minute) \
        .input_filed_from(from_).input_filed_to(to).click_mode_fastest()
    assert page.present_result_time_price() == "Такси ~ 17 руб. В пути 2 мин."
