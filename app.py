
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host='localhost', port=6379)

@app.route('/')
def home():
    return "Book Recommendation System is running."

if __name__ == '__main__':
    app.run(debug=True)
