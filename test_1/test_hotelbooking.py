import pytest

from POM.hotelbooking import HotelPage
from Data.reading_objects import ReadExcel
from Library.config import Config

class TestHotelPage:
    read_excel = ReadExcel()
    read_data= read_excel.read_test_data(Config.read_test_data)

    @pytest.mark.parametrize('destination_,mobile_,email_,f_name,l_name',read_data)
    def test_hotel(self,destination_,mobile_,email_,f_name,l_name,_driver):
        hotel = HotelPage(_driver)
        hotel.popup()
        hotel.click_hotel()
        hotel.destination(destination_)
        hotel.dropdown()
        hotel.date()
        hotel.sel_dropdown()
        hotel.button()
        hotel.book_button()
        hotel.continue_button()
        hotel.enter_mob(mobile_)
        hotel.enter_email(email_)
        hotel.button_continue()
        hotel.title_click()
        hotel.text_title()
        hotel.first_name(f_name)
        hotel.last_name(l_name)
        hotel.payment_btn()
