from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from .models import todo_serializer, validate_todo_data
from pymongo.mongo_client import MongoClient
import os
from . import mongo

MONGO_DB_URL = os.getenv("MONGO_URI")
client = MongoClient(MONGO_DB_URL)

@current_app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400
    
    db = client.get_database("To-do-list")
    collection_users = db.users

    user = collection_users.find_one({"username": username})
    if user:
        return jsonify({"msg": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)
    collection_users.insert_one({"username": username, "password": hashed_password})
    return jsonify({"msg": "User registered successfully"}), 201

@current_app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    db = client.get_database("To-do-list")
    collection_users = db.users

    user = collection_users.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity={"username": username})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@current_app.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    data = request.get_json()
    validated_data = validate_todo_data(data)
    if "error" in validated_data:
        return jsonify(validated_data), 400
    
    db = client.get_database("To-do-list")
    collection_todo = db["to-dos"]

    todo_id = collection_todo.insert_one(validated_data).inserted_id
    todo = collection_todo.find_one({"_id": todo_id})
    return jsonify(todo_serializer(todo)), 201

@current_app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():

    db = client.get_database("To-do-list")
    collection_todo = db["to-dos"]

    todos = collection_todo.find()
    return jsonify([todo_serializer(todo) for todo in todos]), 200

@current_app.route('/todos/<todo_id>', methods=['GET'])
@jwt_required()
def get_todo_by_id(todo_id):

    db = client.get_database("To-do-list")
    collection_todo = db["to-dos"]


    todo = collection_todo.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        return jsonify({"msg": "Todo not found"}), 404
    return jsonify(todo_serializer(todo)), 200

@current_app.route('/todos/<todo_id>', methods=['PUT'])
@jwt_required()
def update_todo_by_id(todo_id):
    data = request.get_json()
    
    validated_data = validate_todo_data(data)
    if "error" in validated_data:
        return jsonify(validated_data), 400
    
    db = client.get_database("To-do-list")
    collection_todo = db["to-dos"]

    collection_todo.update_one({"_id": ObjectId(todo_id)}, {"$set": validated_data})
    todo = collection_todo.find_one({"_id": ObjectId(todo_id)})
    return jsonify(todo_serializer(todo)), 200

@current_app.route('/todos/<todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo_by_id(todo_id):
    db = client.get_database("To-do-list")
    collection_todo = db["to-dos"]

    result = collection_todo.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        return jsonify({"msg": "Todo not found"}), 404
    return jsonify({"msg": "Todo deleted"}), 200
