from service.rss_feed_service import RssFeedService
from flask_sqlalchemy import SQLAlchemy

class EventListService:
    def __init__(self, event_list_repository: SQLAlchemy, app):
        self.event_list_repository = event_list_repository
        self.rss_feed_service = RssFeedService(app.config)
        self.app = app

    def update_event_list(self):
        try:
            with self.app.app_context():
                feed = self.rss_feed_service.get_events_from_feed()
                self.event_list_repository.session.add_all(feed)
                self.event_list_repository.session.commit()
        except Exception as e:
            print(f"Failed to update event list: {e}")