import unittest
import requests
import random
import sqlite3 as sql


BASE_URL = 'http://127.0.0.1:5000/api/v1/recipes'
API_KEY = 'XTG34IU3P4O2TOHU245GHU245GPI45GPIHU45GPO425GPU45GPHU'

HEADERS = {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sql.connect('/path/to/recipes.db')
    conn.row_factory = sql.Row 
    return conn

def create_recipe_in_db():
    """Helper function to insert a recipe directly into the database and return its ID."""
    data = {
        'title': 'Spaghetti Bolognese',
        'ingredients': 'Spaghetti, minced beef, tomato sauce, onions, garlic, olive oil',
        'instructions': '1. Cook spaghetti. 2. Make sauce. 3. Mix and serve.'
    }
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO recipes (title, ingredients, instructions) 
        VALUES (?, ?, ?)
    ''', (data['title'], data['ingredients'], data['instructions']))
    
    conn.commit()
    recipe_id = cur.lastrowid
    conn.close()
    return recipe_id

class TestRecipeAPI(unittest.TestCase):
    """
    Unit test class for testing the Recipe CRUD API.
    This includes tests for all CRUD operations, authentication, and error handling.
    """

    def setUp(self):
        """
        Sets up the initial state for each test by initializing the recipe ID.
        This will be used to track created recipes across tests.
        """
        self.recipe_id = None

    def test_1_create_recipe(self):
        """
        Test creating a new recipe via the API (POST /recipes).
        
        Verifies:
        - Status code 201 (Created) is returned when the recipe is successfully created.
        - The returned response contains the correct recipe details.
        """
        new_recipe = {
            'title': 'Spaghetti Bolognese',
            'ingredients': 'Spaghetti, minced beef, tomato sauce, onions, garlic, olive oil',
            'instructions': '1. Cook spaghetti. 2. Make sauce. 3. Mix and serve.'
        }

        response = requests.post(BASE_URL, headers=HEADERS, json=new_recipe)
        self.assertEqual(response.status_code, 201, f"Failed to create recipe. Status code: {response.status_code}\n")

        created_recipe = response.json()
        self.recipe_id = created_recipe['id']
        print(f"Created recipe: {created_recipe}\n")

    def test_2_get_recipe(self):
        """
        Test retrieving an existing recipe via the API (GET /recipes/{id}).
        
        Verifies:
        - Status code 200 (OK) is returned when the recipe is successfully retrieved.
        - The retrieved recipe details match the expected data.
        """
        self.recipe_id = create_recipe_in_db()
        self.assertIsNotNone(self.recipe_id, "Recipe ID not set. Run create_recipe test first.\n")

        response = requests.get(f'{BASE_URL}/{self.recipe_id}', headers=HEADERS)
        self.assertEqual(response.status_code, 200, f"Failed to get recipe. Status code: {response.status_code}\n")

        recipe = response.json()
        print(f"Retrieved recipe: {recipe}\n")

    def test_3_update_recipe(self):
        """
        Test updating an existing recipe via the API (PUT /recipes/{id}).
        
        Verifies:
        - Status code 200 (OK) is returned when the recipe is successfully updated.
        - The updated recipe details match the provided input data.
        """
        self.assertIsNotNone(self.recipe_id, "Recipe ID not set. Run create_recipe test first.\n")

        updated_recipe = {
            'title': 'Updated Spaghetti Bolognese',
            'ingredients': 'Spaghetti, minced beef, tomato sauce, onions, garlic, olive oil, basil',
            'instructions': '1. Cook spaghetti. 2. Make sauce with basil. 3. Mix and serve.'
        }

        response = requests.put(f'{BASE_URL}/{self.recipe_id}', headers=HEADERS, json=updated_recipe)
        self.assertEqual(response.status_code, 200, f"Failed to update recipe. Status code: {response.status_code}\n")

        updated_recipe_data = response.json()
        print(f"Updated recipe: {updated_recipe_data}")

    def test_4_delete_recipe(self):
        """
        Test deleting an existing recipe via the API (DELETE /recipes/{id}).
        
        Verifies:
        - Status code 204 (No Content) is returned when the recipe is successfully deleted.
        - After deletion, the recipe cannot be retrieved.
        """
        self.assertIsNotNone(self.recipe_id, "Recipe ID not set. Run create_recipe test first.\n")

        response = requests.delete(f'{BASE_URL}/{self.recipe_id}', headers=HEADERS)
        self.assertEqual(response.status_code, 204, f"Failed to delete recipe. Status code: {response.status_code}")

        print(f"Deleted recipe with ID: {self.recipe_id}")

    def test_5_get_deleted_recipe(self):
        """
        Test retrieving a deleted recipe (GET /recipes/{id}) after it has been removed.
        
        Verifies:
        - Status code 404 (Not Found) is returned when trying to retrieve a deleted recipe.
        """
        self.assertIsNotNone(self.recipe_id, "Recipe ID not set. Run create_recipe test first.\n")

        response = requests.get(f'{BASE_URL}/{self.recipe_id}', headers=HEADERS)
        self.assertEqual(response.status_code, 404, f"Expected 404 for deleted recipe, but got {response.status_code}\n")

    def test_6_invalid_api_key(self):
        """
        Test accessing the API with an invalid API key (Unauthorized access).
        
        Verifies:
        - Status code 401 (Unauthorized) is returned when an invalid API key is provided.
        """
        invalid_headers = {
            'X-API-Key': 'INVALID_KEY',
            'Content-Type': 'application/json'
        }

        response = requests.get(BASE_URL, headers=invalid_headers)
        self.assertEqual(response.status_code, 401, "Expected 401 for invalid API key, but got {response.status_code}\n")

    def test_7_sql_injection_protection(self):
        """
        Test the API's protection against SQL injection by attempting to pass SQL commands in the input.
        
        Verifies:
        - Status code 400 or 422 (Bad Request / Unprocessable Entity) is returned for dangerous inputs.
        """
        malicious_input = {
            'title': "'; DROP TABLE recipes;--",
            'ingredients': 'N/A',
            'instructions': 'N/A'
        }

        response = requests.post(BASE_URL, headers=HEADERS, json=malicious_input)
        self.assertNotEqual(response.status_code, 201, "SQL Injection attempt should not succeed.")
        self.assertIn(response.status_code, [400, 422], f"Unexpected status code: {response.status_code}")

if __name__ == '__main__':
    unittest.main()
