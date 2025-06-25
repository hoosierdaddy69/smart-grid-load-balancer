from flask import Flask, request
import requests

app = Flask(__name__)
LOAD_BALANCER_URL = "http://load_balancer:5001"

@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    response = requests.post(f"{LOAD_BALANCER_URL}/route", json=data)
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
