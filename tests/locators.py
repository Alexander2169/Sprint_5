from selenium.webdriver.common.by import By
class TestLocators:
    # Поле "Имя" на форме «Регистрация»
    input_name = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

    # Поле Email на форме «Регистрация»
    input_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" на форме «Регистрация»
    input_password = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка "Зарегистрироваться" на форме «Регистрация»
    button_submit = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # Сообщение о некорректном пароле на форме «Регистрация»    notification_incorrect_password = (By.XPATH, '//p[text()="Некорректный пароль"]')

    # Кнопка "Войти" на форме «Регистрация»
    button_login_in_registration_form = (By.XPATH, '//a[text()="Войти"]')

    # Поле Email на форме «Вход»
    input_email_auth = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" на форме «Вход»
    input_password_auth = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка "Войти" на форме «Вход»
    button_login = (By.XPATH, '//button[text()="Войти"]')

    # Кнопка "Зарегистрироваться" на форме «Вход»
    button_register = (By.XPATH, '//a[text()="Зарегистрироваться"]')

    # Кнопка "Восстановить пароль" на форме «Вход»
    button_forgot_password = (By.XPATH, '//a[text()="Восстановить пароль"]')

    # Кнопка "Войти" в форме восстановления пароля
    button_login_passwd_recovery_form = (By.XPATH, '//a[text()="Войти"]')

    # Личный кабинет
    # Раздел "Профиль" на странице «Личный кабинет»
    profile = (By.XPATH, '//a[@href="/account/profile"]')

    # Кнопка "Выйти" на странице «Личный кабинет»
    button_logout = (By.XPATH, '//button[@type="button"]')

    # Кнопка "Войти в аккаунт" на главной странице сервиса
    button_login_in_main = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Кнопка "Личный кабинет" на главной странице сервиса
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Кнопка "Конструктор" на главной странице сервиса
    header_of_page_constructor = (By.XPATH, '//p[text()="Конструктор"]')

    # Раздел "Булки" на форме «Конструктор»
    buns_block = (By.XPATH, '//span[text()="Булки"]')

    # Раздел "Соусы" на форме «Конструктор»
    sauces_block = (By.XPATH, '//span[text()="Соусы"]')

    # Раздел "Начинки" на форме «Конструктор»
    fillings_block = (By.XPATH, '//span[text()="Начинки"]')

    # Логотип на главной странице сервиса
    logo = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

