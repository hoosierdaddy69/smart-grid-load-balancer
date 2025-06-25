# Entry point for load balancer
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SUBSTATIONS = ["http://substation1:5002", "http://substation2:5002"]

def get_load(substation):
    try:
        response = requests.get(f"{substation}/metrics")
        for line in response.text.splitlines():
            if "active_sessions" in line:
                return int(float(line.split()[-1]))
    except:
        return float('inf')
    return float('inf')

@app.route("/route", methods=["POST"])
def route():
    data = request.json
    target = min(SUBSTATIONS, key=get_load)
    requests.post(f"{target}/charge", json=data)
    return jsonify({"routed_to": target})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
