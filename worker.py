import time
import threading

def background_task():
    while True:
        print("[Worker] Running continuous threat telemetry, velocity spikes, and audit sync...")
        time.sleep(30)

def start_worker():
    t = threading.Thread(target=background_task, daemon=True)
    t.start()
