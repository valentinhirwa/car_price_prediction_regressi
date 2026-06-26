# test.py - with flush
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>🚗 Flask is working!</h1><p>Your car price predictor is ready.</p>'

if __name__ == '__main__':
    print("=" * 50, flush=True)
    print("🚀 Starting Flask server...", flush=True)
    print("🌐 Open: http://127.0.0.1:5000", flush=True)
    print("=" * 50, flush=True)
    sys.stdout.flush()
    app.run(debug=True, host='127.0.0.1', port=5000)