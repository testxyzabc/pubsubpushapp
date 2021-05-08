import base64
import json

from flask import current_app, Flask, render_template, request
app = Flask(__name__)


# Global list to storage messages received by this instance.
MESSAGES = []

@app.route('/msgs')
def index():
    if request.method == 'GET':
        return render_template('index.html', messages=MESSAGES)

@app.route('/pubsub/push', methods=['POST'])
def pubsub_push():
    
    envelope = json.loads(request.data.decode('utf-8'))
    payload = base64.b64decode(envelope['message']['data'])

    MESSAGES.append(payload)
    return 'OK', 200
