from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API!")

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'id': 1,
        'name': 'Sample Data',
        'description': 'This is a sample data entry.'
    }
    return jsonify(sample_data)

@app.route('/api/data', methods=['POST'])
def create_data():
    new_data = request.get_json()
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)