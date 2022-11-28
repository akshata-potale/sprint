from Data import reading_objects
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Library.config import Config
from Data.reading_objects import ReadExcel
read_excel = ReadExcel()
hotel_obj = read_excel.read_locators(Config.read_locators)
print(hotel_obj)
# from Data import reading_objects

class HotelPage:
    def __init__(self,driver):
        self.driver=driver

    def popup(self):
        self.driver.find_element(*hotel_obj['text_popup']).click()

    def click_hotel(self):
        self.driver.find_element(*hotel_obj['text_hotel']).click()

    def destination(self,destination_):
        place = self.driver.find_element(*hotel_obj['text_location'])
        place.click()
        place.send_keys(destination_)
        time.sleep(4)

    def dropdown(self):
        self.driver.find_element(*hotel_obj['text_dropdown']).click()

    def date(self):
        self.driver.find_element(*hotel_obj['text_fromdate']).click()
        time.sleep(4)
        self.driver.find_element(*hotel_obj['click_startdate']).click()
        time.sleep(4)
        self.driver.find_element(*hotel_obj['click_enddate']).click()

    def sel_dropdown(self):
        self.driver.find_element(*hotel_obj['select_dropdown']).click()
        self.driver.find_element(*hotel_obj['opt_dropdown']).click()
        self.driver.find_element(*hotel_obj['click_addroom']).click()
        self.driver.find_element(*hotel_obj['addroom_travellers']).click()
        self.driver.find_element(*hotel_obj['increase_child']).click()
        self.driver.find_element(*hotel_obj['page_click']).click()

    def button(self):
        self.driver.find_element(*hotel_obj['search_btn']).click()
        wait_obj = WebDriverWait(self.driver, 30)
        wait_obj.until(expected_conditions.presence_of_element_located(("xpath", "//div[@class='flex flex-nowrap']")))
        sel_btn = self.driver.find_element(*hotel_obj['select_btn'])
        obj_1 = ActionChains(self.driver)
        obj_1.move_to_element(sel_btn).perform()

        obj_1 = ActionChains(self.driver)
        obj_1.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def book_button(self):
        time.sleep(2)
        self.driver.find_element(*hotel_obj['book_btn']).click()

        handles = self.driver.window_handles
        print(handles)
        print(handles[1])
        time.sleep(10)
        self.driver.switch_to.window(handles[1])

        obj_2 = ActionChains(self.driver)
        obj_2.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def continue_button(self):
        self.driver.find_element(*hotel_obj['continue_btn']).click()
        time.sleep(2)

    def enter_mob(self,mobile_):
        self.driver.find_element(*hotel_obj['text_mob']).send_keys(mobile_)

    def enter_email(self,email_):
        self.driver.find_element(*hotel_obj['text_email']).send_keys(email_)

    def button_continue(self):
        self.driver.find_element(*hotel_obj['btn_continue']).click()
        time.sleep(2)

    def title_click(self):
        self.driver.find_element(*hotel_obj['click_title']).click()

    def text_title(self):
        self.driver.find_element(*hotel_obj['text_title']).click()

    def first_name(self,f_name):
        self.driver.find_element(*hotel_obj['text_firstname']).send_keys(f_name)

    def last_name(self,l_name):
        self.driver.find_element(*hotel_obj['text_lastname']).send_keys(l_name)
        obj_1 = ActionChains(self.driver)
        obj_1.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def payment_btn(self):
        time.sleep(5)
        self.driver.find_element(*hotel_obj['payment_btn']).click()
        # pay.click()
        # pay_btn = self.driver.find_element(*hotel_obj['payment_btn'])
        # obj_1 = ActionChains(self.driver)
        # obj_1.move_to_element(pay_btn).perform()

