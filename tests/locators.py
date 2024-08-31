from selenium.webdriver.common.by import By
class Locators:
    # Локаторы для регистрации
    NAME_IMPUT = (By.NAME, "name")
    EMAIL_IMPUT = (By.NAME, "email")
    PASSWORD_IMPUT = (By.NAME, "password")
    REGISTER_BUTTON = (By.XPATH, "//button[text()="Зарегистрироватья"]")
    ERROR_MESSAGE = (By.XPATH, "//p[text()="Некорректный пароль"]")

    # Локаторы для входа
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()="Войти в аккаунт"]")
    LOGIN_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[text()="Личный кабинет"]")
    LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//button[text()="Войти"]")
    LOGIN_BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[text()="Восстановить пароль"]")

    # Локаторы для навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()="Конструктор"]")
    LOGO = (By.XPATH, "//div[@class="AppHeader_header__logo__2D0X2"]")

    # Локатор для выхода
    LOGOUT_BUTTON = (By.XPATH, "//button[text()="Выйти"]")

    # Локаторы меню Конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()="Булки"]")
    SAUCES_SECTION = (By.XPATH, "//span[text()="Соусы"]")
    FILLINGS_SECTION = (By.XPATH, "//span[text()="Начинки"]")