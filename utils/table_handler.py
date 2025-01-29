from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def verify_table_row(driver: WebDriver, table_locator: tuple, expected_values: list) -> bool:

    try:
        # Locate the table
        table = driver.find_element(*table_locator)
        
        # Locate all rows within the table (excluding header row)
        rows = table.find_elements(By.XPATH, ".//tr")
        
        for row in rows:
            # Get all cells in the current row
            cells = row.find_elements(By.XPATH, ".//td")
            
            # Extract text from each cell
            cell_texts = [cell.text.strip() for cell in cells]
            
            # Check if all expected values are present in the current row
            if all(value in cell_texts for value in expected_values):
                return True  # Match found

        return False  # No matching row found
    except Exception as e:
        print(f"Error while verifying table row: {e}")
        return False
    
def verify_table_row_partial(driver: WebDriver, table_locator: tuple, expected_values: list) -> bool:
    """
    Verify the presence of specific values in any row of a table, even if only a subset of values is provided.

    :param driver: Selenium WebDriver instance
    :param table_locator: Locator for the table element (e.g., (By.ID, "table-id"))
    :param expected_values: List of expected values to match in a row (partial match allowed)
    :return: True if a row contains the expected values, otherwise False
    """
    try:
        # Locate the table
        table = driver.find_element(*table_locator)
        
        # Locate all rows within the table (excluding header row)
        rows = table.find_elements(By.XPATH, ".//tr")
        
        for row in rows:
            # Get all cells in the current row
            cells = row.find_elements(By.XPATH, ".//td")
            
            # Extract text from each cell
            cell_texts = [cell.text.strip() for cell in cells]
            
            # Check if all expected values are present in the current row
            if all(value in cell_texts for value in expected_values):
                return True  # Match found

        return False  # No matching row found
    except Exception as e:
        print(f"Error while verifying table row: {e}")
        return False
    
from selenium.webdriver.remote.webdriver import WebDriver

def get_cell_value(driver: WebDriver,  row_no, column_no) -> str:

    try:
        cell_value = driver.find_element(By.XPATH, f"//table//tbody//tr[{row_no}]//td[{column_no}]")
        return cell_value.text.strip()
    except Exception as e:
        print(f"Error while retrieving cell value: {e}")
        return ""
    



