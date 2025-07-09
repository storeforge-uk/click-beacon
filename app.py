from flask import Flask, request, send_file
from datetime import datetime
import csv
import os

app = Flask(__name__)

LOG_FILE = 'log.csv'

# Make sure the log file exists with headers
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['email', 'timestamp', 'ip'])

@app.route('/track_open')
def track_open():
    email = request.args.get('email', 'unknown')
    ip = request.remote_addr
    timestamp = datetime.utcnow().isoformat()

    # Append to the log file
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email, timestamp, ip])

    return send_file('pixel.png', mimetype='image/png')

@app.route('/')
def home():
    return 'Pixel tracker is running.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
