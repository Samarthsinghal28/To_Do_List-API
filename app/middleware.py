from flask import request, current_app
from flask_jwt_extended import verify_jwt_in_request

@current_app.before_request
def check_jwt():
    if request.endpoint in ['create_todo', 'get_todos', 'get_todo_by_id', 'update_todo_by_id', 'delete_todo_by_id']:
        verify_jwt_in_request()
