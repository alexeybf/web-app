from flask import Flask, request, render_template
from flask import jsonify
import sys

app = Flask(__name__, template_folder='', static_folder='')

@app.route('/', methods=['GET'])
def index():
        return render_template('index.html')

reply_count=0

@app.route('/sendbutton_request', methods=['POST'])
def process_sendbutton():
    global reply_count
    reply_count += 1
    print("Got request data: {}".format(request.form))
    input_data = request.form.get("input")

    return jsonify("some reply from server! #{}".format(reply_count))

if __name__ == '__main__':
    app.run(debug=True)