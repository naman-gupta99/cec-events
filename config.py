import os

class Config:
    pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_URL")).replace('postgres://', 'postgresql://', 1)
    RSS_FEED_URL = "https://25livepub.collegenet.com/calendars/pitt_cech_events.rss"
    
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:password@localhost:5432/cec_events"
    RSS_FEED_URL = "https://25livepub.collegenet.com/calendars/pitt_cech_events.rss"