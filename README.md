## Автоматизация тест кейсов отображене расчета стоимости и времени поездки учебного приложение [Яндекс.Маршруты ](https://qa-routes.praktikum-services.ru/ "Яндекс.Маршруты") с использованием Page Object pattern.
  
 Яндекс.Маршруты — сервис, который строит маршруты для транспорта разных видов. Рассчитывает время и стоимость поездки в зависимости от времени начала поездки.
***

 
 
 
 
 
 > PageObject - Это шаблон проектирования для авто-тестирования при котором
каждая страница приложения описывается как объект внутри которого
инкапсулируется и реализуется логика действий, которые на этой странице
можно выполнять.



`BasePage` класс включает базовую функциональность и инициализацию драйвера

```python
#BasePage.py
class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    def _open_page(self, url):
        self.driver.get(url)
        return self

    def input_value(self, locator, value):
        elem = self.driver.find_element(*locator)
        elem.send_keys(value)
        return self
```
`MainPage`  наследуте  от класса BasePage, он содержит методы, относящиеся к этой странице, которые будут использоваться для создания шагов теста.
```python
#MainPage.py
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
```        

В `test_result_time_price.py` опысываются тесты расчета стоимости и времени поездки режима "Оптимальный" И "Быстрый"

```python
#test_result_time_price.py
# тест расчета стоимости и времени поездки режима "Оптимальный"
@pytest.mark.parametrize("hour, minute, from_, to", test_data_1)
def test_result_time_price_mode_optimal(browser, hour, minute, from_, to):
    page = MainPage(browser)
    page.open().input_filed_hour(hour).input_filed_minute(minute) \
        .input_filed_from(from_).input_filed_to(to).click_mode_optimal()
    assert page.present_result_time_price() == "Авто ~ 16 руб. В пути 2 мин."
```