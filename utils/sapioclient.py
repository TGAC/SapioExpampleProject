import requests
import json
import os

class SapioClient:
    """
    A client for interacting with the Sapio API.

    Attributes:
        url (str): The URL of the Sapio API.
        api_token (str): The API token for authentication.
        guid (str): The GUID for the Sapio application.
        session (requests.Session): The session object for making HTTP requests.
    """

    def __init__(self):
        self.url = os.getenv('SAPIOURL')
        self.api_token = os.getenv('SAPIOTOKEN')
        self.guid = os.getenv('SAPIOGUID')
        self.session = requests.Session()
        self.session.headers = {'X-APP-KEY': self.guid, 'X-API-TOKEN': self.api_token}

    def do_get(self, method, params={}):
        """
        Sends a GET request to the Sapio API.

        Args:
            method (str): The API method to call.
            params (dict): Optional parameters for the API method.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API returns an error status code.
        """
        if method.startswith('/'):
            url = self.url + method
        else:
            url = self.url + '/' + method
        resp = self.session.get(url, params=params)
        if resp.status_code != 200:
            raise Exception('Error: ' + str(resp.status_code) + ' ' + resp.text)
        else:
            return json.loads(resp.text)
        

    