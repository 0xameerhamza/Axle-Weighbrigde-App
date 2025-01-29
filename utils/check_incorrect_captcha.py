class check_captcha_error_msg:

    def is_incorrect_captcha_message_present(self, driver):

        try:
            # Search for the text in the page source
            if "Incorrect Captcha" in driver.page_source:
                return True
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    # Usage example
    if is_incorrect_captcha_message_present(driver):
        print("The page contains 'Incorrect Captcha'.")
    else:
        print("The page does not contain 'Incorrect Captcha'.")
