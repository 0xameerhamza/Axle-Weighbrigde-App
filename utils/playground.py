from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TableUtils:
    def __init__(self, driver: WebDriver):
        """
        Initializes the TableUtils class with the WebDriver instance.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def get_table_row_count(self, table_locator: tuple) -> int:
        """
        Gets the total number of rows in the table.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :return: Number of rows in the table.
        """
        rows = self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr")
        return len(rows)

    def get_table_column_count(self, table_locator: tuple) -> int:
        """
        Gets the total number of columns in the table.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :return: Number of columns in the table.
        """
        columns = self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr[1]//th")
        if not columns:
            columns = self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr[1]//td")
        return len(columns)

    def get_cell_value(self, table_locator: tuple, row: int, column: int) -> str:
        """
        Gets the value of a specific cell in the table.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :param row: Row number (1-based index).
        :param column: Column number (1-based index).
        :return: Value of the cell as a string.
        """
        cell = self.driver.find_element(By.XPATH, f"{table_locator[1]}//tr[{row}]//td[{column}]")
        return cell.text.strip()

    def find_row_by_cell_value(self, table_locator: tuple, column: int, value: str) -> int:
        """
        Finds the row number where a specific value exists in a given column.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :param column: Column number (1-based index).
        :param value: Value to search for.
        :return: Row number (1-based index) or -1 if not found.
        """
        rows = self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr")
        for i, row in enumerate(rows, start=1):
            cell = row.find_element(By.XPATH, f"./td[{column}]")
            if cell.text.strip() == value:
                return i
        return -1

    def click_cell_button(self, table_locator: tuple, row: int, column: int):
        """
        Clicks a button inside a specific cell in the table.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :param row: Row number (1-based index).
        :param column: Column number (1-based index).
        """
        button = self.driver.find_element(By.XPATH, f"{table_locator[1]}//tr[{row}]//td[{column}]//button")
        button.click()

    def get_all_table_data(self, table_locator: tuple) -> list:
        """
        Gets all data from the table as a list of dictionaries.

        :param table_locator: Tuple with (By, value) to locate the table element.
        :return: List of dictionaries where each dictionary represents a row with column headers as keys.
        """
        headers = [header.text.strip() for header in self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr[1]//th")]
        rows = self.driver.find_elements(By.XPATH, f"{table_locator[1]}//tr[position()>1]")
        table_data = []

        for row in rows:
            cells = row.find_elements(By.XPATH, "./td")
            row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
            table_data.append(row_data)

        return table_data
