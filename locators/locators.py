from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "https://qa-routes.praktikum-services.ru/"

    class Form:
        INPUT_HOUR = (By.ID, "form-input-hour")
        INPUT_MINUTE = (By.ID, "form-input-minute")
        INPUT_FROM = (By.ID, "form-input-from")
        INPUT_TO = (By.ID, "form-input-to")
        MODE_OPTIMAL = (By.ID, "form-mode-optimal")
        MODE_FASTEST = (By.ID, "form-mode-fastest")
        MODE_CUSTOM = (By.CSS_SELECTOR, "form-mode-custom")
        ICON_TYPE_CAR = (By.ID, "from-type-car")
        ICON_TYPE_WALK = (By.ID, "from-type-walk")
        ICON_TYPE_TAXI = (By.ID, "from-type-taxi")
        ICON_TYPE_BIKE = (By.ID, "from-type-bike")
        ICON_TYPE_SCOOTER = (By.ID, "from-type-scooter")
        ICON_TYPE_DRIVE = (By.ID, "from-type-drive")
        RESULT_TIME_PRICE = (By.ID, "result-time-price")




