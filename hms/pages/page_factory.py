from hms.pages.login_page import Login_Page
from hms.pages.main_page import Main_Page


class Page_Factory():
    """ Returns the appropriate page object based on the name of the page """

    def get_page_object(page_name, driver, base_url='http://localhost:8084/console/'):
        """Return the appropriate page object based on page_name"""

        test_page_object = None
        page_name = page_name.lower()
        if page_name == "login":
            test_page_object = Login_Page(driver, base_url=base_url)
        elif page_name == "main":
            test_page_object = Main_Page(driver, base_url=base_url)

        return test_page_object

