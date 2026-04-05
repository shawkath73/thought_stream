from flask import Blueprint, request, jsonify
from app.models import get_all_thoughts, create_thought
from app import extensions
from bson import ObjectId

# 1. Create the Traffic Cop (Blueprint)
# It intercepts any internet traffic trying to go to '/api/thoughts'
thoughts_bp = Blueprint('thoughts', __name__, url_prefix='/api/thoughts')

# 2. The "Read" Endpoint (GET)
@thoughts_bp.route('', methods=['GET'])
def fetch_thoughts():
    # Ask the worker file for the thoughts, package them into JSON, and send a 200 (OK) code
    return jsonify(get_all_thoughts()), 200

# 3. The "Write" Endpoint (POST)
@thoughts_bp.route('', methods=['POST'])
def add_thought():
    # Unpack the data the user sent over the internet
    data = request.get_json()
    
    # Security check: Make sure they actually sent text
    if not data or not data.get('text'):
        # If blank, reject it and send a 400 (Bad Request) code
        return jsonify({"error": "Text is required"}), 400
        
    # Hand the text to the worker file to save in the database
    thought_id = create_thought(data['text'])
    
    # Send a success message back with a 201 (Created) code
    return jsonify({"message": "Thought saved!", "id": thought_id}), 201

@thoughts_bp.route('/<thought_id>', methods=['DELETE'])
def delete_thought(thought_id):
    db = extensions.db
    result = db.thoughts.delete_one({'_id': ObjectId(thought_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404

@thoughts_bp.route('/<thought_id>/like', methods=['PATCH'])
def like_thought(thought_id):
    db = extensions.db
    # This increments a 'likes' counter in MongoDB automatically
    db.thoughts.update_one(
        {'_id': ObjectId(thought_id)},
        {'$inc': {'likes': 1}}
    )
    return jsonify({"message": "Liked"}), 200