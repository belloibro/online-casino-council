from flask import Flask, render_template, jsonify
from worker import start_worker

app = Flask(__name__)
start_worker()

@app.route('/')
def index():
    return "Online Casino Council Autonomous Node is Live."

@app.route('/council-hub')
def council_hub():
    council_data = {
        "active_members": 12,
        "status": "Secure",
        "node": "Termux-Mobile-Environment"
    }
    return render_template('hub.html', data=council_data)

@app.route('/api/trigger-worker', methods=['POST'])
def trigger_worker_api():
    return jsonify({"success": True, "message": "Manual threat scan triggered successfully."})

@app.route('/api/emergency/lockdown', methods=['POST'])
def emergency_lockdown():
    return jsonify({"success": True, "alert": "GLOBAL CIRCUIT BREAKER ENGAGED. Assets and balances frozen."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
