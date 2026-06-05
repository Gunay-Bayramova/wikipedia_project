import re
import json
from bs4 import BeautifulSoup

class WikipediaScraper : 
    def __init__(self, session):
        self.session = session

    def fetch_html(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except:
            return ""

    def get_first_paragraph(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('p')

        for paragraph in paragraphs:
            text = paragraph.get_text(strip =True)
            if text:
                return text
        return ""
    
    def clean_text(self, text):
        cleaned_text = re.sub(r'\[\d+\]', '', text) 
        cleaned_text = re.sub(r'\[citation needed\]', '', cleaned_text, flags=re.IGNORECASE) 
        
        return cleaned_text
    
    def to_json_file(self, data, filepath):
        with open(filepath, 'w') as file:
            json.dump(data, file)
            

"""
Track 2: The HTML Scraper (src/html_scraper.py)
- Build a WikipediaScraper class responsible only for downloading and parsing HTML documents.
- Attributes: session (passed down from the parent application context).
- Methods:
    - fetch_html(url: str): Safely requests raw HTML text. Must include robust exception handling to deal with 404s, 500s, or connection drops.
    - get_first_paragraph(html: str): Parses raw HTML with BeautifulSoup, finds the first true biographical narrative paragraph (<p>), and returns it.
    - clean_text(text: str): A cleaning utility method to strip out unwanted characters, whitespace, or Wikipedia citation brackets (e.g., [1], [citation needed]).
    -  `to_json_file(filepath: str) -> None` stores the data structure into a JSON file

"""