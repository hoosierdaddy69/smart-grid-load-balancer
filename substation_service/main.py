from flask import Flask, request
from prometheus_client import start_http_server, Gauge
import threading

app = Flask(__name__)
active_sessions = 0
active_sessions_gauge = Gauge('active_sessions', 'Current number of active EV charging sessions')


@app.route("/charge", methods=["POST"])
def charge():
    global active_sessions
    # Simulate starting a new EV charging session
    active_sessions += 1
    active_sessions_gauge.set(active_sessions)

    # Simulate charging time with a timer (10 seconds per session)
    def finish_session():
        global active_sessions
        active_sessions -= 1
        active_sessions_gauge.set(active_sessions)

    threading.Timer(10.0, finish_session).start()

    return {"status": "charging_started", "current_sessions": active_sessions}


if __name__ == "__main__":
    # Start Prometheus metrics server on the same port
    start_http_server(5002)
    app.run(host="0.0.0.0", port=5002)
# Entry point for substation service
