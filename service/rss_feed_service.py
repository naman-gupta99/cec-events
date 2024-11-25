import requests
import xml.etree.ElementTree as ET
from model.event import Event

class RssFeedService:
    
    def __init__(self, config):
        self.url = config.get("RSS_FEED_URL")
    
    def get_events_from_feed(self) -> list[Event]:
        feed = self.__fetch_and_parse_feed()
        return [self.__extract_event_data(item) for item in feed.findall("channel/item")]
    
    def __fetch_and_parse_feed(self) -> ET.Element:
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch feed: {response.status_code}")
        return ET.fromstring(response.content)

    def __extract_event_data(self, item) -> Event:
        """Extracts event data from an XML item element."""
        title = item.find("title").text
        description = item.find("description").text
        link = item.find("link").text
        category = item.find("category").text
        pub_date = item.find("pubDate").text

        return Event(title=title, description=description, link=link, category=category, pub_date=pub_date)