from service.rss_feed_service import RssFeedService
from flask_sqlalchemy import SQLAlchemy
from model.event import Event
import threading
import time

class EventListService:
    def __init__(self, event_list_repository: SQLAlchemy, app):
        self.event_list_repository = event_list_repository
        self.rss_feed_service = RssFeedService(app.config)
        self.app = app
        self.event_ids = self._load_event_ids()

    def _load_event_ids(self):
        with self.app.app_context():
            events = self.event_list_repository.session.query(Event.id).all()
            return set(event.id for event in events)

    def update_event_list(self):
        try:
            def run_update():
                while True:
                    with self.app.app_context():
                        print("Updating event list...")
                        feed = self.rss_feed_service.get_events_from_feed()
                        new_events = [event for event in feed if event.id not in self.event_ids]
                        if new_events:
                            self.event_list_repository.session.add_all(new_events)
                            self.event_list_repository.session.commit()
                            self.event_ids.update(event.id for event in new_events)
                    time.sleep(300)  # Sleep for 5 minutes

            update_thread = threading.Thread(target=run_update)
            update_thread.daemon = True
            update_thread.start()
        except Exception as e:
            print(f"Failed to update event list: {e}")
    
    def get_all_events(self):
        return self.event_list_repository.session.query(Event).all()