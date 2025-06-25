import requests
import time
import random

BASE_URL = "http://localhost:5000/charge"

def simulate_ev_charging(ev_count=20, delay_range=(0.2, 1.0)):
    for i in range(ev_count):
        vehicle_id = f"EV_{i}"
        try:
            response = requests.post(BASE_URL, json={"vehicle_id": vehicle_id})
            print(f"[{vehicle_id}] Routed to: {response.json().get('routed_to')}")
        except Exception as e:
            print(f"[{vehicle_id}] Failed: {e}")
        time.sleep(random.uniform(*delay_range))

if __name__ == "__main__":
    simulate_ev_charging()
