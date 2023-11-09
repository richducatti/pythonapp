"""
A simple Flask app to greet visitors.
"""
from flask import Flask, request, redirect
from flask import jsonify
import os
from os import environ as env
from dotenv import load_dotenv
import hashlib

load_dotenv()

app = Flask(__name__)

try: 
    os.mkdir(env['FOLDER_NAME'])
except OSError as error: 
    print(error)  

@app.before_request
def redirect_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

"""
"""
@app.route("/")
def say_hello():
    return env['HELLO_WORLD']

"""
greeting
"""
@app.route("/<greeting>")
def display_custom_message(greeting):
    return str(greeting)

   
"""
Create a file with Data Result
"""
def create_file(data):
    if not os.path.exists('files'):
        os.makedirs('files')
    # Create file for each data item
    for item in data:
        id = item['id']
        name = item['name']
        hashed_id = hashlib.sha256(id.encode('utf-8')).hexdigest()
        # Create file in files directory with id.txt filename and name as contents
        with open(f'files/{hashed_id}.txt', 'w') as file:
            file.write(name)
    return 'Files created successfully'
"""
Return sample JSON data
"""
@app.route("/data")
def data():
    data = [
        {"name":"one","id":"1"},
        {"name":"two","id":"2"},
        {"name":"three","id":"3"}
    ]
    create_file(data)
    return jsonify(data)

"""
Runtime
"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

