***TO DO LIST API***

This project is a RESTful API for managing a collection of To-Do items, built with Flask and MongoDB. It includes user authentication using JSON Web Tokens (JWT) to ensure that only authenticated users can perform CRUD operations.

**Features**
* User Registration and Authentication: Users can register and log in to receive a JWT token.
* CRUD Operations: Create, retrieve, update, and delete To-Do items.
* JWT Middleware: Secure routes with JWT token validation.

**Project Structure :**

├── app<br />
│   ├── __init__.py<br />
│   ├── middleware.py<br />
│   ├── models.py<br />
│   └── routes.py<br />
├── .env<br />
├── requirements.txt<br />
├── run.py<br />
└── README.md<br />


**How to run :**

Run the Following commands in Terminal/Bash.<br />
1)Clone the Repository:<br />
* git clone https://github.com/Samarthsinghal28/To_Do_List-API.git<br />
* cd To_Do_List-API
  
2)Create and activate a virtual environment:<br />
* python -m venv venv<br />
* source venv/bin/activate

3)Install dependencies:<br />
* pip install -r requirements.txt

4)Set environment variables:<br />
* Create a .env file with the following content:<br />
  i)MONGO_URI=your_mongodb_connection_string<br />
  ii)JWT_SECRET_KEY=your_secret_key<br />

5)Run the application:<br />
 * python run.py<br />

**Testing the API :**

1)Register a new user:<br />
* curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'

2)Login to get a JWT token:<br />
* curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'

3)Create a new ToDo item:<br />
* curl -X POST http://localhost:5000/todos -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_JWT_TOKEN" -d '{"name": "Test ToDo", "description": "This is a test todo item"}'

4)Retrieve all ToDo items:<br />
* curl -X GET http://localhost:5000/todos -H "Authorization: Bearer YOUR_JWT_TOKEN"

5)Retrieve a specific ToDo item by ID:<br />
* curl -X GET http://localhost:5000/todos/YOUR_TODO_ID -H "Authorization: Bearer YOUR_JWT_TOKEN"

6)Update a specific ToDo item by ID:<br />
* curl -X PUT http://localhost:5000/todos/YOUR_TODO_ID -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_JWT_TOKEN" -d '{"name": "Updated ToDo", "description": "Updated description"}'

7)Delete a specific ToDo item by ID:<br />
* curl -X DELETE http://localhost:5000/todos/YOUR_TODO_ID -H "Authorization: Bearer YOUR_JWT_TOKEN"
