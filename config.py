import os

class Config:
    WEBSOCKET_URL = "ws://localhost:5000"

class ProductionConfig(Config):
    WEBSOCKET_URL = "wss://cec-events-604b31b937b9.herokuapp.com"
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_URL")).replace('postgres://', 'postgresql://', 1)
    
class DevelopmentConfig(Config):
    WEBSOCKET_URL = "ws://localhost:5000"
    SQLALCHEMY_DATABASE_URI = "postgresql://uf9vs1gr26qimf:p0162ed4e0e5cc49b0f9b916489987c0f508cf6c86dc99668e03a826186b4594c@ceqbglof0h8enj.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/degi8si8t791g2"