import os

class Config:
    WEBSOCKET_URL = "ws://localhost:5000"

class ProductionConfig(Config):
    WEBSOCKET_URL = "wss://cec-events-604b31b937b9.herokuapp.com"
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_URL")).replace('postgres://', 'postgresql://', 1)
    
class DevelopmentConfig(Config):
    WEBSOCKET_URL = "ws://localhost:5000"
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:password@localhost:5432/cec_events"