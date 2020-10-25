from selenium.webdriver.common.by import By



class SignInPageLocators():

    sign_in_link = (By.XPATH, "//div[@class='header_user_info']//a")
    create_email_input = (By.ID, "email_create")
    create_button = (By.NAME, "SubmitCreate")
    sign_in_email_input = (By.ID, "email")
    sign_in_passwd_input = (By.ID, "passwd")
    sign_in_button = (By.NAME, "SubmitLogin")


class RegistrationPageLocators():

    mr_gender_select = (By.ID, "id_gender1")
    mrs_gender_select = (By.ID, "id_gender2")
    fname_input = (By.ID, "customer_firstname")
    lname_input = (By.ID, "customer_lastname")
    email_input = (By.ID, "email")
    passwd_input = (By.ID, "passwd")
    birth_day_select = (By.ID, "days")
    birth_month_select = (By.ID, "months")
    birth_year_select = (By.ID, "years")
    company_input = (By.ID, "company")
    address_input = (By.ID, "address1")
    city_input = (By.ID, "city")
    state_select = (By.ID, "id_state")
    post_input = (By.ID, "postcode")
    country_select = (By.ID, "id_country")
    phone_input = (By.ID, "phone_mobile")
    address_alias_input = (By.ID, "alias")
    register_button = (By.ID, "submitAccount")