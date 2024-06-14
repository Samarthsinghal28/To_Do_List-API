from datetime import datetime

def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "created_at": todo["created_at"].strftime("%Y-%m-%d %H:%M:%S")
    }

def validate_todo_data(data) -> dict:
    if "name" not in data or "description" not in data:
        return {"error": "name and description are required fields"}
    return {"name": data["name"], "description": data["description"], "created_at": datetime.utcnow()}
