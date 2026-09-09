import time
import threading

def background_task():
    while True:
        print("[Worker] Running background health check and event sync...")
        time.sleep(30)

def start_worker():
    t = threading.Thread(target=background_task, daemon=True)
    t.start()
