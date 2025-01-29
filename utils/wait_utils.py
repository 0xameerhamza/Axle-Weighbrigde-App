from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    def __init__(
            self,
            driver,
            timeout=10):
        """
        Initializes the WaitUtils class.

        :param driver: Selenium WebDriver instance
        :param timeout: Default timeout for waits (in seconds)
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(
            driver,
            timeout)

    def wait_for_visibility(
            self,
            locator_type,
            locator_value):
        """
        Waits for an element to be visible on the page.

        :param locator_type: Locator type (e.g., By.ID, By.XPATH, etc.)
        :param locator_value: Locator value
        :return: The visible WebElement
        """
        return self.wait.until(
            EC.visibility_of_element_located(
                (
                locator_type,
                locator_value)))

    def wait_for_clickable(
            self,
            locator_type,
            locator_value):
        """
        Waits for an element to be clickable.

        :param locator_type: Locator type (e.g., By.ID, By.XPATH, etc.)
        :param locator_value: Locator value
        :return: The clickable WebElement
        """
        return self.wait.until(
            EC.element_to_be_clickable(
                (
                locator_type,
                locator_value)))

    def wait_for_presence(
            self,
            locator_type,
            locator_value):
        """
        Waits for an element to be present in the DOM.

        :param locator_type: Locator type (e.g., By.ID, By.XPATH, etc.)
        :param locator_value: Locator value
        :return: The WebElement
        """
        return self.wait.until(
            EC.presence_of_element_located(
                (
                locator_type,
                locator_value)))

# Example usage:
# from wait_utils import WaitUtils
# wait_utils = WaitUtils(driver)
# element = wait_utils.wait_for_visibility(By.ID, "element_id")
