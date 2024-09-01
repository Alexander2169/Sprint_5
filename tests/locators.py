from selenium.webdriver.common.by import By
class Locators:
    # Поле "Имя" на форме «Регистрация»
    input_name = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

    # Поле Email на форме «Регистрация»
    input_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" на форме «Регистрация»
    input_password = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка "Зарегистрироваться" на форме «Регистрация»
    button_register_2 = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # Сообщение о некорректном пароле на форме «Регистрация»
    message_incorrect_password = (By.XPATH, '//p[text()="Некорректный пароль"]')

    # Кнопка "Войти" на форме «Регистрация»
    button_login_in_registration = (By.XPATH, '//a[text()="Войти"]')

    # Поле Email на форме «Вход»
    input_email_login = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" на форме «Вход»
    input_password_login = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка "Войти" на форме «Вход»
    button_login = (By.XPATH, '//button[text()="Войти"]')

    # Кнопка "Зарегистрироваться" на форме «Вход»
    button_register_1 = (By.XPATH, '//a[text()="Зарегистрироваться"]')

    # Кнопка "Восстановить пароль" на форме «Вход»
    button_recover_password = (By.XPATH, '//a[text()="Восстановить пароль"]')

    # Кнопка "Войти" в форме восстановления пароля
    button_login_recover_password = (By.XPATH, '//a[text()="Войти"]')

    # Раздел "Профиль" на странице «Личный кабинет»
    profile = (By.XPATH, '//a[@href="/account/profile"]')

    # Кнопка "Выйти" на странице «Личный кабинет»
    button_logout = (By.XPATH, '//button[@type="button"]')

    # Кнопка "Войти в аккаунт" на главной странице сервиса
    button_login_main_page = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Кнопка "Конструктор"
    button_constructor_main_page = (By.XPATH, '//p[text()="Конструктор"]')

    # Раздел "Булки" на форме «Конструктор»
    buns_section = (By.XPATH, '//span[text()="Булки"]')

    # Раздел "Соусы" на форме «Конструктор»
    sauces_section = (By.XPATH, '//span[text()="Соусы"]')

    # Раздел "Начинки" на форме «Конструктор»
    fillings_section = (By.XPATH, '//span[text()="Начинки"]')

    # Логотип на главной странице сервиса
    logo = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')



