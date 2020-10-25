import pytest

from page_objects.sign_in_page_object import SignInPage

from utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestRegistration():

    @pytest.mark.parametrize("reg_data", ExcelReader.get_reg_data())
    def test_registration_initial_form(self, reg_data):

        sign_in_page = SignInPage(self.driver)
        sign_in_page.open_sign_in_page()
        sign_in_page.open_registration_form(reg_data.email)
        assert sign_in_page.is_register_button()

    # def test_registration_main_form(self):