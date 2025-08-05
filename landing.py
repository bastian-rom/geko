from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Roomers is live</h1><p>Contact us for pharma and medtech growth.</p>"

# Only run the server if this script is executed directly
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
