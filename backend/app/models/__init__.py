from app.extensions import db
from datetime import datetime
from app.utils import serialize_doc

def get_all_thoughts():
    thoughts = db.thoughts.find().sort("timestamp",-1)
    return [serialize_doc(t) for t in thoughts]

def create_thought(text):
    new_thought = {
        "text" : text,
        "timestamp" : datetime.utcnow().isoformat()
    }
    result = db.thoughts.insert_one(new_thought)
    return str(result.inserted_id)