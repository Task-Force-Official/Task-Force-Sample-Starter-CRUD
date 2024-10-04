# Task Force Competition: Recipe CRUD API

## Introduction

Welcome to **Task Force**, where your coding skills will be tested in building a secure, functional, and well-documented **Recipe CRUD API**. This task challenges you to create an API that allows authenticated users to manage recipes in a SQLite database. You will need to ensure proper API key-based authentication and safeguard the API against SQL injection attacks. Additionally, we have written unit tests to verify that your implementation meets all the requirements.

Your API should be capable of the following:
- **CRUD Operations**: Create, Read, Update, and Delete recipes.
- **Authentication**: API key-based security.
- **Database**: Persistent storage using SQLite.
- **Security**: SQL injection prevention.
- **Testing**: Write unit tests for all functionalities.

---

## Task Requirements

### 1. API Specifications

You are tasked with developing a **Recipe CRUD API** with the following specifications:

- **API Version**: 1.0
- **Base URL**: `/api/v1`

### 2. Endpoints

The API should support the following endpoints:

- **POST /api/v1/recipes**  
  Creates a new recipe.
  
  - Request body (JSON):
    - `title`: The title of the recipe (string).
    - `ingredients`: The list of ingredients (array).
    - `instructions`: The instructions for making the recipe (string).
  
  - Status codes:
    - `201 Created`: Recipe successfully created.
    - `400 Bad Request`: Invalid input data.
    - `401 Unauthorized`: API key missing or invalid.

- **GET /api/v1/recipes**  
  Retrieves a list of all recipes.
  
  - Status codes:
    - `200 OK`: Successfully fetched the list of recipes.
    - `401 Unauthorized`: API key missing or invalid.

- **GET /api/v1/recipes/{id}**  
  Retrieves a specific recipe by ID.
  
  - URL parameters:
    - `id`: The ID of the recipe (integer).
  
  - Status codes:
    - `200 OK`: Successfully retrieved the recipe.
    - `404 Not Found`: Recipe with the specified ID does not exist.
    - `401 Unauthorized`: API key missing or invalid.

- **PUT /api/v1/recipes/{id}**  
  Updates an existing recipe by ID.
  
  - URL parameters:
    - `id`: The ID of the recipe (integer).
  
  - Request body (JSON):
    - `title`: Updated title of the recipe (string).
    - `ingredients`: Updated list of ingredients (array).
    - `instructions`: Updated instructions (string).
  
  - Status codes:
    - `200 OK`: Recipe successfully updated.
    - `400 Bad Request`: Invalid input data.
    - `404 Not Found`: Recipe with the specified ID does not exist.
    - `401 Unauthorized`: API key missing or invalid.

- **DELETE /api/v1/recipes/{id}**  
  Deletes a specific recipe by ID.
  
  - URL parameters:
    - `id`: The ID of the recipe (integer).
  
  - Status codes:
    - `204 No Content`: Recipe successfully deleted.
    - `404 Not Found`: Recipe with the specified ID does not exist.
    - `401 Unauthorized`: API key missing or invalid.

---

## API Security

Your API must be secured using **API keys**:
- Requests must include an `X-API-Key` header with a valid key.
- If the key is missing or invalid, the API should return a `401 Unauthorized` response.

Example API Key Header:
```
X-API-Key: your_api_key_here
```

---

## Database Setup

- Use **SQLite** as the database engine.
- The database should have a table to store recipes with the following fields:
  - `id`: Auto-incremented primary key.
  - `title`: Text field for the recipe title.
  - `ingredients`: Text field for the list of ingredients.
  - `instructions`: Text field for the recipe instructions.

Ensure that all database interactions are **protected against SQL injection** by using parameterized queries.

---

## YAML Structure Example

To ensure your API is well-structured, you are required to create a **YAML file** that outlines the API structure. Below is an example structure you can follow, but ensure you create your own design:

```yaml
api:
    version: 1.0
    title: Sample CRUD API
    description: API for managing resources with authentication
    base_url: /api/v1

authentication:
    type: API Key
    header_name: X-API-Key
    required: true

endpoints:
    - path: /resources
        methods:
            - GET:
                    description: Retrieve all resources
                    responses:
                        200: Success
                        401: Unauthorized
            - POST:
                    description: Create a new resource
                    request_body:
                        type: application/json
                        required: true
                        schema:
                            properties:
                                name: 
                                    type: string
                                    description: Name of the resource
                                details: 
                                    type: string
                                    description: Details of the resource
                    responses:
                        201: Created
                        400: Bad Request
                        401: Unauthorized
    - path: /resources/{id}
        methods:
            - GET:
                    description: Retrieve a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    responses:
                        200: Success
                        404: Not found
                        401: Unauthorized
            - PUT:
                    description: Update a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    request_body:
                        type: application/json
                        required: true
                        schema:
                            properties:
                                name: 
                                    type: string
                                    description: Updated name of the resource
                                details: 
                                    type: string
                                    description: Updated details of the resource
                    responses:
                        200: Updated
                        400: Bad Request
                        404: Not found
                        401: Unauthorized
            - DELETE:
                    description: Delete a resource by ID
                    parameters:
                        - name: id
                            in: path
                            required: true
                            type: integer
                    responses:
                        204: No Content
                        404: Not found
                        401: Unauthorized
```

---

## Testing

Your code must pass all the unit tests provided in the test.py file created using **Python's `unittest` framework** to validate your API. To pass the test you should include:

- CRUD operations (create, read, update, delete).
- API key authentication.
- Error responses (e.g., 404 for non-existing recipes, 401 for unauthorized access).
- Prevention for SQL injection vulnerabilities.

You can check if you pass the tests by running

```bash
python3 src/test.py
```

in a terminal window open in the project directory

---

## Submission Guidelines

Your submission should include the following:
1. **API source code**: Flask or any other framework in Python
2. **SQLite database**: Include a pre-populated `recipes.db` file with sample data.
3. **YAML file**: A structured `api.yaml` describing the API.
4. **Unit tests**: Python `unittest` file that tests all API endpoints.
5. **README**: A short explanation of how to run the API and tests.

6. **Virtual Environment**: A `requirements.txt` file listing all the python dependancies used in your codebase to emulate the environment needed by your source code to run
---

## Good Luck!

We wish you the best of luck in completing the task. This is your chance to show your skills in building secure, scalable APIs. Make sure to focus on best practices and clean code!
