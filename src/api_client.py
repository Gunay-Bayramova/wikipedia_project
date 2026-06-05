from numpy import isin
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
        self.cookies = response.cookies
        
    def get_countries(self):
        if not self.cookies:
            self.refresh_cookies()
        
        response = self.session.get(f"{self.base_url}{self.country_endpoint}", cookies=self.cookies)
        return response.json()
        
        
    def get_leaders(self, country):

        if not self.cookies:
            self.refresh_cookies()
        
        response = self.session.get(
            f"{self.base_url}{self.leaders_endpoint}", 
            cookies=self.cookies,
            params={"country": country}
        )
        
        data = response.json()
        
        if  isinstance(data, dict):
            self.refresh_cookies()
            
            response = self.session.get(
                f"{self.base_url}{self.leaders_endpoint}", 
                cookies=self.cookies, 
                params={"country": country}
            )           
            
            data = response.json()
        
        return data
        