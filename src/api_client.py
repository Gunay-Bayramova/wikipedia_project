import requests

class CountryLeadersAPI:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"

        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"

        self.session = requests.Session()
        self.cookies = None

    def refresh_cookies(self):
        response = self.session.get(f"{self.base_url}{self.cookies_endpoint}")
        if response.status_code == 200:
            self.cookies = response.cookies
        else:
            raise Exception(f"Failed to refresh cookies: {response.status_code}")
        
    def get_countries(self):
        if not self.cookies:
            self.refresh_cookies()
        
        response = self.session.get(f"{self.base_url}{self.country_endpoint}", cookies=self.cookies)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get countries: {response.status_code}")
        
    def get_leaders(self, country):
        if not self.cookies:
            self.refresh_cookies()
        
        response = self.session.get(f"{self.base_url}{self.leaders_endpoint}/{country}", cookies=self.cookies)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get leaders for {country}: {response.status_code}")

"""
#### Track 1: The API Client (src/api_client.py)
- Build a CountryLeadersAPI class responsible only for communicating with the REST API.
    - Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
    - Methods:
        - refresh_cookie(): Checks validity and refreshes the session cookie when expired.
        - get_countries(): Queries the API and returns a clean list of supported country codes.
        - get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country
    
"""