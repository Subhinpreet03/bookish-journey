from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for processed data
processed_data_storage = {}


# Simulated data retrieval function
def fetch_data():
    # Mock data simulating an external service (e.g., Shopify)
    return {
        "order_id": 12345,
        "customer_name": "John Doe",
        "items": ["Shirt", "Pants", "Shoes"],
        "total_price": 150.00
    }


# Data processing function
def process_data(data):
    # Convert customer name to uppercase and total price to an integer
    data['customer_name'] = data['customer_name'].upper()
    data['total_price'] = int(data['total_price'])
    return data


# API Endpoint for Data Retrieval
@app.route('/fetch-data', methods=['GET'])
def fetch_data_endpoint():
    data = fetch_data()
    return jsonify(data), 200


# API Endpoint for Data Processing and Storage
@app.route('/process-data', methods=['POST'])
def process_data_endpoint():
    data = fetch_data()
    processed_data = process_data(data)
    processed_data_storage[data['order_id']] = processed_data
    return jsonify({"message": "Data processed and stored successfully"}), 200


# API Endpoint to Retrieve Processed Data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data_endpoint():
    return jsonify(processed_data_storage), 200


if __name__ == '__main__':
    app.run(debug=True)
