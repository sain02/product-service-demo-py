from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for local development)
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Enable CORS (allow any origin, restrict to GET)
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# Define the /products route
@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

if __name__ == "__main__":
    # Get port from environment or default to 3030
    port = int(os.getenv("PORT", 3030))
    # Run Flask app (host=0.0.0.0 makes it accessible externally, like Warp did)
    app.run(host="0.0.0.0", port=port)
