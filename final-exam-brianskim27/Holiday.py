import requests

class Holiday:
    def __init__(self, num):
        """
        Initializes and gets access to the url
        args: self, num (int)
        return: none
        """
        self.api_url = 'https://holidayapi.com/v1/holidays?pretty&key=be18cdd0-36ad-45ae-8c50-0a8d17bfe185&country=US&year=2020'    
        
        self.num = num

    def get(self):
        """
        Receives and stores data from the website (holiday name and date)
        args: self
        return: Holiday name and date if access to the site is granted, None if access is not granted
        """
        self.result = requests.get(self.api_url)
        response = self.result.json()
        self.holiday = response['holidays'][self.num]

    def __str__(self):
        """
        Returns the string form of the holiday name and date
        args: self
        return: string form of the holiday name and date
        """
        return str(self.holiday['name']) + " (" + str(self.holiday['date']) + ")"
