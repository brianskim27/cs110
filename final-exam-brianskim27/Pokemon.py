import requests

class Pokemon:
    """
    Initializes and gets access to the url that uses a random number
    args: self, ran_num (int)
    return: none
    """
    def __init__(self, ran_num):
        self.ran_num = ran_num
        self.api_url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(self.ran_num)
       
    
    def get(self):
        """
        Receives and stores data from the website (pokemon name based on its number)
        args: self
        return: Name of the pokemon assigned to the random number if access to the site is granted, None if access to the site is not granted
        """
        self.result = requests.get(self.api_url)
        response = self.result.json()
        self.pokemon = response['forms'][0]


    def __str__(self):
        """
        Returns the string form of the pokemon name and the number it is identified by
        args: self
        return: string form of the pokemon name and the number it is identified by
        """
        return str(self.pokemon['name'].capitalize()) + " (#" + str(self.ran_num) + ")"