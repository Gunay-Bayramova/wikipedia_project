
from src.api_client import CountryLeadersAPI
from src.html_scraper import WikipediaScraper

api = CountryLeadersAPI()

scraper = WikipediaScraper(api.session)

countries = api.get_countries()

leaders_per_country = {}

for country in countries:

    leaders = api.get_leaders(country)

    for leader in leaders:

        wikipedia_url = leader["wikipedia_url"]

        html = scraper.fetch_html(wikipedia_url)

        paragraph = scraper.get_first_paragraph(html)

        paragraph = scraper.clean_text(paragraph)

        leader["first_paragraph"] = paragraph

    leaders_per_country[country] = leaders

scraper.to_json_file(leaders_per_country, "leaders.json")