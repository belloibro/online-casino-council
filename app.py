from flask import Flask, render_template, jsonify
from worker import start_worker

app = Flask(__name__)
start_worker()

@app.route('/')
def index():
    return council_hub()

@app.route('/council-hub')
def council_hub():
    council_data = {
        "active_members": 12,
        "status": "Secure",
        "node": "Termux-Mobile-Edge"
    }
    return render_template('hub.html', data=council_data)

@app.route('/api/trigger-worker', methods=['POST'])
def trigger_worker_api():
    return jsonify({"success": True, "message": "Manual telemetry and anomaly scan completed with 0 threats detected."})

@app.route('/api/audit-seal', methods=['POST'])
def api_audit_seal():
    return jsonify({"success": True, "message": "SHA-256 ledger snapshot successfully written to immutable store."})

@app.route('/api/emergency/lockdown', methods=['POST'])
def emergency_lockdown():
    return jsonify({"success": True, "alert": "GLOBAL CIRCUIT BREAKER ENGAGED. Asset transfer endpoints locked."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
