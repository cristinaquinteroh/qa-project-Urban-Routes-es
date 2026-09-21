from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from utilis.retrieve_code import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')

    phone_button = (By.CSS_SELECTOR, '.np-button')
    phone_field = (By.ID, 'phone')
    phone_next_button = (By.XPATH, '//button[text()="Siguiente"]')
    sms_code_field = (By.ID, 'code')
    sms_confirm_button = (By.XPATH, '//button[text()="Confirmar"]')

    payment_method_button = (By.CSS_SELECTOR, '.pp-button')
    add_card_option = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '.card-code-input input')
    add_card_button = (By.XPATH, '//button[text()="Agregar"]')
    driver_message_field = (By.ID, 'comment')

    blanket_and_tissues_switch = (
        By.XPATH,
        '//div[@class="r-sw-container"][.//div[text()="Manta y pañuelos"]]//span[contains(@class,"slider")]'
    )
    blanket_and_tissues_checkbox = (
        By.XPATH,
        '//div[@class="r-sw-container"][.//div[text()="Manta y pañuelos"]]//input[@class="switch-input"]'
    )

    ice_cream_plus_button = (
        By.XPATH,
        '//div[@class="r-counter-container"][.//div[text()="Helado"]]//div[@class="counter-plus"]'
    )
    ice_cream_value = (
        By.XPATH,
        '//div[@class="r-counter-container"][.//div[text()="Helado"]]//div[@class="counter-value"]'
    )
    confirm_order_button = (By.CSS_SELECTOR, '.smart-button')
    search_car_modal_title = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=7)

    # --- Dirección ---
    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    # --- Taxi / Comfort ---
    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )

    def reader_comfort_icon_assert(self):
        comfort_tariff = self.get_comfort_icon_assert().text
        return comfort_tariff

    # --- Teléfono ---
    def click_phone_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.phone_button)
        ).click()

    def set_phone(self, phone_number):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_field)
        ).send_keys(phone_number)

    def click_phone_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.phone_next_button)
        ).click()

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def set_sms_code(self, code):
        self.wait.until(
            EC.visibility_of_element_located(self.sms_code_field)
        ).send_keys(code)

    def click_sms_confirm_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.sms_confirm_button)
        ).click()

    def fill_phone_number(self, phone_number):
        self.click_phone_button()
        self.set_phone(phone_number)
        self.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.set_sms_code(code)
        self.click_sms_confirm_button()

    # --- Tarjeta ---
    def click_payment_method_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.payment_method_button)
        ).click()

    def click_add_card_option(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_card_option)
        ).click()

    def set_card_number(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def set_card_code(self, card_code):
        field = self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        )
        field.send_keys(card_code)
        field.send_keys(Keys.TAB)  # fuerza el blur para habilitar el botón "Agregar"

    def click_add_card_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

    def add_credit_card(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_option()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_add_card_button()

    def set_driver_message(self, message):
        self.wait.until(
            EC.visibility_of_element_located(self.driver_message_field)
        ).send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.driver_message_field).get_property('value')

    def click_blanket_and_tissues_switch(self):
        self.wait.until(
        EC.element_to_be_clickable(self.blanket_and_tissues_switch)
        ).click()

    def is_blanket_and_tissues_selected(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_selected()

    def click_ice_cream_plus_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_plus_button)
        ).click()

    def add_ice_cream(self, quantity):
        for _ in range(quantity):
            self.click_ice_cream_plus_button()

    def get_ice_cream_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ice_cream_value)
        ).text

    def click_confirm_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_order_button)
        ).click()

    def get_search_car_modal_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.search_car_modal_title)
        ).text

