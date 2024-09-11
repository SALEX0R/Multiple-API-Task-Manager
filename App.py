from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Complete Project Proposal", "description": "Draft a project proposal document outlining the objectives, timeline, and resources required"},
    {"id": 2, "name": "Schedule Meeting", "description": "Coordinate with team members to set up a meeting agenda and schedule"},
    {"id": 3, "name": "Notify Pending Task", "description": "Coordinate with team members to set up a huddle where Pending task becoming blockage for our project"}
]

# API Endpoints
@app.route("/items", methods=["GET"])
def get_all_items():
    """
    Retrieves all items.
    """
    return jsonify({"items": items})

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    """
    Retrieves a specific item based on its ID.
    """
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def create_item():
    """
    Creates a new item based on the request data.
    """
    data = request.get_json()
    if 'name' in data and 'description' in data:
        new_item = {
            "id": len(items) + 1,
            "name": data["name"],
            "description": data["description"]
        }
        items.append(new_item)
        return jsonify({"message": "Item created successfully", "item": new_item}), 201
    else:
        return jsonify({"message": "Missing name or description in request"}), 400

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """
    Deletes a specific item based on its ID.
    """
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": f"Item {item_id} deleted successfully"})

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
