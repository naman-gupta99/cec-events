import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.event_registration import EventRegistration
from service.event_list_service import EventListService

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")

if env == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
event_list_service = EventListService(db, app)
event_list_service.update_event_list()

@app.route("/event", methods=["POST"])
def event():
    data = request.get_json()
    user_id = data.get("user_id")
    event_id = data.get("event_id")

    if not user_id or not event_id:
        return jsonify({"error": "user_id and event_id are required"}), 400

    registration = EventRegistration(user_id=user_id, event_id=event_id)
    db.session.add(registration)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201

@app.route("/events", methods=["GET"])
def get_all_events():
    events = event_list_service.get_all_events()
    events.sort(key=lambda e: e.get_event_date())
    event_data = list(map(lambda e: e.to_dict(), events))
    return jsonify(event_data)

if __name__ == '__main__':
    app.run()