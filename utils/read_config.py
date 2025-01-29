import configparser

config = configparser.RawConfigParser()
config.read(".\\config\\config.ini")

class Read_Config:
    @staticmethod
    def get_login_page_url():
      url=  config.get('WB login info','login_page_url')
      return url

    @staticmethod
    def get_username():
        username = config.get('WB login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('WB login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('WB login info', 'invalid_username')
        return invalid_username
    
    @staticmethod
    def get_attachment_file_path():
        path = config.get('Add Trip info', 'attachment_file_path')
        return path
    
    @staticmethod
    def get_data_sheet_file_path():
        path = config.get('Add Trip info', 'data_sheet_path')
        return path


